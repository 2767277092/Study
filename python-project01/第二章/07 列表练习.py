list1=[]
#
# for i in range(1,21)
#     i*=i
#     list1.append(i)


list1=[i**2 for i in range(1,21)]
print(list1)
print(list1)
list2=[]
for num in list1:
    if num%2==0:
        list2.append(num)
list3=[]
for num in list2:
    num*=num
    list3.append(num)
print(list3)
