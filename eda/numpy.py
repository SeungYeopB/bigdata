import numpy as np

sc = np.array(1.2)
print(sc)
print(sc.shape)
print(sc.ndim)

ve = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(ve)
print(ve.shape)
print(ve.ndim)  # 1차원

ma = np.array([[0, 1, 2, 3],
              [4, 5, 6, 7]])
print(ma)
print(ma.shape)
print(ma.ndim)

te = np.array([[[[0, 1, 2, 3],
                [4, 5, 6, 7],
               [8, 9, 10, 11],
               [12, 13, 14, 15]]]])
print(te)
print(te.shape)
print(te.ndim)

data1 = [1, 2, 3, 4, 5]
print(data1)
data2 = [1, 2, 3, 4, 5, 4]
print(data2)
arr1 = np.array(data1)
print(arr1)
print(arr1.shape)
print(arr1.ndim)

data2 = np.array([1, 2, 3, 4, 5])
print(data2)
print(data2.shape)
print(data2.ndim)

np.zeros(10)
np.zeros((3,5))

np.ones(9)
np.ones((2,10))

ar1 = np.array([[1,2,3,],[4,5,6]])
ar1.shape
ar2 = np.array([[10,11,12],[13,14,15]])
ar2.shape

ar1 + ar2
ar2 - ar1
ar2 * ar1
ar2 / ar1

ar1 = np.array([[1,2,3,],[4,5,6]])
ar1.shape
ar3 = np.array([10,11,12])
ar3.shape
ar1 + ar3
ar1 * ar3

ar2 = np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12]])
ar2[0,0]
ar2[2,:]
ar2[2,3]
ar2[:,3]

ar1= np.arange(15).reshape(3,5)
ar1

for i in range(1,10):
    for j in range(1,10):
        print("{} * {} = {}".format(i,j,i*j))

ve = np.arange(1,10)

import numpy as np
gu_ar = np.zeros((81, 3))
print(gu_ar)
idx = 0
for i in range(1,10):
    for j in range(1,10):
        gu_ar[idx,0] = i
        gu_ar[idx,1] = j
        gu_ar[idx,2] = i * j
        idx += 1
print(gu_ar)
for i in range(0,81):
    if ( i % 9 == 0):
        dan = (i // 9) + 1
        print(dan, "--------------------------")
    print("{} * {} = {}".format(gu_ar[i,0],gu_ar[i,1],gu_ar[i,2]))
