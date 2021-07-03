### 기본 라이브러리 불러오기
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
'''
[Step 1] 데이터 준비 -  자동차 연비 데이터셋 가져오기
'''
# CSV 파일을 데이터프레임으로 변환
df = pd.read_csv("./auto-mpg.csv", header=None)
df
# 열 이름 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight',
              'acceleration','model year','origin','name']
# 데이터 살펴보기
df
df.index
df.columns
df.head()
'''
[Step 2] 데이터 탐색
'''
# 데이터 자료형 확인
print(df.info())
# 데이터 통계 요약정보 확인
print(df.describe())
# horsepower 열의 자료형 변경 (문자열 > 숫자)
df.horsepower
df["horsepower"].unique()
# ? 제거, ? 대체 - nan 값으로, 삭제,
df["horsepower"].replace("?",np.nan, inplace=True)
df["horsepower"].unique()
df.dropna(subset=["horsepower"], axis=0, inplace=True)
df["horsepower"].unique()
print(df.info())
print(df.describe())
# 숫자로 변형(.astype("float")
df["horsepower"] = df["horsepower"].astype("float")
df.info()
print(df.horsepower.describe())
'''
[step 3] 속성(feature 또는 variable) 선택
'''
#분석에 활용할 열(속성)을 선택 ndf로 만들기
#(연비. 실린더. 출력. 중량)-" mpg", "cylinders","horsepower","weight"
ndf = df[["mpg","cylinders","horsepower","weight"]]
ndf
ndf.head()
ndf.sample(5)
ndf.tail()
ndf.sample(10)
## 종속 변수 y인 "연비(mpg)"와 다른 변수간의 선형관계를 그래프(산점도)로 확인
# Matplotlib으로 산점도 그리기, x = "weight", y="mpg"
ndf.plot(kind="scatter", x="weight", y="mpg",c="coral",s=10,figsize=(10,5))
plt.show()
plt.close()
ndf.plot(kind="scatter", x="cylinders", y="mpg",c="coral",s=10,figsize=(10,5))
plt.show()
plt.close()
ndf.plot(kind="scatter", x="horsepower", y="mpg",c="coral",s=10,figsize=(10,5))
plt.show()
plt.close()
fig = plt.figure(figsize=(10,5))
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)
sns.regplot(x="weight", y="mpg", data=ndf, ax=ax1)
sns.regplot(x="weight", y="mpg", data=ndf, ax=ax1, fit_reg=False)
plt.show()
plt.close()

#seaborn 조인트 그래프 - 산점도, 히스토그램
sns.jointplot(x="weight", y="mpg", data=ndf)
plt.show()
plt.close()
sns.jointplot(x="weight", y="mpg",kind="reg", data=ndf)
plt.show()
plt.close()
#seaborn pariplot으로 두 변수 간의 모든 경우의 수 그리기
grid_ndf = sns.pairplot(ndf)
plt.show()
plt.close()

# 머신러닝
# 기계(컴퓨터 알고리즘) 스스로 데이터를 학습하고 서로 다른변수간의 관계를
# 찾아가는 과정
# 해결하려는 문제에 따라 - 예측, 분류, 군집 알고리즘으로 분류된다.
# 주가, 환율 예측, 은행 고객분류 - 대출 승인. 거절. 비슷한 소비패턴 가진 고객 유형을 분류
# 인공 지능 = 머신러닝. 딥러닝 포함.
# 지도학습(unsupervised learning) - 정답 데이터를 다른 데이터와 함께 컴퓨터 알고리즘에 입력 처리
#                                  회귀분석, 분류
# 비지도 학습(unsupervised learning) - 정답 없이 컴퓨터 알고리즘
#                                     스스로 데이터로 부터 숨은 패턴을 찾아 내는 방식
#                                     군집분석
# 순서 - 데이터 정리 - 데이터분리(100% 정답 데이터 7:3 분리) - 알고리즘 준비
#                  - 훈련데이터(7할)로 모형 학습 --> 검증데이터(3할) 예측 --> 평가 --> 활용
# 데이터셋 분리 - 훈련데이터(train data)/검증용)(test data)
# 속성(변수) 선택
# x = 독립 변수,  weight 사용, y = 종속변수, mpg 사용
x = ndf[["weight"]]
x
y = ndf[["mpg"]]
y
# 데이터 분리 7:3
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,  ## 독립변수
                                                    y,  ## 종속변수
                                                    test_size=0.3,  # 검증용 30%
                                                    random_state=10)
print("train data 수:", len(x_train))
print("test data 수:", len(x_test))

# 5) 모형 학습및 검증
# sklearn에서 선형회기분석 모듈 가져오기
from sklearn.linear_model import LinearRegression

# 단순회귀분석 모형 객체 생성
lr = LinearRegression()
# 모형 학습
lr.fit(x_train, y_train)
# r_square = > 결정계수 ,  값이 클수록 에측 능력이 좋다고 판단.
r_square = lr.score(x_test, y_test)
print(r_square)
ndf.info()
# y = ax + b    a : 기울기    b : 절편
#     a 값  - 모형객체.coef_ b 값 - 모형객체.intercept_

# 회귀식 기울기
print("기울기 a:", lr.coef_)
# 절편
print("절  편 b:", lr.intercept_)

# 값 예측
y_hat = lr.predict(x)
print(y_hat)
df[["weight"]].head()
y_hat1 = lr.predict([[3504.0]])
y_hat1

yy = -0.0077343 * 3504.0 + 46.71036626
yy
# 원래 y 값 : 종속변수(mpg)
# 새로운 y 값 : y_hat

plt.figure(figsize=(10,5))
ax1 = sns.distplot(y, hist=False, label="y")
ax2 = sns.distplot(y_hat, hist=False, label="y_hat", ax=ax1)
plt.legend()
plt.show()
plt.close()

# 연습 : horsepower 와 mpg 를 이용해서
# 변수 선택서 부터 학습 , 평가까지 실행 해보세요요

AIzaSyBbU-JUBY-LtjGuNUtQu_6Xyu7XcZkIFPo