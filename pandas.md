pandas

#### series

**Series** 通常特指 **pandas 库** 提供的一种**一维带标签数组**

```
import pandas as pd
data=[1,2,3]
series=pd.Series(data,index=['a'','b','c'])
//print(series.loc['a'])
print(series.iloc[1])
```

series.loc[]  按照index(即label)寻找key                  series.iloc[] 按照序号 (0,1,2...)寻找Key

*index的数量和data数量要匹配*



```
print(series[series>200])   *输出大于200的
```

####  *data frame*

df.shape          # (行数, 列数) df.columns        # 列索引
df.index          # 行索引   df.dtypes         # 每列的数据类型
df.values         # 返回底层 NumPy 数组

```
import pandas as pd
data={"Name":["Sam","Bob","John"],"Age":[20,21,22]}
df=pd.DataFrame(data,index=["employee1","employee2","employee3"])
print(df.loc["employee2"])
#加入新列 coloumn
df["job"]=["cook","N/A","cashier"]
#加入新行Row
new_row=pd.DataFrame([{"Name":"Sandy","Age":28,"job":"engineer"}]**,index=["employee4"])
df=pd.concat([df,new_row])     //append淘汰了  concat   新的一行默认索引为0(无index)

print(df) 
```









