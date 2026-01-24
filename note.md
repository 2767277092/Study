<P> 三引号 大量字符  可以自主换行

### 转义字符

<p>           \'        and   \"   and   \n     换行符 and  \t   缩进等于ta

### 字符串的转接

<p> 字符串之间可以直接写  或者+    

<p>字符串和其他类型得用+  ex.:  "字符串"+ a

### 字符串的格式化

<p>    ex.:         print("这是 %s" %s1)            print("这是 %s   ,%s " %(s1,s2)) 

<p>**第二种     print(f"这是 {s1}"  )               推荐 **  即{}  是变量/表达式

### 数据容器

#### 列表List   

切片        :       [s]=[ a,b,c,d,e,f,g]       

S[0:5:1]  =S[:5:]       即a b c d e  

 S[0:5:2]       即第a c e       不包含结束索引的元素

切片仍是List类型



if  num in/  not in  list:  判断元素是否存在于列表   返回True  或False   (去循环)



解包: 将列表解开为独立的元素

组包:将多个值 合并到一个容器

 list1=[list2,*list3]    *****



列表推导式:  list1=[i**2 for i in range(1,21)]

####   字符串Str   

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

####         元组tuple      集合set           字典dirt





