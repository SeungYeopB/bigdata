import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set_style("whitegrid")

tips = sns.load_dataset("tips")
tips.head()

plt.figure(figsize=(8,6))
sns.boxplot(x="day",y="total_bill",data=tips)
plt.show()

palette = sns.color_palette("Set2")
sns.palplot(palette)
plt.figure(figsize=(8,6))
sns.boxplot(x="day",y="total_bill",hue="smoker", data=tips, palette="Set2")
plt.show()

sns.set_style("darkgrid")
sns.lmplot(x="total_bill", y="tip", data=tips, size=7)
plt.show()

sns.set_style("darkgrid")
sns.lmplot(x="total_bill",y="tip",hue="smoker", data=tips, palette="Set3")
plt.show()


# ci 신뢰구간 표시됨
# 범위 0 - 100 사이값, 95를 기술 한다면 양극단의 5% 제외한 값을 표시
tips["smoker"]
tips["smoker"].unique()

sns.set_style("darkgrid")
sns.lmplot(x="total_bill",y="tip",ci= 50,hue="smoker", data=tips, palette="Set3",size=7)
plt.show()
plt.close()

sns.set_style("darkgrid")
sns.lmplot(x="total_bill",y="tip",ci= 95,hue="smoker", data=tips, palette="Set3",size=7)
plt.show()
plt.close()

flights = sns.load_dataset("flights")
flights.info()
flights.index
flights.columns
flights
flights1 = flights.pivot("month", "year", "passengers")
flights1
plt.figure(figsize=(10,8))
sns.heatmap(flights1,annot=True, fmt="d")
plt.show()

sns.set(style="ticks")
iris = sns.load_dataset("iris")
iris.info()
iris.head()
iris["species"].unique()
iris.describe()
sns.pairplot(iris, hue="species")