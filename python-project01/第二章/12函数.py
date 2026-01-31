#根据传入的低和计算三角形的面积
def cal_triangle(l,h):
    s=l*h/2
    return s
#计算传入字符中原因字母的个数 (元音字母aeiou AEIOU)
def cal_letter(str_letter):
    str_letter1=str_letter.lower()
    return str_letter1.count('a')+str_letter1.count('e')+str_letter1.count('i')+str_letter1.count('o')+str_letter1.count('u')

    # num=0
    # for w in str_letter:
    #     if w in 'aeiou':
    #         num+=1
#计算传入的班级学员成绩列表中成绩的最高分最低分平均分(保留一位小数)并返回
def cal_points(list_point):
    max_point=max(list_point)
    min_point=min(list_point)
    avg_point=round(sum(list_point)/len(list_point),1)
    return max_point,min_point,avg_point
print("""
#########请选择要进行的操作##########
         1.计算三角形的面积
         2.计算传入字符元音字母数3
         3.计算分数
""")
while True:
    choice = input("请选择你要进行的操作:(1-3)")
    match choice:
        case "1":
                l=input("请输入三角形的底")
                h=input("请输入三角形的高")
                s=cal_triangle(l,h)
                print(f"三角形的面积为{s}")
        case "2":
            str_letter=str(input("请输入字符串"))
            num=cal_letter(str_letter)
            print(f"所传入字符串的元音字母个数为{num}")
        case "3":
            list_points=list(input("请输入分数"))
            max_point,min_point,avg_point=cal_points(list_points)
            print(f"学员中的最高分为{max_point}")
            print(f"学员中的最低分为{min_point}")
            print(f"学员中的平均分为{avg_point}")
        case _ :
            print("违规操作")
            break




