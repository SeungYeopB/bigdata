import numpy as np

array1 = np.array([1, 2, 3, 4])
print(array1)
print(type(array1))

array1 = np.arange(10)
array2 = np.arange(10,20)

print(array1)
print(array2)
print(array1 * 2)
print(array1 + array2)
print(array1 + 2)
print(array1 ** 2)


import numpy as np

revenue_in_yen = [
    300000, 340000, 320000, 360000,
    440000, 140000, 180000, 340000,
    330000, 290000, 280000, 380000,
    170000, 140000, 230000, 390000,
    400000, 350000, 380000, 150000,
    110000, 240000, 380000, 380000,
    340000, 420000, 150000, 130000,
    360000, 320000, 250000
]

re = np.array(revenue_in_yen)
print(re)
print(type(re))
print((re/100) * 1032.78)

array1 = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31])
target = (array1 > 4)
print(target)
array1[target]

booleans = np.array([True, False, True, False, True])
array2 = np.array([2, 3, 5, 7, 11])
array2[booleans]
target1 = array1 % 2 ==0

array1[target1]


array1 = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31])
target = np.array([True, False, False, False, False, False, False, False, False, False, True])
# target = np.full(len(array1), False)
# target[-1] = True
# target[0] = True
array1[target]




array2 = np.arange(2,31,2)
array2
target = array2 % 3 ==0
target
var_of_multiple_of_6 = array2[target]
print(var_of_multiple_of_6)


array1 = np.array([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31])

array1.max()
array1.min()
array1.mean()
array1.std()
array1.var()

import pandas as pd

df2 = pd.read_csv("./practice/lec4_pandas/iphone.csv", index_col="기종")

df2
target = df2["디스플레이"] >= 5.5
target
df2[target]

target = (df2["디스플레이"] < 6) & (df2["Face ID"] == "Yes")
df2
df2.iloc[:,2:4]
df2.iloc[[1,3], 2:4]
df2.iloc[3:, [1,3]]


import pandas as pd

df = pd.read_csv("./practice/lec4_pandas/iphone.csv", index_col="기종")

target = df.loc[:,"Face ID"] == "No"
target
df['Face ID'] = "O"
df
df.loc[target,["Face ID"]] = 'X'

