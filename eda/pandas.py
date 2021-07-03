import pandas as pd

dict_data = {"a": 1, "b":2, "c":3}

sr = pd.Series(dict_data)
print(type(sr))
print(sr)

import pandas as pd
list_data = ["2031-06-02", 3.14, "ABC", 100, True]
sr = pd.Series(list_data)
print(sr)

idx = sr.index
val = sr.values
print(idx)

print(val)

import pandas as pd
tup_data = ("영인", "2010-05-01", "여", True)
sr = pd.Series(tup_data, index=["이름", "생년월일", "성별","학생여부"])
print(sr)

print(sr[0])
print(sr["이름"])
print(sr[[1,2]])
print(sr[1:2])
print(sr[["생년월일", "성별"]])

import pandas as pd
dict_data = {"c0":}

import pandas as pd

df = pd.DataFrame([[15,"남","청주중"],[17, "여", "꽃별중"]], index=["동학","현지"], columns=["나이", "성별", "학교"])
print(df)
print(df.index)
print(df.columns)
df.index=["학생","학생2"]
df.columns=["연령","남녀","소속"]

df = pd.DataFrame([[15,"남","청주중"],[17, "여", "꽃별중"]], index=["동학","현지"], columns=["나이", "성별", "학교"])
print(df)
df.rename(columns={"나이":"연령", "성별":"남녀", "학교":"소속"},inplace=True)
df.rename(index={"동학":"학생1", "현지":"학생2"},inplace=True)
print(df)

import pandas as pd
exam_data = {"수학":[90,80,70],"영어":[98,89,95],"인지":[85,95,100],"특할":[100,90,90]}
df = pd.DataFrame(exam_data, index=["형식","태오","유진"])
print(df)
df2 = df[:]
df2.drop("태오", inplace=True)
print(df2)
df3 = df[:]
df3.drob(["태오","유진"], axis=0, inplace=True)
print(df3)

import pandas as pd

exam_data = {"수학":[90,80,70],"영어":[98,89,95],"인지":[85,95,100],"특할":[100,90,90]}
df = pd.DataFrame(exam_data, index=["형식", "태오", "유진"])
print(df)

label1 = df.loc["형식"]
position1 = df.iloc[0]
print(label1)
print(position1)
label2=df.loc[["형식", "태오"]]
position2 = df.iloc[[0,1]]
print(label2)
print(position2)

label3 = df.loc["형식":"태오"]
position3 = df.iloc[0:1]
print(label3)
print(position3)

import pandas as pd
#DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장
exam_data = {'이름' : [ '형식', '태오', '유진'],
            '수학' : [ 90, 80, 70],
            '영어' : [ 98, 89, 95],
            '인지' : [ 85, 95, 100],
            '특활' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data)
print(df)
print(type(df))

math1 = df['수학']
print(math1)
print(type(math1))

english = df.영어
print(english)
print(type(english))

music_gym = df[['인지', '특활']]
print(music_gym)
print(type(music_gym))

math2 = df[['수학']]
print(math2)
print(type(math2))

import pandas as pd
# DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장
exam_data = {'이름' : [ '형식', '태오', '유진'],
             '수학' : [ 90, 80, 70],
             '영어' : [ 98, 89, 95],
             '인지' : [ 85, 95, 100],
             '특활' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data)
df.set_index("이름", inplace=True)
print(df)
print(df.index)
print(df.columns)

a = df.loc['형식', '인지']
print(a)
b = df.iloc[0, 2]
print(b)
c= df.loc[['태오','유진'], ['인지', '특활']]
print(c)
c= df.iloc[[1,2 ], [2,3]]
print(c)
c= df.iloc[1: , 2:]
print(c)

c = df.loc['형식', ['인지', '특활']]
print(c)
d = df.iloc[0, [2, 3]]
print(d)
e = df.loc['형식', '인지':'특활']
print(e)
f = df.iloc[0, 2:]
print(f)

g = df.loc[['형식', '태오'], ['인지', '특활']]
print(g)
h = df.iloc[[0, 1], [2, 3]]
print(h)
i = df.loc['형식':'태오', '인지':'특활']
print(i)
j = df.iloc[0:2, 2:]
print(j)

exam_data = {'이름' : [ '형식', '태오', '유진'],
         '수학' : [ 90, 80, 70],
         '영어' : [ 98, 89, 95],
         '인지' : [ 85, 95, 100],
         '특활' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data)
print(df)
df['독어'] = 80
print(df)

exam_data = {'이름' : ['형식', '태오', '유진'],
 '수학' : [ 90, 80, 70],
 '영어' : [ 98, 89, 95],
 '인지' : [ 85, 95, 100],
 '특활' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data)
print(df)
# 새로운 행(row)을 추가 - 같은 원소 값을 입력
df.loc[3] = 0
print(df)
print('\n')
df.loc[4] = ['동규', 90, 80, 70, 60]
print(df)
df.loc["행"] = df.loc[3]
print(df)

exam_data = {'이름' : [ '형식', '태오', '유진'],
 '수학' : [ 90, 80, 70],
 '영어' : [ 98, 89, 95],
 '인지' : [ 85, 95, 100],
 '특활' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data)
# '이름' 열을 새로운 인덱스로 지정하고, df 객체에 변경사항 반영
df.set_index('이름', inplace=True)
print(df)
print(df)# 데이터프레임 df의 특정 원소를 변경하는 방법: '형식'의'특활' 점수
df.iloc[0][3] = 80
print(df)
df.loc['형식']['특활'] = 90
print(df)
df.loc['형식', '특활'] = 100
print(df)

exam_data = {'이름' : [ '형식', '태오', '유진'],
 '수학' : [ 90, 80, 70],
 '영어' : [ 98, 89, 95],
 '인지' : [ 85, 95, 100], '특활' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data)
print(df)
# 데이터프레임 df를 전치하기 (메소드 활용)
df = df.transpose()
print(df)
df = df.T
print(df)

exam_data = {'이름' : [ '형식', '태오', '유진'],
            '수학' : [ 90, 80, 70],
            '영어' : [ 98, 89, 95],
            '인지' : [ 85, 95, 100],
            '특활' : [ 100, 90, 90]}
df = pd.DataFrame(exam_data)
print(df)
# 특정 열(column)을 데이터프레임의 행 인덱스(index)로 설정
ndf = df.set_index(['이름'])
print(ndf)
ndf2 = ndf.set_index("인지")
print(ndf2)
print(ndf2.index)

dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9],
'c3':[10,11,12], 'c4':[13,14,15]}# 딕셔서리를 데이터프레임으로 변환. 인덱스를 [r0, r1, r2]로 지정
df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
print(df)
# 인덱스를 [r0, r1, r2, r3, r4]로 재지정
new_index = ['r0', 'r1', 'r2', 'r3', 'r4']
ndf = df.reindex(new_index)
print(ndf)
new_index = ['r0', 'r1', 'r2', 'r3', 'r4']
ndf2 = df.reindex(new_index, fill_value=0)
print(ndf2)

data = {'name':['홍길동', '임꺽정', '장길산', '홍경래'],
        'kor':[90,80,70,70],
        'eng':[99,98,97,46],
        'mat':[90,70,70,60],
}
df = pd.DataFrame(data)
print(df)
df1 = df.set_index("name")
df1

print(df1.loc["홍길동", "mat"]
print(a)







print(df1.iloc[0:1,2:3])

print(df1.iloc[2: , 0:2])
print(df1.iloc[1,1] - 30)

import pandas as pd

dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9],
'c3':[10,11,12], 'c4':[13,14,15]}
print(dict_data)

df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
print(df)
ndf = df.reset_index()
print(ndf)

import pandas as pd

dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9],
'c3':[10,11,12], 'c4':[13,14,15]}
print(dict_data)

df = pd.DataFrame(dict_data, index=['r0', 'r1', 'r2'])
print(df)
ndf = df.sort_index(ascending=False)
print(ndf)
ndf = df.sort_index(ascending=True)
print(ndf)

import pandas as pd

student1 = pd.Series({"독어":100, "영어":80, "수학":90})
print(student1)
percentage = student1 / 200
percentage = student1 + 5000
print(percentage)
print(percentage)
print(type(percentage))

import pandas as pd

student1 = pd.Series({"독어":100,"영어":80, "수학":90})
student2 = pd.Series({"수학":80, "독어":90, "영어":80})
print(student1)
print(student2)
addition = student1 + student2
print(addition)
subtraction = student1 - student2
print(subtraction)
multiplication = student1 * student2
print(multiplication)
division = student1 / student2
print(type(division))


result = pd.DataFrame([addition, subtraction,
multiplication, division],
 index=['덧셈', '뺄셈', '곱셈', '나눗셈'])
print(result)


import pandas as pd
import numpy as np
# 딕셔너리 데이터로 판다스 시리즈 만들기
student1 = pd.Series({'독어':np.nan, '영어':80, '수학':90})
student2 = pd.Series({'수학':80, '독어':90})
print(student1)
print(student2)

sr_add = student1.add(student2, fill_value=0)
sr_sub = student1.sub(student2, fill_value=0)
sr_mul = student1.mul(student2, fill_value=0)
sr_div = student1.div(student2, fill_value=0)
print(sr_div)
result = pd.DataFrame([sr_add, sr_sub, sr_mul, sr_div],
                      index=['덧셈', '뺄셈', '곱셈', '나눗셈'])
print(result)

import pandas as pd
import seaborn as sns

titanic = sns.load_dataset("titanic")
df = titanic.loc[:,["age","fare"]]
print(df.head())
print(df.tail())
print(type(df))
addition = df + 10
print(addition.head())

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
# path = 파일 위치 정보 기술
# sep , delimeter = 텍스트데이터 필드 구분하는 문자
# header - 열이름으로 사용될 행의 번호
#        - none - header가 없고 첫행부터 데이터인 경우
# index_col : 행인덱스로 사용할 열의번호, 또는 열 이름
# names - 열 이름으로 사용할 열의 번호. 또는 열 이름
# skip_footer - 마지막 몇줄을 skip 할것인지 설정(숫자)
# encoding = 텍스트 인코딩 종류
print(df1)
print('\n')
print(df2)
df3 = pd.read_excel('./data/남북한발전전력량.xlsx', header=1)
print(df3)
df4 = pd.read_excel('./data/남북한발전전력량.xlsx', index_col=1)
print(df4)

import pandas as pd
# read_json() 함수로 데이터프레임 변환
df = pd.read_json('./data/read_json_sample.json')
print(df)
print('\n')
print(df.index)

import pandas as pd
# 판다스 DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장
data = {'name' : [ 'Jerry', 'Riah', 'Paul'],
 'algol' : [ "A", "A+", "B"],
 'basic' : [ "C", "B", "B+"],
 'c++' : [ "B+", "C", "C+"],
 }
df = pd.DataFrame(data)
df.set_index('name', inplace=True) #name 열을 인덱스로 지정
print(df)
df.to_csv("./data/df_sample.csv")

pay = [{"date": "3/1 ", "traffic": 2000, "coffee": 3000, "bab": 7000},
       {"date": "3/2 ", "traffic": 1500, "coffee": 4000, "bab": 8000},
       {"date": "3/3 ", "traffic": 2000, "coffee": 5000, "bab": 7000},
       {"date": "3/4 ", "traffic": 2500, "coffee": 5000, "bab": 9000},
       {"date": "3/5 ", "traffic": 4000, "coffee": 2000, "bab": 8000},
       {"date": "3/6 ", "traffic": 2500, "coffee": 3000, "bab": 7000},
       {"date": "3/7 ", "traffic": 3000, "coffee": 4000, "bab": 6000},
       {"date": "3/8 ", "traffic": 4000, "coffee": 5000, "bab": 4000},
       {"date": "3/9 ", "traffic": 5000, "coffee": 6000, "bab": 8000},
       {"date": "3/10", "traffic": 2000, "coffee": 4000, "bab": 3000}]

df = pd.DataFrame(pay)
print(df)
print(type(df))
df.to_csv("./data/expense.csv")
df1 = pd.read_csv("./data/expense.csv")
print(df1)



import pandas as pd
# 판다스 DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장
data = {'name' : [ 'Jerry', 'Riah', 'Paul'],
        'algol' : [ "A", "A+", "B"],
        'basic' : [ "C", "B", "B+"],
        'c++' : [ "B+", "C", "C+"],
 }
df = pd.DataFrame(data)
df.set_index('name', inplace=True) #name 열을 인덱스로 지정
print(df)
# to_csv() 메소드를 사용하여 CSV 파일로 내보내기. 파열명은 df_sample.csv로 저장
df.to_csv("./df_sample.csv")

import pandas as pd
# 판다스 DataFrame() 함수로 데이터프레임 변환. 변수 df에 저장
data = {'name' : [ 'Jerry', 'Riah', 'Paul'],
         'algol' : [ "A", "A+", "B"],
         'basic' : [ "C", "B", "B+"],
         'c++' : [ "B+", "C", "C+"],
        }
df = pd.DataFrame(data)
df.set_index('name', inplace=True) #name 열을 인덱스로 지정
print(df)
# to_excel() 메소드를 사용하여 엑셀 파일로 내보내기. 파열명은 df_sample.xlsx로 저장
df.to_excel("./df_sample.xlsx")



import pandas as pd
# 판다스 DataFrame() 함수로 데이터프레임 변환. 변수 df1, df2에 저장
data1 = {'name' : [ 'Jerry', 'Riah', 'Paul'],
 'algol' : [ "A", "A+", "B"],
 'basic' : [ "C", "B", "B+"],
 'c++' : [ "B+", "C", "C+"]}
data2 = {'c0':[1,2,3],
 'c1':[4,5,6],  'c2':[7,8,9],
 'c3':[10,11,12],
 'c4':[13,14,15]}
df1 = pd.DataFrame(data1)
df1.set_index('name', inplace=True) #name 열을 인덱스로 지정
print(df1)
print('\n')
df2 = pd.DataFrame(data2)
df2.set_index('c0', inplace=True) #c0 열을 인덱스로 지정
print(df2)
# df1을 'sheet1'으로, df2를 'sheet2'로 저장 (엑셀파일명은 "df_excelwriter.xlsx")
writer = pd.ExcelWriter("./df_excelwriter.xlsx")
df1.to_excel(writer, sheet_name="sheet1")
df2.to_excel(writer, sheet_name="sheet2")
writer.save()