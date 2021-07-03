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


# 결측치 "OT" 대체
drinks['continent'] = drinks['continent'].fillna('OT')
drinks.info()
drinks.head(10)
drinks.loc[:,"beer_servings"]
result = drinks.groupby("continent").mean()["beer_servings"]
print(result)
print(type(result))
df = result.to_frame()
print(df)
print(type(df))
df.index
df.columns
df = df.rename(columns={"beer_servings":"beer_servings_cont_avg"})
print(df)
df.info()
drinks= pd.merge(drinks,df,on="continent",how="outer")
print(drinks)
df.index
df.columns
df.info()
drinks[["country","continent","beer_servings","beer_servings_cont_avg"]].head
drinks[["country","continent","beer_servings","beer_servings_cont_avg"]].sample(5).head()

# 국가별 total-serving(beer,spirit,wine) 피쳐(칼럽)을 만들어서 drinks에 병합하시오

drinks["total_servings"] = drinks["beer_servings"] + \
                           drinks["spirit_servings"] + drinks["wine_servings"]
drinks[["country","continent","beer_servings","total_servings"]].head()

# 전체 평균보다 큰 알코올 (평균)을 섭취하는 대륙중에서 beer를 가장 많이 마시는 국가 구하기
# 12:00 시까지
# 1. 전체 평균 구하기
total_mean = drinks.total_litres_of_pure_alcohol.mean()
print(total_mean)
# 2. 대륙별 평균 구하기
continent_mean = drinks.groupby("continent").total_litres_of_pure_alcohol.mean()
print(continent_mean)
# 3. 평균 이하 마시는 대륙
continent_upper_mean = continent_mean[continent_mean < total_mean]
print(continent_upper_mean)
# index 값만, list로 만들기
continent_upper_mean = continent_mean[continent_mean < total_mean].index.tolist()
print(continent_upper_mean)

df_continent_upper_mean = drinks.loc[drinks.continent.isin(continent_upper_mean)]
print(df_continent_upper_mean)

# spirit 가장 많이 마시는 국가
most_spirit_upper_mean = \
    df_continent_upper_mean.loc[df_continent_upper_mean["spirit_servings"].idxmax()]
print(most_spirit_upper_mean)
# 술소비량 대비 알콜 비율 구하기, 전체 순위중 대한민국 순위를 구하세요
#drinks["total_servings"] = drinks["beer_servings"] + \
#                           drinks["spirit_servings"] + drinks["wine_servings"]
# 대한민국이 술소비량대비 알콜비율이 전체 순위중 몇위인가요
# 1. 술소비량 대비 알콜 비율에 대한 피쳐를 만들기
drinks["alcohol_rate"] = drinks["total_litres_of_pure_alcohol"] / drinks["total_servings"]
drinks["alcohol_rate"] = drinks["alcohol_rate"].fillna(0)
drinks["alcohol_rate"]
# 2. 전체 순위중 한국 순위 구하기 - rank() 함수 사용
#      순위 소수점 이하 없애지 - np.floor
drinks["alcohol_rate_rank"] = drinks["alcohol_rate"]
drinks["alcohol_rate_rank"] = drinks["alcohol_rate"].rank(ascending=False)
drinks["alcohol_rate_rank"] = drinks["alcohol_rate_rank"].apply(np.floor)
drinks["alcohol_rate_rank"]
drinks.loc[drinks["country"] == "South korea"].alcohol_rate_rank


