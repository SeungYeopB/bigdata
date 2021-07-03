# 1. 데이터 가져 오기 및 구성 요소 살펴보기   : 10분  9:47분 까지
# chipotle.tsv 파일로 작업
import pandas as pd
# data 읽기
file_path = './chipotle.tsv'
chipo = pd.read_csv(file_path, sep = '\t')
print(chipo.shape)
print(chipo.describe())
print(chipo.info())
print(chipo.index)
chipo
print(chipo.columns)
print(chipo.head())
print(chipo.tail())
#order_id - 주문번호
#quantity - 수량
#item_name - item 이름
#choice_description - 토핑 내용  - null data 예측됨
#item_price -  가격 -  $로 표시됨

# order_id를 문자열로 변경하세요, 기존 자료에 적용하세요   10:5분 까지
# 적용된것 확인 하세요
chipo.describe()
chipo['order_id'] = chipo['order_id'].astype(str)
chipo.describe()
chipo.info()
type(chipo['order_id'])
chipo.head()

# order_id 와  item_name 의 숫자를 확인하세요 (order 갯수와 item갯수 확인 )
# 중복되지 않는 값 확인하는 명령어
# len(), unique()
chipo['order_id'].unique()
len(chipo['order_id'].unique())
print(len(chipo['order_id'].unique()))
chipo['item_name'].unique()
len(chipo['item_name'].unique())
print(len(chipo['item_name'].unique()))

# 가장 많이 주문하는 item top 10 - 출력
# value_counts() - 특정 series에  객체를 반환
chipo['item_name'].value_counts().head(10)
chipo['item_name'].value_counts()[:10]
item_top10 = chipo['item_name'].value_counts()[:10]
print(type(item_top10))

#  Top 10 내용 출력 하기     :  11:10분 까지
#---------------------------
#   Top 1 : Chicken Bowl  726
#   Top 2 : Chicken Burrito  553
#   ~
#   Top 10 : Chips and Fresh Tomato  Salsa 110
item_top10.index
item_top10.values
#item_top10.columns # 의미 없음
item_top10.iteritems()

item10 = item_top10.iteritems()  # iterable 객체로 변경
for idx ,( itm, value) in enumerate(item_top10.iteritems(),1):
    print("Top",idx, ":", itm, value)

for itm, value in item_top10:   # error
    print("Top",idx, ":", itm, value)

idx = 0
for itm, value in item10:
    idx += 1
    print("Top",idx, ":", itm, value)

# item별 주문개수 와 총량 구하기
# groupby() 사용 ,갯수 - count(),  , 총량 - sum() 사용  11:50 분 까지
chipo.info()
ord_cnt = chipo.groupby('item_name')['order_id'].count()
print(ord_cnt)
tot_qty = chipo.groupby('item_name')['quantity'].sum()
print(tot_qty)
print(type(tot_qty))
print(tot_qty.index)
idx = tot_qty.index
idx
print(type(idx))
print(tot_qty.values)
# 아이템별 주문 총량을 bar graph로 그려 주세요 .  10분

import matplotlib.pyplot as plt
# 주문 갯수 로 graph 그리기
plt.figure(figsize=(15,10))
plt.bar(idx,ord_cnt,align='center')
plt.xticks(rotation=45)
plt.ylabel("Order Count")
plt.xlabel("items")
plt.show()
# 주문 총량 로 graph 그리기
plt.figure(figsize=(10,10))
plt.bar(idx,tot_qty,align='center',color='red')
plt.ylabel("Order Total")
plt.xlabel("items")
plt.xticks(rotation=45)
plt.show()

chipo.info()
print(type(chipo.item_price))
chipo.head()

chipo.iloc[0,4]
chipo.iloc[0,4][1:]
float(chipo.iloc[0,4][1:])
chipo.item_price = chipo.item_price.apply(lambda x:float(x[1:]))
chipo.describe()

chipo.info()
chipo.groupby("order_id")
chipo.groupby("order_id")["item_price"].sum().mean()
# 한주문당 10달러 이상 사용한 id 출력 - 10분
#groupby , sum()  금액 비교
chi_group = chipo.groupby("order_id").sum()
print(chi_group)
t_id = chi_group[chi_group.item_price >= 20]
print(t_id)
print(t_id.index.values)
#가장 비싼 주문. item이 총 몇개 팔렷는지 계산 하세요.
# 가장 수량이 많은 주문
chipo.groupby("order_id").sum().sort_values(by="quantity", ascending=False)[:1]
chipo.groupby("order_id").sum().sort_values(by="quantity", ascending=False)[:10]
# 가장 비싼 주문
chipo.groupby("order_id").sum().sort_values(by="item_price", ascending=False)[:10]

# Chicken Bowl 몇 번 주문 됏는지 계산 하세요, 중복제거 - 같은 order에서 중복 된거 제거 3:5분
chipo
chipo["item_name"]
chipo.info()
chipo["item_name"] == "Chicken Bowl"
Bowl_ordered = chipo[chipo["item_name"] == "Chicken Bowl"]
print(Bowl_ordered)
Bowl_ordered1 = Bowl_ordered.drop_duplicates(["item_name","order_id"])
Bowl_ordered2 = Bowl_ordered.drop_duplicates(["order_id"])
print(len(Bowl_ordered1))
print(len(Bowl_ordered2))
print(Bowl_ordered.head())

# # Chicken Bowl 을 2개 이상 주문한 주문 횟수 구하기.
Bowl_ordered = chipo[chipo["item_name"] == "Chicken Bowl"]

Bowl_ordered.info()
Bowl_ordered_cnt = Bowl_ordered[Bowl_ordered["quantity"] >= 2]
Bowl_ordered_cnt1 = Bowl_ordered_cnt.drop_duplicates(["item_name", "order_id"])
print(len(Bowl_ordered_cnt1))

##  Chicken Bowl 을 2개 이상 주문한 고객들의 Chicken Bowl 총 주문 수량 구하기

Bowl_ordered = chipo[chipo["item_name"] == "Chicken Bowl"]
Bowl_ordered
Bowl_ordered.info()
Bowl_ordered_sum = Bowl_ordered.groupby("order_id").sum()["quantity"]
Bowl_ordered_sum
Bowl_ordered_sum_result = Bowl_ordered_sum[Bowl_ordered_sum >= 2]
Bowl_ordered_sum_result
print(len(Bowl_ordered_sum_result))

## data 불러오기
## data 기초 사항 분석
## 상관분석 술소비량에 대한 상관분석을 수행
## 결측치 찾아서 co ntinental - "OT" EOCP
## 전체 평균보다 많은 알콜을 섭취하는 대륙은 어디 일까요?
## 평균 맥주 소비량이 가장 높은 대륙은 어디일까요?
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
file_path = './drinks.csv'
drinks = pd.read_csv(file_path)
print(drinks.info())
drinks.head()
drinks.index
drinks.columns
drinks.describe()
#3. 상관 분석
corr = drinks[['beer_servings','wine_servings']]
print(corr)
corr.corr()
corr.corr(method='pearson')
# 항목을 여러 항목으로
colum = ['beer_servings', 'spirit_servings', 'wine_servings',
       'total_litres_of_pure_alcohol']
print(colum)
corr1 = drinks[colum].corr(method='pearson')
print(corr1)
# graph 그리기
# heatmap
corr1.index
corr1.columns
corr1.values

# pip instll seanborn
import seaborn as sns

view = ['beer', 'spirit', 'wine', 'alcohol']
sns.set(font_scale=1.5)
hmap = sns.heatmap(corr1.values,
        cbar = True, # 컬러 막대 그래프
        annot = True, # 각셀의 값 표현
        square = True, # 사각
        fmt = '.2f',   # 값의  데이터 타입
        annot_kws = {'size' : 15}, # annotation key,value로 지정
        xticklabels = view,   # x축의 내용 표시
        yticklabels = view)   # y 축의 내용 표시

plt.tight_layout()
plt.show()

# pairplot

sns.set(style = 'whitegrid', context='notebook')
sns.pairplot(drinks[colum],height=2.5)
plt.show()

sns.set(style = 'darkgrid', context='poster')  # 사이즈 선택, context = paper, notebook, talk, poster
sns.pairplot(drinks[colum],height=2.5)          # style 테마 지정 : darkgrid, whitegrid, dark, white, ticks
plt.show()

drinks.info()
# 결측치 "OT" 대체
drinks['continent'] = drinks['continent'].fillna('OT')
drinks.info()
drinks.head(10)

# 파이 챠트로 시각화 하기
label = drinks['continent']
print(label)
label = drinks['continent'].value_counts()
print(label)
label = drinks['continent'].value_counts().index
print(label)
label = drinks['continent'].value_counts().index.tolist()
print(label)
value = drinks['continent'].value_counts().values.tolist()
print(value)
explod = (0.25,0,0,0.25,0,0)

plt.pie(value,labels=label, autopct='%.0f%%' ,  shadow=True )
plt.pie(value,explode= explod, labels=label, autopct='%.0f%%' ,  shadow=True )

explod=(0.25,0,0,0.25,0,0)
print(explod)
plt.pie(value,labels=label,autopct='%.0f%%',shadow=True)
plt.pie(value,explode=explod,labels=label,autopct='%.0f%%',shadow=True)

drinks.columns
# 전체 평균보다 많은 알콜을 섭취하는 대륙은 어디 일까요?
tot_mean = drinks.total_litres_of_pure_alcohol.mean()
print(tot_mean)
cont_mean = drinks.groupby('continent')['total_litres_of_pure_alcohol']
print(cont_mean)
cont_mean = drinks.groupby('continent')['total_litres_of_pure_alcohol'].mean()
cont_over_mean = cont_mean[cont_mean >= tot_mean]
print(cont_over_mean)

#  평균 맥주 소비량이 가장 높은 대륙은 어디일까요?
beer_cont = drinks.groupby('continent').beer_servings.mean()
print(beer_cont)
beer_cont.sort_values(ascending=True)
beer_cont = drinks.groupby('continent').beer_servings.mean().idxmax()
print(beer_cont)
beer_cont.index
beer_cont = drinks.groupby('continent').beer_servings.mean().max()
print(beer_cont)
beer_cont = drinks.groupby('continent').beer_servings.mean().min()
print(beer_cont)

# agg 함수 사용 , apply 사용
# wine에 대해  대륙별 평균, 최소,최대,합계 계산하기
result_agg = drinks.groupby('continent').wine_servings.agg(['mean','min','max','sum'])
print(result_agg)

# 시각화 하기
# group 갯수 계산

n_groups = len(result_agg)
print(n_groups)
means = result_agg['mean']
print(means)
print(type(means))
# means 를 list로 만들기
means = result_agg['mean'].tolist()
mins = result_agg['min'].tolist()
maxs = result_agg['max'].tolist()
sums = result_agg['sum'].tolist()
print(means)
print(type(means))
print(result_agg)
x_value = result_agg.index.tolist()
print(x_value)
bar_width = 0.1
plt.bar(x_value, means,  bar_width, color ='r', label='Mean')
plt.bar(x_value, mins,  bar_width, color ='g', label='Mins')
plt.bar(x_value, maxs,  bar_width, color ='b', label='Maxs')
plt.bar(x_value, sums,  bar_width, color ='y', label='Sums')


import numpy as np
n_groups = len(result_agg)
print(n_groups)
index = np.arange(n_groups)
print(index)
rect1 = plt.bar(index, means,  bar_width, color ='r', label='Mean')
rect2 = plt.bar(index+bar_width, mins,  bar_width, color ='g', label='Mins')
rect3 = plt.bar(index+bar_width*2, maxs,  bar_width, color ='b', label='Maxs')
rect4 = plt.bar(index+bar_width*3, sums,  bar_width, color ='y', label='Sums')
plt.xticks(index,result_agg.index.tolist() )
plt.legend()

# sprite에 대해  대륙별 평균, 최소,최대,합계 계산하기 & graph 그리기  2:15뿐 까지
result_agg = drinks.groupby('continent').spirit_servings.agg(['mean','min','max','sum'])
print(result_agg)
drinks.info()

# 시각화 하기
# group 갯수 계산

n_groups = len(result_agg)
print(n_groups)
means = result_agg['mean']
print(means)
print(type(means))
# means 를 list로 만들기
means = result_agg['mean'].tolist()
mins = result_agg['min'].tolist()
maxs = result_agg['max'].tolist()
sums = result_agg['sum'].tolist()
print(means)
print(type(means))
print(result_agg)
x_value = result_agg.index.tolist()
print(x_value)
bar_width = 0.1
plt.bar(x_value, means,  bar_width, color ='r', label='Mean')
plt.bar(x_value, mins,  bar_width, color ='g', label='Mins')
plt.bar(x_value, maxs,  bar_width, color ='b', label='Maxs')
plt.bar(x_value, sums,  bar_width, color ='y', label='Sums')


import numpy as np
n_groups = len(result_agg)
print(n_groups)
index = np.arange(n_groups)
print(index)
rect1 = plt.bar(index, means,  bar_width, color ='r', label='Mean')
rect2 = plt.bar(index+bar_width, mins,  bar_width, color ='g', label='Mins')
rect3 = plt.bar(index+bar_width*2, maxs,  bar_width, color ='b', label='Maxs')
rect4 = plt.bar(index+bar_width*3, sums,  bar_width, color ='y', label='Sums')
plt.xticks(index,result_agg.index.tolist() )
plt.legend()

# 대륙별 total_liters_of_pure_alcohol의 시각화
cont_mean = drinks.groupby('continent')['total_litres_of_pure_alcohol'].mean()
print(cont_mean)
print(type(cont_mean))
conts = cont_mean.index.tolist()
conts.append('mean')
print(conts)
x_pos = np.arange(len(conts))
print(x_pos)
alcohol = cont_mean.tolist()
print(alcohol)
tot_mean = drinks.total_litres_of_pure_alcohol.mean()
print(tot_mean)
alcohol.append(tot_mean)
print(alcohol)
bar_list = plt.bar(x_pos, alcohol, align='center', alpha=0.8) # alpha 투명도
print(type(bar_list))
print(len(bar_list))
print(len(conts))
bar_list[len(conts) - 1].set_color('r')
bar_list[len(bar_list) - 1].set_color('r')
# 선긋기 - 평균에 해댕하는 값
plt.plot([0.,6],[tot_mean,tot_mean],'k--')
plt.xticks(x_pos,conts)
plt.ylabel('total_liters_of_pure_alcohol')
plt.xlabel('total_liters_of_pure_alcohol by continent')
plt.show()

#  beer_servings 시각화하기

drinks.info()
beer = drinks.groupby("continent")["beer_servings"].sum()
print(beer)
print(type(beer))
conts = beer.index.tolist()
print(type(conts))
conts
x_pos = np.arange(len(conts))
print(x_pos)
alcohol = beer.tolist()
print(alcohol)
bar_list = plt.bar(x_value, alcohol, align="center", alpha=0.8)
conts.index
bar_list[conts.index("EU")].set_color("r")
bar_list[2].set_color("r")
plt.xticks(x_pos, conts)
plt.ylabel("beer_servings")
plt.title("beer_servings by continent")
plt.show()

##T test, T검증
##두 집단간의

africa = drinks.loc[drinks["continent"]=="AF"]
print(africa)
africa.index
africa.columns
europe = drinks.loc[drinks["continent"]=="EU"]
print(europe)
europe.index
europe.columns

## 가설 : 아프리카 와 유럽의 맥주 소비량이 같다.
## stats.ttest_ind() : t - statistic, pvalue 산출,
## p-value를 가지고 가설이 의미가 있는지를 판별
# 기준 : 0.05 또는 0,01, pvalue 가 0.01 이하보다 작으면 가설

from scipy import stats
# 분산이 같은경우
tTestResult = stats.ttest_ind(africa["beer_servings"],europe["beer_servings"])
print(tTestResult)
print("t-statistics and p;value %.3f, %.3f"% tTestResult)
# 분산이 다른경우
tTestResultDiff = stats.ttest_ind(africa["beer_servings"], \
                              europe["beer_servings"],equal_var=False)
print(tTestResultDiff)
print("t-statistics and p;value %.3f, %.3f"% tTestResultDiff)