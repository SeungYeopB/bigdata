# 1장 연습 문제
# total_servings : beer_servings, spirit_servings, wine_servings의 합을 통해 실질적인 소비량을 계산
# alcohol_rate : 소비량 대비 알콜 비율을 계산
# alcohol_rate_rank, alcohol_rate_continent 등으로 응용.

# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = './drinks.csv'
drinks = pd.read_csv(file_path) # read_csv 함수로 데이터를 Dataframe 형태로 불러옵니다.
drinks['continent'] = drinks['continent'].fillna('OT')

#[대륙별 평균 wine_servings 탐색]
#대륙별 평균 wine_servings 피처를 만들어서 병합합니다.
result = drinks.groupby('continent').mean()['wine_servings']
print(result)
df = result.to_frame().reset_index()
print(df)
df = df.rename(columns={'wine_servings': 'wine_servings_cont_avg'})
print(df)
drinks = pd.merge(drinks, df, on='continent', how='outer')
print(drinks)
drinks.index
drinks.columns
# 위와 같은 방법의 코드입니다.
#wine_serving 대륙별 평균 항목 추가 작업
drinks['wine_servings_cont_avg'] = drinks.groupby('continent')['wine_servings'].transform(np.mean)
drinks0 = drinks.groupby('continent')['wine_servings'] # 내용 보기 어려움 시리즈라
drinks1 = drinks.groupby('continent')['wine_servings'].transform(np.mean)
#drinks1.info()
print(drinks)
print(drinks1)
#print(drinks0)
#drinks0
#drinks0.info()
drinks.head()
drinks.index
drinks.columns
# 결과를 출력합니다.
drinks[['country', 'continent', 'wine_servings_cont_avg']].sample(5).head()

# 대륙별 평균 wine_servings 피처 생성

# transform 함수가 있다면, 이 모든 과정을 단 한줄의 코드로 수행할 수 있습니다.
#
# 국가별 total_servings 피처를 만들어서 병합합니다.
drinks['total_servings'] = drinks['beer_servings'] + drinks['wine_servings'] + drinks['spirit_servings']

# 결과를 출력합니다.
drinks[['country', 'beer_servings', 'wine_servings', 'spirit_servings', 'total_servings']].sample(5).head()
drinks[['country', 'beer_servings', 'wine_servings', 'spirit_servings', 'total_servings']].sample(5).head()

# 국가별 total_servings 피처 생성

# [전체 평균보다 적은 알코올을 섭취하는 대륙 중에서, spirit을 가장 많이 마시는 국가 구하기]
# 전체 평균보다 적은 알코올을 섭취하는 대륙 중에서, spirit을 가장 많이 마시는 국가를 구합니다.
total_mean = drinks.total_litres_of_pure_alcohol.mean()
total_mean
continent_mean = drinks.groupby('continent').total_litres_of_pure_alcohol.mean()
continent_mean
continent_under_mean = continent_mean[continent_mean <= total_mean].index.tolist()
continent_under_mean

df_continent_under_mean = drinks.loc[drinks.continent.isin(continent_under_mean)]
df_continent_under_mean
df_continent_under_mean.loc[df_continent_under_mean['spirit_servings'].idxmax()]
most_spirit_under_mean = df_continent_under_mean.loc[df_continent_under_mean['spirit_servings'].idxmax()]

# 결과를 출력합니다.
most_spirit_under_mean['country']

# 전체 평균보다 적은 알코올을 섭취하는 대륙 중에서, spirit을 가장 많이 마시는 국가

## [술 소비량 대비 알콜 비율 구하기]

# 술 소비량 대비 알콜 비율에 대한 칼럼을 만들어서 병합합니다.
drinks['alcohol_rate'] = drinks['total_litres_of_pure_alcohol'] / drinks['total_servings']
drinks['alcohol_rate'] = drinks['alcohol_rate'].fillna(0)

# 술 소비량 대비 알콜 비율 : 전체 순위 중 한국의 순위를 구합니다.
drinks['alcohol_rate_rank'] = drinks['alcohol_rate'].rank(ascending=False)
drinks['alcohol_rate_rank']
# 각 원소 값보다 작거나 같은 가장 큰 정수 값 (바닥 값)으로 내림
#
# 출처: https://rfriend.tistory.com/293 [R, Python 분석과 프로그래밍의 친구 (by R Friend)]
drinks['alcohol_rate_rank'] = drinks['alcohol_rate_rank'].apply(np.floor)
drinks['alcohol_rate_rank']

drinks.loc[drinks['country'] == 'South Korea'].alcohol_rate_rank

# 술 소비량 대비 알콜 비율에 대한 피처 생성


# [대륙별 술 소비량 대비 알콜 비율 구하기]
# 대륙별 술 소비량 대비 알콜 비율을 구합니다.
continent_sum = drinks.groupby('continent').sum()
continent_sum
continent_sum.index
continent_sum.columns
continent_sum['alcohol_rate_continent'] = continent_sum['total_litres_of_pure_alcohol'] / \
                                         continent_sum['total_servings']
continent_sum.index
continent_sum.columns
continent_sum
continent_sum = continent_sum.reset_index()
continent_sum.index
continent_sum.columns
continent_sum = continent_sum[['continent', 'alcohol_rate_continent']]
drinks = pd.merge(drinks, continent_sum, on='continent', how='outer')
drinks
# 결과를 출력합니다.
drinks[['country', 'continent', 'alcohol_rate_continent']].sample(5).head()
