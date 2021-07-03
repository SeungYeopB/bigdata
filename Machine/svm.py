### 기본 라이브러리 불러오기
import pandas as pd
import seaborn as sns

#[Step 1] 데이터 준비 - Seaborn에서 제공하는 titanic 데이터셋 가져오기
data = sns.load_dataset('titanic')
data

pd.set_option('display.max_columns', 15)
pd.set_option('display.max_rows', 1000)
data
print(data.head())

'''
[Step 2] 데이터 탐색
'''
data.info()
# 데이터 자료형 확인
# Nan 값 처리
# NaN값이 많은 deck 열을 삭제, embarked와 내용이 겹치는 embark_town 열을 삭제
Ndata = data.drop(['deck','embark_town'],axis=1)
Ndata.columns
# age 열에 나이 데이터가 없는 모든 행을 삭제 - age 열(891개 중 177개의 NaN 값)
Ndata = Ndata.dropna(subset=['age'],how='any',axis=0)
Ndata.info()
len(Ndata)
# embarked 열의 NaN값을 승선도시 중에서 가장 많이 출현한 값으로 치환하기
most = Ndata['embarked'].value_counts()
most
most = Ndata['embarked'].value_counts(dropna=True)
most
most = Ndata['embarked'].value_counts(dropna=False)
most
Ndata['embarked'].unique()
most = Ndata['embarked'].value_counts().idxmax()
most
most = Ndata['embarked'].value_counts(dropna=True).idxmax()
most
Ndata.describe()
Ndata.describe(include='all')
Ndata['embarked'].fillna(most,inplace=True)
Ndata["embarked"].fillna(most, inplace=True)
most = Ndata['embarked'].value_counts()
most

'''
[Step 3] 분석에 사용할 속성을 선택
'''
# 분석에 활용할 열(속성)을 선택 -
# 'survived' - 생존 여부 0: 사망, 1: 생존
# 'pclass' - 좌석 등급
# 'sex' - 성별
# 'age' - 나이
# 'sibsp' - 함께 탑승한 형재자매 , 배우자수
# 'parch' - 함께 탑승한 부모,아이의 수
# 'embarked' - 탑승항구,승선도시
Adata = Ndata[['survived', 'pclass', 'sex', 'age', 'sibsp', 'parch', 'embarked']]
Adata.head()
# 원핫인코딩 - 범주형 데이터를 모형이 인식할 수 있도록 숫자형으로 변환
Adata.info()
Adata['sex'].unique()
Adata['embarked'].unique()
#Adata['sex'] -> 더미변수로 만들기 (숫자형으로 변환) - one-not-encoding 처리
onhot_sex = pd.get_dummies(Adata['sex'])
onhot_sex
# 합치기
Adata = pd.concat([Adata,onhot_sex ],axis=1)
Adata.head()
onhot_embarked = pd.get_dummies(Adata['embarked'],prefix='town')
onhot_embarked.head()
# 합치기
Adata = pd.concat([Adata,onhot_embarked ],axis=1)
Adata.head(2)
'''
[Step 4] 데이터셋 구분 - 훈련용(train data)/ 검증용(test data)
'''
# 속성(변수) 선택
 #독립 변수 X       [['pclass', 'age', 'sibsp', 'parch', 'female', 'male',  'town_C', 'town_Q', 'town_S']]
#종속 변수 Y          y=ndf['survived']

x = Adata[['pclass', 'age', 'sibsp', 'parch', 'female', 'male', \
           'town_C', 'town_Q', 'town_S']]
#x1=Adata[['pclass','age','sibsp','parch','female','male','town_C','town_Q','town_S']]
#x1
x.head()
x.info()
x['male'].unique()
y = Adata['survived']
# 설명 변수 데이터를 정규화(normalization)
from sklearn import preprocessing
x = preprocessing.StandardScaler().fit(x).transform(x)
x
# train data 와 test data로 구분(7:3 비율)
from sklearn.model_selection import train_test_split
x_train,x_test, y_train,y_test = train_test_split(x,y ,test_size=0.3, random_state=10)
print('train data 수 : ', x_train.shape)
print('test  data 수 : ', x_test.shape)

# [Step 5] KNN 분류 모형 - sklearn 사용'''
# sklearn 라이브러리에서 KNN 분류 모형 가져오기
from sklearn.neighbors import KNeighborsClassifier
# 모형 객체 생성 (k=5로 설정)
knn = KNeighborsClassifier(n_neighbors=5)
# train data를 가지고 모형 학습
knn.fit(x_train, y_train)
# test data를 가지고 y_hat을 예측 (분류)
y_hat = knn.predict(x_test)
print(y_hat[0:10])
print(y_test.values[0:10])
# 모형 성능 평가 - confusion matric 계산
from sklearn import metrics
knn_matrix = metrics.confusion_matrix(y_test, y_hat)
print(knn_matrix)
# 모형 성능 평가 - 평가지표 계산
knn_report = metrics.classification_report(y_test, y_hat)
print(knn_report)


# [Step 5] svm 분류 모형 - sklearn 사용
# Support Vector Machine
# sklearn 라이브러리에서 svm 분류 모형 가져오기
from sklearn import svm
# 모형 객체 생성 (k=5로 설정)
svm_model = svm.SVC(kernel="rbf") # rbg, linear, polyminal, Sigmoid
# train data를 가지고 모형 학습
svm_model.fit(x_train, y_train)
# test data를 가지고 y_hat을 예측 (분류)
y_hat = svm_model.predict(x_test)
print(y_hat[0:10])
print(y_test.values[0:10])
# 모형 성능 평가 - confusion matric 계산
from sklearn import metrics
svm_metrix = metrics.confusion_matrix(y_test, y_hat)
print(svm_metrix)
# 모형 성능 평가 - 평가지표 계산
svm_report = metrics.classification_report(y_test, y_hat)
print(svm_report)
