# 利用count函数

# mail=input("")
# if mail.count("@")==1 and mail.count(".")>=1:
#     print("mail is legal")
# else:
#     print(f"{mail}mail is not legal")
# # 利用In函数
# mail=input("")
# if mail.count("@")==1 and "@" in mail:
#     print("mail is legal")
# else:
#     print(f"{mail}mail is not legal")



# 练习回文检测
# text=input("请输入文章")
# is_prime=True
# for i in range(0,len(text)//2):
#     if text[i]!=text[len(text)-1-i]:
#         is_prime=False
# if is_prime:
#     print("是回文")
# else:
#     print("不是")

# 将用户输入的10个字符串,反转后              全部转换为大写 然后记录在列表 最后将列表内容遍历输出
text=str(input("请输入十个字符串"))
# text_convert=text[::-1]    一步到位
text_convert=[]
for i in range(-1,-len(text)-1,-1):
    text_convert.append(text[i])
text_convert = "".join(text_convert)

print(text_convert)
text_convert=text_convert.upper()
text_list=[]
for i in range(0,len(text_convert)):
    text_list.append(text_convert[i])
print(text_list)
for i in range(0,len(text_convert)):
    print(text_convert[i])


