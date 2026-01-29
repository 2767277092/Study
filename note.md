

### 快捷键

alt+shift    选中不同行

shift+tab删除缩进



### 运算符

#### match

- match   choice:

​	case "1":

​	case  _:  其他情况(直接  下划线不要别的)

#### if in

  if  value in list/dict:

#### while true+break

无限循环+主动终止 

break仅终止所在那一层 若为嵌套不影响外层循环

​       

 字符串

#### 字符

三引号 大量字符  可以自主换行



​         \'        and   \"   and   \n     换行符 and  \t   缩进等于ta

#### 字符串的转接

<p> 字符串之间可以直接写  或者+    

<p>字符串和其他类型得用+  ex.:  "字符串"+ a

#### 字符串的格式化

<p>    ex.:         print("这是 %s" %s1)            print("这是 %s   ,%s " %(s1,s2)) 

<p>**第二种     print(f"这是 {s1}"  )               推荐 **  即{}  是变量/表达式



for s in student:        (在student中遍历)

### 数据容器

#### 列表List

有序 可重复  可修改

切片        :       [s]=[ a,b,c,d,e,f,g]       

S[0:5:1]  =S[:5:]       即a b c d e  

 S[0:5:2]       即第a c e       不包含结束索引的元素

切片仍是List类型



if  num in/  not in  list:  判断元素是否存在于列表   返回True  或False   (去循环)



解包: 将列表解开为独立的元素

组包:将多个值 合并到一个容器

 list1=[list2,*list3]    *****



列表推导式:  list1=[i**2 for i in range(1,21)]

#### 字符串Str

特点: 不可修改  有序性 可迭代性   (可通过for循环迭代输出)

切片和列表一样 

字符串常见操作方法:

find()        s.find('python')从前往后查找子字符串  返回第一次出现的索引位置 找不到返回-1 

count()     s.count('h')  统计字串在字符串中出现的次数

upper        s.upper()       将字符串中的所有字母转为大写

lower          s.lower()      将字符串中的所有字母转为小写

split()         s.split('p')  将字符串咱找指定分隔符分割成列表

strip              s.strip()/s.strip('*')去除字符串两端的空白字符或指定字符

replace()       s.replace('h','c')  将字符串中的指定字串替换为新的子串

startswith()   s.startswith() 检查字符串是否以指定字串开头 返回布尔值

#### 元组tuple

有序 可重复 不可修改

定义元组: t3=() /t3=tuple()定义单元素元组时候 t3=(100,)   一定逗号

元组 不可更改  (等于不可修改的列表)

​        定义(组包)t1=1,2,3    t2=1,2,3,4

   基础解包t1=a,b,c         a=1,b=2,c=3          (可以用于交换)

​    拓展解包t2=a,*b,c       a=1 c=4 b=[2,3]         b是列表



count()   用于统计某元素出现的次数

index()  统计某元素的出现的索引位置(多个重复则 返回第一个)

#### 集合set

  #无序  不可重复 可修改  (不支持下标索引访问)

定义:     s1={"c","x"}       定义空集合 s2=set()       {}表示空字典

常见操作:

s1.add()          添加元素至集合      s1.remove()     移除集合中的指定元素 (指定元素不存在将报错)

e=s1.pop()                  随机删除集合中的元素并返回       s1.clear 清空集合

s1.difference(s2)  {s1-s2}    求取两集合的差集(在s1不在s2)    s1/union(s2)   {s1&s2}求并集

s1.intersection(s2)   {s1|s2}  求交集     





#### 字典dict

 定义:dict={"key":value}    空字典: dic1={}    dict2=dict()  

键值对     键不能重复 可修改  value任意类型  key为不可变类型(不可为List set dict)

常用操作:

访问   print(dict["key1"])        修改:dict["key"]=value1

增加 : dict1["key1"]=value1    

删除:   

score=dict1.pop("key1")  删除并返回Key对应的value      

del dict1("key1")仅删除 

修改:   dict['key1']=value2

查询:  根据Key获取value  dict["key1"]   /   dict1.get("key1")

获取所有的Key   dict1.keys()  获取所有的value  dict1.values()

获取所有的键值对 dict1.items   

#### 总结

![](E:\录像\屏幕截图 2026-01-29 201328.png)





## 函数

定义函数 def 函数名(参数列表):

​		    函数体

​		    return 返回值





 