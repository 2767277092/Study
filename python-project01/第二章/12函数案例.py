# def jiecheng (a):
#     if a==0:
#         return 1
#     else :
#         result=1
#         for i in range(1,a+1):
#
#             result=result*i
#         return result
# print(jiecheng(5))\

#递归调用注意终结点
def jc(a):
    if a!=0:
        return a*jc(a-1)
    else:
        return 1
print(jc(5))