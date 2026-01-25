# t3=tuple(100)
# print(t3)
# print(type(t3))
# a=10
# b=20
# t1=a,b
# print(a)
# print(b)
# b,a=t1
# print(a)
# print(b)
#

students = (
    ("S001", "王林", 85, 92, 78),
    ("S002", "李慕婉", 92, 88, 95),
    ("S003", "十三", 78, 85, 82),
    ("S004", "曾牛", 88, 79, 91),
    ("S005", "周轶", 95, 96, 89),
    ("S006", "王卓", 76, 82, 77),
    ("S007", "红蝶", 89, 91, 94),
    ("S008", "徐立国", 75, 69, 82),
    ("S009", "许木", 86, 89, 98),
    ("S010", "遁天", 66, 59, 72)
)

print("学号 \t姓名 \t语文 \t数学 \t英语 \t总分 \t平均分")
for s in students:
    total=s[2]+s[3]+s[4]
    avg=total/3
    print(f"{s[0]}\t {s[1]}\t {s[2]}\t\t {s[3]}\t\t {s[4]}\t\t {total}\t {avg:.1f} ")

chinese_score=[s[2] for s in students]
math_score=[s[3] for s in students]
english_score=[s[4] for s in students]

print(f"语文最低分:{min(chinese_score)},语文最高分:{max(chinese_score)},平均分:{sum(chinese_score)/len(chinese_score)}")

for s in students:
    total=s[2]+s[3]+s[4]
    avg=total/3
    if avg>90:
        print(f"学号{s[0]},姓名{s[1]},平均分{s[2]}")