num_list = []
for i in range(1,11):
    num=int(input())
    num_list.append(num)
num_list.sort()
print(sum(num_list)/len(num_list))
num_list.sort(reverse=True)
num_reverse=sorted(num_list,reverse=True)
print(num_reverse)