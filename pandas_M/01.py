import pandas as pd
data={"Name":["Sam","Bob","John"],"Age":[20,21,22]}
df=pd.DataFrame(data,index=["employee1","employee2","employee3"])
print(df.loc["employee2"])
#加入新列
df["job"]=["cook","N/A","cashier"]
#加入新行Row
new_row=pd.DataFrame([{"Name":"Sandy","Age":28,"job":"engineer"}],index=["employee4"])
df=pd.concat([df,new_row])
print(df)
 