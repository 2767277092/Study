

### 快捷键

alt+shift    选中不同行

shift+tab删除缩进



### 运算符

#### match

- match   choice:

		case "1":

		case  _:  #其他情况(直接  下划线不要别的)

#### if in

  

```
if  value in list/dict:
```



#### while true+break

无限循环+主动终止 

break仅终止所在那一层 若为嵌套不影响外层循环

####      round  

round(value,1)      用来限制小数位数  

#### global 

```
global  num1
num1=100
:声明函数内的该变量为全局变量    !先声明 在使用
```



###   字符串

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

操作:

append()      列表尾部增加元素s.append(10086)

inset()       在指定索引之前插入该元素  s.insert(0,10086)

remover   移除列表中匹配到的第一个值  s.remove(10086)

pop()      删除列表中指定索引位置的元素(若未指定索 默认删除最后一个)  s.pop(2/空)

reverse()       反转列表元素  s.reverse()

sort()  对列表进行排序 (列表元素的数据类型一致才可以进行排序)   s.sort()

sort











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

### 定义函数 

```
def 函数名(参数列表):
	函数
	return 返回值
```

### 返回多个值

return a,b,c          会输出一个元组  (a,b,c)   

相应的 可以利用解包操作 获取多个输出值    

### 函数的说明文档

```
def function()
	"""
	此处进行说明
	"""
	return 
    
    
 help(function)  查看说明文档 注意function后面!不要括号!
```

### 嵌套调用

 函数的调用遵循栈规则   后进先出

```
def function_a()
	print("a_before")
	function_b()
	print("a_after")
def function_b()
	print("b_before")
	function_c()
	print("b_after)
def function_c()
	print("c")
顺序:a_before	->b_befor->c->b_after->a_after	
```

### 函数的传参方式

位置传参(顺序一致)

 关键字参数                **若位置参数与关键字参数混用 关键字参数必须在后面**

```
def reg_stu(name, age, gender, city):
    print(f"注册成功,姓名:{name}, 年龄:{age}, 性别:{gender}, 城市:{city}")
    return {"name": name, "age": age, "gender": gender, "city": city}

# 调用函数
stu = reg_stu(name="张三", age=18, gender="男", city="北京")
print(stu)

stu2 = reg_stu(gender="男", name="王武", city="上海", age=22)
print(stu2)

stu2 = reg_stu("赵四", 28, gender="男", city="上海")
print(stu2)
```



###  不定长参数

用于参数个数不确定的场景  类型分为:**位置传递**和**关键字传递**

```
#基于位置传递的不定长参数
def calc_data(*args):
	min_data=min(args)
	max_data=max(args)
	avg_data=sum(args)/len(args)
	

data=function(10,20,30,40,50)
#传递的所有匹配的位置参数都会被args变量收集 合并封装为一个元组
#args为元组类型 (注意并不会封装关键字参数) 
```

```
#基于关键字的不定长参数 
def calc_data(*args.**kwrgs): #封装到字典
	min_data=min(args)
	max_data=max(args)
	avg_data=sum(args)/len(args)
	
	if kwrgs.get("round") is not None:
		avg_data=round(avg_data,kwargs.get("round"))
	if kwrgs.get("print"):
		print(f"计算出的最小值为{min_data},最大值为{max_data},平均值为{avg_data})


#调用函数
print(calc_data(2,7,9,10,round=3,print=True))
	
	
	
	
```

不定长位置参数(*args) 用于处理数量不确定的数据

不定长关键字参数(**kwargs)用于处理数量不确定的选项  (函数的配置参数.用来定制函数的行为)





```
def add(x,y):
	return x+y
def subtract (x,y):
	return x-y
def calc(x,y,oper):
	return oper(x,y)
result=calc(10,20,add) #add传递的是函数中 封装的逻辑
print(result)
```



### 匿名函数

Def:  没有名称的函数,需要通过lambda来声明函数,可以简化函数的编写(单行表达式)

```
#定义匿名函数
lambda 参数列表 :函数体   #不能换行

out_line=lambda :print("---")  #匿名函数得赋给一个变量
add=lambda x,y:x+y             #自动返回表达式的结果(无需return)
out_line()
print(add(100,200))

```

函数逻辑间的的单行表达式且只在一个地方使用,可以考虑匿名函数(通常作为高阶函数的参数使用)

### 类型注解

```
#普通定义变量
a=699
score=98
name=["a","b","c"]
phones={"123","1234"}


#类型注解
a:int=699
score:float=98
name:list[str]=["a","b","c"]
phones:set[str]={"123","1234"}

```















 
