import pandas as pd
import re, os
os.getcwd()
df = pd.read_csv('apt.csv', encoding="CP949")
print(df)
len(df)
df.head()
df.tail()
df.info()
df.describe()

df.지역
df.면적
df.면적 > 130
df[df.면적 > 130]
df.head(10).면적
df[df.가격 < 15000]
df.아파트[(df.면적 > 130) & (df.가격 < 15000)]
df.loc[:,["아파트","가격"]]
df.아파트[df.가격 > 40000]
df.loc[:,["아파트","가격"]][df.가격 >= 40000]

df['단가'] = df.가격 / df.면적
df.loc[:10,("가격","면적","단가")]

import pandas

data = pandas.read_csv("apt2.csv")
print(data)


import pandas as pd
import re, os
os.getcwd()
# 읽어 오기
df = pd.read_csv('apt.csv',encoding='cp949')
print(df)

# 자료 수
len(df)
# 자료 파악하기
df.head()
df.tail()
df.info()
df.describe()
# 특정열
df.지역
# 조건 출력
# 면적 130평 이상 출력
df.면적 > 130

df.면적

df[df.면적 > 130]

df.head(10).면적

df[df.가격 < 15000]

df[(df.면적 > 130) & (df.가격 < 15000)]
df.가격[(df.면적 > 130) & (df.가격 < 15000)]
df.면적[(df.면적 > 130) & (df.가격 < 15000)]
df.아파트[(df.면적 > 130) & (df.가격 < 15000)]

# 4억 이상 가격으로 거래된 아파트
df.loc[:,['아파트','가격']]

df.아파트[df.가격 >= 40000]

df.loc[:,['아파트','가격']][df.가격 >= 40000]
print(type(df.loc[:,['아파트','가격']]))
# 가격,면적 ,단가 10개 출력
# 단가 없음, 단가 생성
df['단가'] = df.가격 / df.면적
df.loc[:10,('가격','면적','단가')]

# 25억 아파트 출력하기  - 아파트명으로 sort, 출력내용 -'아파트','가격','면적','단가'
df.가격 > 250000
df[df.가격 > 250000]
print(df[df.가격 > 250000].sort_values(by = '아파트').loc[:,('아파트','가격','면적','단가')])

# 강릉 아파트만 출력
df
df.지역.str.find('강릉')   # 값이  -1 이면  not found
df[df.지역.str.find('강릉') > -1]

# 강릉 아파트만 출력 하려 각 변수 평균 출력 (mean())
df_gang = df[df.지역.str.find('강릉') > -1]
print(df_gang.mean())