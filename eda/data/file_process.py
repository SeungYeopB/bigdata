import pandas as pd

file_path = './data/read_csv_sample.csv'


df1 = pd.read_csv(file_path)
print(df1)
print("\n")

# read_csv() 함수로 데이터프레임 변환. 변수 df2에 저장. header=None 옵션
df2 = pd.read_csv(file_path, header=None)
print(df2)
print('\n')
# read_csv() 함수로 데이터프레임 변환. 변수 df3에 저장. index_col=None 옵션
df3 = pd.read_csv(file_path, index_col=None)
print(df3)
print('\n')
# read_csv() 함수로 데이터프레임 변환. 변수 df4에 저장. index_col='c0' 옵션
df4 = pd.read_csv(file_path, index_col='c0')
print(df4)

import pandas as pd
# read_excel() 함수로 데이터프레임 변환
df1 = pd.read_excel('./data/남북한발전전력량.xlsx') # header=0 (default 옵션)
df2 = pd.read_excel('./data/남북한발전전력량.xlsx', header=None) # header=None 옵션
# 데이터프레임 출력
print(df1)
print('\n')
print(df2)