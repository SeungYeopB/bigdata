# 라이브러리 불러오기
import seaborn as sns
# titanic 데이터셋 가져오기
df = sns.load_dataset('titanic')
# deck 열의 NaN 개수 계산하기
nan_deck = df['deck'].value_counts(dropna=False)
print(nan_deck)
nan_deck1 = df['deck'].value_counts()
print(nan_deck1)
# isnull() 메서드로 누락 데이터 찾기
print(df.head().isnull())  # head나 tail은 기본이 5건
# notnull() 메서드로 누락 데이터 찾기
print(df.head().notnull())
# isnull() 메서드로 누락 데이터 개수 구하기
print(df.head().isnull().sum(axis=0))
print(df.isnull().sum(axis=0))

print(df.head().isnull().sum(axis=1))
print(df.isnull().sum(axis=1))

import seaborn as sns
# titanic 데이터셋 가져오기
df = sns.load_dataset('titanic')
# for 반복문으로 각 열의 NaN 개수 계산하기
missing_df = df.isnull()
print(missing_df.columns)
for col in missing_df.columns:
    print(col)
    missing_count = missing_df[col].value_counts() # 각 열의 NaN 개수 파악
    try:
        print(col, ': ', missing_count[True]) # NaN 값이 있으면 개수를 출력
    except:
        print(col, ': ', 0) # NaN 값이 없으면 0개 출력
 # NaN 값이 500개 이상인 열을 모두 삭제 - deck 열(891개 중 688개의 NaN 값)
df_thresh = df.dropna(axis=1, thresh=500)
print(df_thresh.columns)

import seaborn as sns
# titanic 데이터셋 가져오기
df = sns.load_dataset('titanic')
# embark_town 열의 829행의 NaN 데이터 출력
print(df['embark_town'][825:830])
print('\n')

import pandas as pd

df = pd.DataFrame({'c1':['a', 'a', 'b', 'a', 'b'],
 'c2':[1, 1, 1, 2, 2],
 'c3':[1, 1, 2, 2, 2]})
print(df)
print('\n')
# 데이터프레임 전체 행 데이터 중에서 중복값 찾기
df_dup = df.duplicated()
print(df_dup)
print('\n')
# 데이터프레임의 특정 열 데이터에서 중복값 찾기
col_dup = df['c2'].duplicated()
print(col_dup)
col_dup = df['c1'].duplicated()
print(col_dup)


df = pd.DataFrame({'c1':['a', 'a', 'b', 'a', 'b'],
 'c2':[1, 1, 1, 2, 2],
 'c3':[1, 1, 2, 2, 2]})
print(df)
print('\n')
# 데이터프레임에서 중복 행을 제거
df2 = df.drop_duplicates()
print(df2)
print('\n')
# c2, c3열을 기준으로 중복 행을 제거
df3 = df.drop_duplicates(subset=['c2', 'c3'])
print(df3)

import pandas as pd
# read_csv() 함수로 df 생성
df = pd.read_csv('./auto-mpg.csv', header=None)

# 열 이름을 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
        'acceleration','model year','origin','name']
print(df.head())
print(df.head(3))
print('\n')

# mpg(mile per gallon)를 kpl(kilometer per liter)로 변환 (mpg_to_kpl = 0.425)
mpg_to_kpl = 1.60934 / 3.78541
# mpg 열에 0.425를 곱한 결과를 새로운 열(kpl)에 추가
df['kpl'] = df['mpg'] * mpg_to_kpl
print(df.head(3))
print('\n')
# kpl 열을 소수점 아래 둘째 자리에서 반올림
df['kpl'] = df['kpl'].round(2)
print(df.head(3))