import pandas
import pandas as pd
import numpy as np

df = pandas.read_excel("./02. sales-funnel.xlsx")
df.head()
df.index
df.columns
df.info()
df.describe()

pd.pivot_table(df,index=["Name"])
# index만 지정하고 다른 칼럼 지정 안하면 숫자형 칼럼만 남긴다.
# 키 = name , unique, 하나의 name으로 합쳐진다. value - 평균값을 가진다.
#df.pivot_table(df, index=["Name", "Rep", "Manager"], values=["Price"])
pd.pivot_table(df,index=["Name","Manager", "Rep"], values=["Price"])
pd.pivot_table(df,index=["Name"], values=["Price"])
pd.pivot_table(df,index=["Manager", "Rep"], values=["Price"],aggfunc=np.sum)
pd.pivot_table(df,index=["Manager", "Rep","Product"],
               values=["Price","Quantity"],
               aggfunc=[np.sum, np.mean])