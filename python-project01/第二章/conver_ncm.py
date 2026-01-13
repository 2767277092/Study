import struct
import base64
import json
from Crypto.Cipher import AES

def ncm_to_audio(ncm_path, output_name):
    with open(ncm_path, 'rb') as f:
        f.read(8)  # 跳过文件头

        key_len = struct.unpack('<I', f.read(4))[0]
        key_data = bytearray(f.read(key_len))
        for i in range(len(key_data)):
            key_data[i] ^= 0x64

        core_key = b'neteasecloudmusic'
        aes = AES.new(core_key, AES.MODE_ECB)
        key_data = aes.decrypt(bytes(key_data))[17:]

        key_box = list(range(256))
        j = 0
        for i in range(256):
            j = (j + key_box[i] + key_data[i % len(key_data)]) & 0xff
            key_box[i], key_box[j] = key_box[j], key_box[i]

        f.read(4)
        meta_len = struct.unpack('<I', f.read(4))[0]
        meta_data = bytearray(f.read(meta_len))
        for i in range(len(meta_data)):
            meta_data[i] ^= 0x63

        meta_data = base64.b64decode(meta_data[22:])
        meta_data = AES.new(core_key, AES.MODE_ECB).decrypt(meta_data)
        meta_json = json.loads(meta_data[6:].rstrip(b'\x00'))

        f.read(9)

        audio_data = bytearray(f.read())
        for i in range(len(audio_data)):
            audio_data[i] ^= key_box[(i + 1) & 0xff]

    ext = meta_json.get("format", "mp3")
    out_file = f"{output_name}.{ext}"

    with open(out_file, 'wb') as out:
        out.write(audio_data)

    print(f"转换完成：{out_file}")

if __name__ == "__main__":
    ncm_to_audio("test.ncm", "test")
