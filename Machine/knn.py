## 작업 내용 :
# machine project에 knn.py 생성

### 기본 라이브러리 불러오기
import pandas as pd
import seaborn as sns

'''
[Step 1] 데이터 준비 - Seaborn에서 제공하는 titanic 데이터셋 가져오기
'''
# load_dataset 함수를 사용하여 데이터프레임으로 변환
data =  sns.load_dataset('titanic')
data
data.index
data.columns
data.info()
data.describe()
pd.set_option("display.max_columns", 15)  # 보이는 칼룸 수 늘리기
pd.set_option("display.max_rows", 100)
data
data.head()
# 데이터 살펴보기

#  IPython 디스플레이 설정 - 출력할 열의 개수 한도 늘리기

'''
[Step 2] 데이터 탐색
'''
# 데이터 자료형 확인
# Nan 값 처리
data.info()

# NaN값이 많은 deck 열을 삭제, embarked와 내용이 겹치는 embark_town 열을 삭제
Ndata = data.drop(["deck","embark_town"], axis=1)
Ndata.columns

# age 열에 나이 데이터가 없는 모든 행을 삭제 - age 열(891개 중 177개의 NaN 값)
Ndata = data.dropna(subset=["age"],how="any",axis=0)   ### non값들을 삭제하는것임 drop 에 na 까지
Ndata.info()
len(Ndata)
# embarked 열의 NaN값을 승선도시 중에서 가장 많이 출현한 값으로 치환하기
most = Ndata["embarked"].value_counts()
most
most = Ndata["embarked"].value_counts(dropna=True)
most
most = Ndata["embarked"].value_counts(dropna=False)
most## NaN 값까지 나온다
Ndata["embarked"].unique()
most = Ndata["embarked"].value_counts().idxmax()  ## 제일 큰값 출력쓰
most
most = Ndata["embarked"].value_counts(dropna=True).idxmax()
most
Ndata.describe()
Ndata.describe(include="all")
Ndata["embarked"].fillna(most, inplace=True)
most = Ndata["embarked"].value_counts()
most
'''
[Step 3] 분석에 사용할 속성을 선택
'''
# 분석에 활용할 열(속성)을 선택
# 'survived' - 생존여부 0: 사망, 1: 생존
# 'pclass' - 좌석 등급
# 'sex' - 성별
# 'age' - 나이
# 'sibsp' - 함께 탑승한 형재자매, 배우자수
# 'parch' - 함께 탑승한 부모. 아이의 수
# 'embarked' - 탑승항구, 승선도시
Adata = Ndata[['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'embarked']]
Adata.head()
# 원핫인코딩 - 범주형 데이터를 모형이 인식할 수 있도록 숫자형으로 변환
Adata.info()
Adata["sex"].unique()
Adata["embarked"].unique()
## Adata["sex"] --> 더미변수로 만들기 (숫자형으로 변환)  - one-not-encoding-처리
onhot_sex = pd.get_dummies(Adata["sex"])
onhot_sex
## 합치기
Adata = pd.concat([Adata, onhot_sex], axis=1)
Adata.head()
onhot_embarked = pd.get_dummies(Adata["embarked"], prefix="town")
onhot_embarked.head()
## 합치기
Adata = pd.concat([Adata, onhot_embarked], axis=1)
Adata.head()

'''
[step4] 데이터셋 구분 - 훈련용(train data) / 검증용(test data)
'''
## 속성(변수) 선택
  # 독립변수 X [["survived", "pclass", "sex", "age", "sibsp", "parch embarked", "female male",
#               "town_C",  "town_Q",  "town_S"]]
  # 종속변수 Y    y=ndf["survived"]
x = Adata[["survived", "age", "sibsp", "parch", "female", "male",\
           "town_C",  "town_Q",  "town_S"]]
x
y = Adata["survived"]
y
## 설명 변수 데이터를 정규화
from sklearn import preprocessing
x = preprocessing.StandardScaler().fit(x).transform(x)
x
## train data 와 test data를 구분(7:3 비율)
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.3, random_state=10)
print("train_data 수 : ", x_train.shape)
print("test_data 수 : ", x_test.shape)

from sklearn.neighbors import KNeighborsClassifier
##  모형 객체 생성 (k=5)
knn = KNeighborsClassifier(n_neighbors=5)
knn
# train data를 가지고 모형 학습
knn.fit(x_train, y_train)
## test data 가지고 y_hat을 예측(분류)
y_hat = knn.predict(x_test)
print(y_hat[0:10])
print(y_test.values[0:10])
## 모형 성능 평가 - confusion matric
from sklearn import metrics
knn_matrix = metrics.confusion_matrix(y_test, y_hat)
print(knn_matrix)
## 모형 성능 평가 - 평가지표 계산
knn_report = metrics.classification_report(y_test, y_hat)
print(knn_report)