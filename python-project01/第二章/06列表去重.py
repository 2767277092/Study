# num_list1=[19,23,54,64,875,20,109,232,123,54]
# num_list2=[55,80,72,35,60,123,54,29,91]
# num_sum=[]
# for i in range (len(num_list1)):
#     num_sum.append(num_list1[i])
# for i in range (len(num_list2)):
#     num_sum.append(num_list2[i])
# num_sum.sort()
# for i in range(len(num_sum)-1, 0, -1):
#     if num_sum[i] == num_sum[i-1]:
#         del num_sum[i]
#         del num_sum[i-1]
#
# print(num_sum)

# num_list1=[19,23,54,64,875,20,109,232,123,54]
# num_list2=[55,80,72,35,60,123,54,29,91]
# for num in num_list2:
#     num_list1.append(num)
#
# print(num_list1)
# num_sum=[]
# for num in num_list1:
#     if num not in num_sum:
#         num_sum.append(num)
# print(num_sum)


num_list1=[19,23,54,64,875,20,109,232,123,54]
num_list2=[55,80,72,35,60,123,54,29,91]
num_list3=num_list1+num_list2

print(num_list1)
num_sum=[]
for num in num_list3:
    if num not in num_sum:
        num_sum.append(num)
print(num_sum)



