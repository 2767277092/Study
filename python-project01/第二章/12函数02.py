#需求3:完成如下列表的排序操作,按照每一个元素的字符个数从小到大排序
data_list=["C++","C","Python","Java","PHP","JAVA"]
# for j in (0,len(data_list)-1):
#     for i in range(1,len(data_list)):
#         if len(data_list[i])<=len(data_list[i-1]):
#             pop=data_list[i-1]
#             data_list[i-1]=data_list[i]
#             data_list[i]=pop

data_list.sort(key=lambda item: len(item))
print(data_list)


#list.sort是默认按照编码排序