import requests

URL = "http://finance.naver.com/"
response = requests.get(URL)
html_data = response.text
print(html_data)
import re
temp_data = html_data.split('<tr class="')
temp_data[0]
temp_data[1]
temp_data[2]
temp_data[3]
temp_data[4]
temp_data[5]
temp_data[6]
temp_data[7]
nujuk = []
for i in range(1,2):
    #for i in range(1, 8):
    if i == 7 :
        temp_data1 = temp_data[i].split("</span></a></li")
        body = re.search('<span class="txt">.*', temp_data1[0], re.I | re.S)
    else :
        body = re.search('event\);">.*', temp_data[i], re.I | re.S)  # *뒤에 내용 다 찾아라 뜻
    body = body.group()
    body = re.sub("<.+>","",body)   #태그  모두 제거
    temp_data2 = body.split("\n")
    jongmok = re.sub('event\);">', '', temp_data2[0].strip())
    nujuk.append(jongmok)

print(nujuk)

import pickle
pfile_w = open("./jongmok.pck", mode='wb')
pickle.dump(nujuk, pfile_w)
pfile_w.close()


pfile_r = open("./jongmok.pck", mode='rb')
nujuk_text_read = pickle.load(pfile_r)
print("길이 :",len(nujuk_text_read))
print("type :",type(nujuk_text_read))
print("내용 :",nujuk_text_read)
pfile_r.close()



# -*- coding: utf-8 -*-
import pandas as pd
# read_csv() 함수로 df 생성
df = pd.read_csv('./auto-mpg.csv', header=None)
df
# 열 이름을 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
 'acceleration','model year','origin','name']
# 데이터프레임 df의 내용을 일부 확인
print(df.head()) # 처음 5개의 행
print('\n')
print(df.tail()) # 마지막 5개의 행
# df의 모양과 크기 확인: (행의 개수, 열의 개수)를 투플로 반환
print(df.shape)
print('\n')
# 데이터프레임 df의 내용 확인
print(df.info())
print('\n')
# 데이터프레임 df의 자료형 확인
print(df.dtypes)
print('\n')
# 시리즈(mog 열)의 자료형 확인
print(df.mpg.dtypes)
print('\n')
# 데이터프레임 df의 기술통계 정보 확인
print(df.describe())
print('\n')
print(df.describe(include='all'))

import pandas as pd# read_csv() 함수로 df 생성
df = pd.read_csv('./auto-mpg.csv', header=None)
# 열 이름을 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
 'acceleration','model year','origin','name']
# 데이터프레임 df의 각 열이 가지고 있는 원소 개수 확인
print(df.count())
print('\n')
# df.count()가 반환하는 객체 타입 출력
print(type(df.count()))
print('\n')
# 데이터프레임 df의 특정 열이 가지고 있는 고유값 확인
unique_values = df['origin'].value_counts()
print(unique_values)
print('\n')
# value_counts 메소드가 반환하는 객체 타입 출력
print(type(unique_values))


import pandas as pd
# read_csv() 함수로 df 생성
df = pd.read_csv('./auto-mpg.csv', header=None)
# 열 이름을 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
 'acceleration','model year','origin','name']
# 평균값
print(df.mean())
print('\n')
print(df['mpg'].mean())
print(df.mpg.mean())
print('\n')
print(df[['mpg','weight']].mean())
# 중간값
print(df.median())
print('\n')
print(df['mpg'].median())
# 최대값
print(df.max())
print('\n')
print(df['mpg'].max())
# 최소값
print(df.min())
print('\n')
print(df['mpg'].min())
# 표준편차
print(df.std())
print('\n')
print(df['mpg'].std())
# 상관계수
print(df.corr())
print('\n')
print(df[['mpg','weight']].corr())


import seaborn as sns
# titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','fare']]
df['ten'] = 10
print(df.head())
print('\n')
# 사용자 함수 정의
def add_10(n):  # 10을 더하는 함수
    return n + 10
def add_two_obj(a, b):  # 두 객체의 합
    return a + b

print(add_10(10))
print(add_two_obj(10, 10))
print('\n')
# 시리즈 객체에 적용
sr1 = df['age'].apply(add_10) # n = df['age']의 모든 원소
print(sr1.head())
print('\n') # 시리즈 객체와 숫자에 적용 : 2개의 인수(시리즈 + 숫자)
sr2 = df['age'].apply(add_two_obj, b=10)  # a=df['age']의 모든 원소, b=10
print(sr2.head())
print('\n')
# 람다 함수 활용: 시리즈 객체에 적용
sr3 = df['age'].apply(lambda x: add_10(x)) # x=df['age']
print(sr3.head())

import seaborn as sns
# titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','fare']]
print(df.head())
print('\n')
# 사용자 함수 정의
def add_10(n): # 10을 더하는 함수
    return n + 10
 # 데이터프레임에 applymap()으로 add_10() 함수를 매핑 적용
df_map = df.applymap(add_10)
print(df_map.head())

import seaborn as sns
# titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','fare']]
print(df.head())
print('\n')
df.describe(include="all")
df.describe()
df2.describe(include="all")
df2.describe()
# 사용자 함수 정의
def missing_value(series): # 시리즈를 인수로 전달
    return series.isnull() # 불린 시리즈를 반환
 # 데이터프레임의 각 열을 인수로 전달하면 데이터프레임을 반환
result = df.apply(missing_value, axis=0)
print(result.head())
print('\n')
print(type(result))

import seaborn as sns
# titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','fare']]
print(df.head())
print('\n')
# 사용자 함수 정의
def min_max(x): # 최대값 - 최소값
    return x.max() - x.min() # 데이터프레임의 각 열을 인수로 전달하면 시리즈를 반환
result = df.apply(min_max) #기본값 axis=0
print(result)
print('\n')
print(type(result))

print(df.age.max())
print(df.age.min())
print(df.age.max()-df.age.min())
print(df.fare.max())
print(df.fare.min())
print(df.fare.max()-df.fare.min())

# 라이브러리 불러오기
import seaborn as sns
# titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','fare']]
df['ten'] = 10
print(df.head())
print('\n')
# 사용자 함수 정의
def add_two_obj(a, b): # 두 객체의 합
    return a + b
 # 데이터프레임의 2개 열을 선택하여 적용
# x=df, a=df['age'], b=df['ten']
df['add'] = df.apply(lambda x: add_two_obj(x['age'], x['ten']), axis=1)
print(df.head())

import seaborn as sns
# titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','fare']]
print(df)
# 각 열의 NaN 찾기 - 데이터프레임 전달하면 데이터프레임을 반환
def missing_value(x):
    return x.isnull()
# 각 열의 NaN 개수 반환 - 데이터프레임 전달하면 시리즈 반환
def missing_count(x): #
    return missing_value(x).sum()# 데이터프레임의 총 NaN 개수 - 데이터프레임 전달하면 값을 반환
def totoal_number_missing(x):
    return missing_count(x).sum() # 데이터프레임에 pipe() 메소드로 함수 매핑
result_df = df.pipe(missing_value)
print(result_df.head())
print(type(result_df))
print('\n')
result_series = df.pipe(missing_count)
print(result_series)
print(type(result_series))
print('\n')
result_value = df.pipe(totoal_number_missing)
print(result_value)
print(type(result_value))

import seaborn as sns
# titanic 데이터셋의 부분을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[0:4,'survived':'age']
print(df, '\n')
# 열 이름의 리스트 만들기
columns = list(df.columns.values) #기존 열 이름
print(columns, '\n')
# 열 이름을 알파벳 순으로 정렬하기
columns_sorted = sorted(columns) #알파벳 순으로 정렬
df_sorted = df[columns_sorted]
print(df_sorted, '\n')
# 열 이름을 기존 순서의 정반대 역순으로 정렬하기
columns_reversed = list(reversed(columns))
df_reversed = df[columns_reversed]
print(df_reversed, '\n')# 열 이름을 사용자가 정의한 임의의 순서로 재배치하기
columns_customed = ['pclass', 'sex', 'age', 'survived']
df_customed = df[columns_customed]
print(df_customed)


import pandas as pd
# 데이터셋 가져오기
df = pd.read_excel('./주가데이터.xlsx')
print(df.head(), '\n')
print(df.dtypes, '\n')
# 연, 월, 일 데이터 분리하기
df['연월일'] = df['연월일'].astype('str') # 문자열 메소드 사용을 자료형 변경
dates = df['연월일'].str.split('-') # 문자열을 split() 메서드로 분리
print(type(dates))
dates.index
dates.values
print(dates.head(), '\n')
# 분리된 정보를 각각 새로운 열에 담아서 df에 추가하기
df['연'] = dates.str.get(0) # dates 변수의 원소 리스트의 0번째 인덱스 값
df['월'] = dates.str.get(1) # dates 변수의 원소 리스트의 1번째 인덱스 값
df['일'] = dates.str.get(2) # dates 변수의 원소 리스트의 2번째 인덱스 값
print(df.head())

import seaborn as sns
# titanic 데이터셋 로딩
titanic = sns.load_dataset('titanic')
# 나이가 10대(10~19세)인 승객만 따로 선택
mask1 = (titanic.age >= 10) & (titanic.age < 20)
df_teenage = titanic.loc[mask1, :]
print(df_teenage.head())
print('\n')# 나이가 10세 미만(0~9세)이고 여성인 승객만 따로 선택
mask2 = (titanic.age < 10) & (titanic.sex == 'female')
df_female_under10 = titanic.loc[mask2, :]
print(df_female_under10.head())
print('\n')
# 나이가 10세 미만(0~9세) 또는 60세 이상인 승객의 age, sex, alone 열만 선택
mask3 = (titanic.age < 10) | (titanic.age >= 60)
df_under10_morethan60 = titanic.loc[mask3, ['age', 'sex', 'alone']]
print(df_under10_morethan60.head())

import seaborn as sns
import pandas as pd
# titanic 데이터셋 로딩
titanic = sns.load_dataset('titanic')
# IPyhton 디스플레이 설정 변경 - 출력할 최대 열의 개수
pd.set_option('display.max_columns', 10)
print(pd.set_option)
print(type(pd.set_option))

 # 함께 탑승한 형제 또는 배우자의 수가 3, 4, 5인 승객만 따로 추출 - 불린 인덱싱
mask3 = titanic['sibsp'] == 3
mask4 = titanic['sibsp'] == 4
mask5 = titanic['sibsp'] == 5
df_boolean = titanic[mask3 | mask4 | mask5]
print(df_boolean.head())
print('\n')
# isin() 메서드 활용하여 동일한 조건으로 추출
isin_filter = titanic['sibsp'].isin([3, 4, 5])
df_isin = titanic[isin_filter]
print(df_isin.head())


import pandas as pd# 데이터프레임 만들기
df1 = pd.DataFrame({'a': ['a0', 'a1', 'a2', 'a3'],
                'b': ['b0', 'b1', 'b2', 'b3'],
                'c': ['c0', 'c1', 'c2', 'c3']},
                index=[0, 1, 2, 3])
df2 = pd.DataFrame({'a': ['a2', 'a3', 'a4', 'a5'],
                'b': ['b2', 'b3', 'b4', 'b5'],
                'c': ['c2', 'c3', 'c4', 'c5'],
                'd': ['d2', 'd3', 'd4', 'd5']},
                index=[2, 3, 4, 5])
print(df1, '\n')
print(df2, '\n')
# 2개의 데이터프레임을 위 아래 행 방향으로 이어 붙이듯 연결하기
result1 = pd.concat([df1, df2])
print(result1, '\n')
# ignore_index=True 옵션 설정하기
result2 = pd.concat([df1, df2], ignore_index=True)
print(result2, '\n')
# 2개의 데이터프레임을 좌우 열 방향으로 이어 붙이듯 연결하기
result3 = pd.concat([df1, df2], axis=1)
print(result3, '\n')
# join='inner' 옵션 적용하기(교집합)
result3_in = pd.concat([df1, df2], axis=1, join='inner')
print(result3_in, '\n')

sr1 = pd.Series(['e0', 'e1', 'e2', 'e3'], name='e')
sr2 = pd.Series(['f0', 'f1', 'f2'], name='f', index=[3, 4, 5])
sr3 = pd.Series(['g0', 'g1', 'g2', 'g3'], name='g')
# df1과 sr1을 좌우 열 방향으로 연결하기
result4 = pd.concat([df1, sr1], axis=1)
print(result4, '\n')

result5 = pd.concat([df2, sr2], axis=1, sort=True)
print(result5, '\n')
# sr1과 sr3을 좌우 열 방향으로 연결하기
result6 = pd.concat([sr1, sr3], axis=1)
print(result6, '\n')
result7 = pd.concat([sr1, sr3], axis=0)
print(result7, '\n')

import pandas as pd
# IPyhton 디스플레이 설정 변경
pd.set_option('display.max_columns', 10) # 출력할 최대 열의 개수
pd.set_option('display.max_colwidth', 20) # 출력할 열의 너비
pd.set_option('display.unicode.east_asian_width', True) # 유니코드 사용 너비 조정
# 주식 데이터를 가져와서 데이터프레임 만들기
df1 = pd.read_excel('./stock price.xlsx')
df2 = pd.read_excel('./stock valuation.xlsx')
print(df1)
print('\n')
print(df2)
print('\n')
# 데이터프레임 합치기 - 교집합
merge_inner = pd.merge(df1, df2)
print(merge_inner)
print('\n')
# 데이터프레임 합치기 - 합집합
merge_outer = pd.merge(df1, df2, how='outer', on='id')
print(merge_outer)
print('\n')
# 데이터프레임 합치기 - 왼쪽 데이터프레임 기준, 키 값 분리
merge_left = pd.merge(df1, df2, how='left', left_on='stock_name', right_on='name')print(merge_left)
print('\n')
# 데이터프레임 합치기 - 오른쪽 데이터프레임 기준, 키 값 분리
merge_right = pd.merge(df1, df2, how='right', left_on='stock_name', right_on='name')
print(merge_right)
print('\n')
# 불린 인덱싱과 결합하여 원하는 데이터 찾기
price = df1[df1['price'] < 50000]
print(price.head())
print('\n')
value = pd.merge(price, df2)
print(value)


import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','sex', 'class', 'fare', 'survived']]
print('승객 수:', len(df))
print(df.head())
print('\n')
# class 열을 기준으로 분할
grouped = df.groupby(['class'])
print(grouped)
print('\n')
# 그룹 객체를 iteration으로 출력: head() 메소드로 첫 5행만을 출력
for key, group in grouped:
    print('* key :', key)
    print('* number :', len(group))
    print(group.head())
    print('\n') # 연산 메소드 적용
average = grouped.mean()
print(average)
print('\n')
# 개별 그룹 선택하기
group3 = grouped.get_group('Third')
print(group3.head())
print('\n')
# class 열, sex 열을 기준으로 분할
grouped_two = df.groupby(['class', 'sex'])
# grouped_two 그룹 객체를 iteration으로 출력
for key, group in grouped_two:
    print('* key :', key)
    print('* number :', len(group))
    print(group.head())
    print('\n') # grouped_two 그룹 객체에 연산 메소드 적용
average_two = grouped_two.mean()
print(average_two)
print('\n')
print(type(average_two))
# grouped_two 그룹 객체에서 개별 그룹 선택하기
group3f = grouped_two.get_group(('Third','female'))
print(group3f.head())


import pandas as pd
import seaborn as sns
# titanic 데이터셋에서 age, sex 등 5개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','sex', 'class', 'fare', 'survived']]
# class 열을 기준으로 분할
grouped = df.groupby(['class'])
# 각 그룹에 대한 모든 열의 표준편차를 집계하여 데이터프레임으로 반환
std_all = grouped.std()
print(std_all)
print('\n')
print(type(std_all))
print('\n')
# 각 그룹에 대한 fare 열의 표준편차를 집계하여 시리즈로 반환
std_fare = grouped.fare.std()
print(std_fare)
print('\n')
print(type(std_fare))
print('\n')
# 그룹 객체에 agg() 메소드 적용 - 사용자 정의 함수를 인수로 전달
def min_max(x): # 최대값 - 최소값
    return x.max() - x.min() # 각 그룹의 최대값과 최소값의 차이를 계산하여 그룹별로 집계
agg_minmax = grouped.agg(min_max)
print(agg_minmax.head())
print('\n')
# 여러 함수를 각 열에 동일하게 적용하여 집계
agg_all = grouped.agg(['min', 'max'])
print(agg_all.head())
print('\n')
# 각 열마다 다른 함수를 적용하여 집계
agg_sep = grouped.agg({'fare':['min', 'max'], 'age':'mean'})
print(agg_sep.head())


import pandas as pd
import seaborn as sns
# titanic 데이터셋에서 age, sex 등 5개 열을 선택하여 데이터프레임 만들기
titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age','sex', 'class', 'fare', 'survived']]
# class 열을 기준으로 분할
grouped = df.groupby(['class'])
# 집계 : 각 그룹별 요약 통계정보를 집계
agg_grouped = grouped.apply(lambda x: x.describe())
print(agg_grouped)
print('\n')
# z-score를 계산하는 사용자 함수 정의
def z_score(x):
 return (x - x.mean()) / x.std()
age_zscore = grouped.age.apply(z_score) #기본값 axis=0
print(age_zscore.head())
print('\n')
# 필터링 : age 열의 데이터 평균이 30보다 작은 그룹만을 필터링하여 출력
age_filter = grouped.apply(lambda x: x.age.mean() < 30)
print(age_filter)
print('\n')
for x in age_filter.index:
 if age_filter[x]==True:
 age_filter_df = grouped.get_group(x)
 print(age_filter_df.head())
 print('\n'
