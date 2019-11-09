import numpy as np

arr1 = np.array([1, 2, 3], float)
arr2 = np.array([1, 2, 3], float)
# 数组运算(维度要相同)
arr3 = arr1 + arr2
arr4 = arr1 - arr2
arr5 = arr1 * arr2
arr6 = arr1 / arr2
arr7 = arr1 % arr2
arr8 = arr2 ** arr1
# print('arr3:', arr3, 'arr4:', arr4, 'arr5:', arr5, 'arr6:', arr6, ' arr7:', arr7, 'arr8:', arr8)
# 当数组维度不同时，如果自身可以补齐，可以继续计算
arr9 = np.array([[1, 2], [3, 4], [5, 6]], float)
arr10 = np.array([1, 2], float)
arr11 = arr9 + arr10
# print('arr11:', arr11)

arr12 = np.zeros((2, 2), float)
arr13 = np.array([1, 2], float)
arr14 = arr12 + arr13
# print(arr14)
# 指定数组的广播方式？
arr15 = arr12 + arr13[np.newaxis, :]
arr16 = arr12 + arr13[:, np.newaxis]
# print(arr15)
# print(arr16)
# 数组的条件筛选，用布尔数组过滤
arr17 = np.array([[2, 3], [5, 9]], float)
arr18 = arr17 > 7
# print(arr18)
arr19 = arr17[arr17 > 7]
# print(arr19)
arr20 = arr17[np.logical_and(arr17 > 5, arr17 < 11)]
# print(arr20)

# 根据索引构造数组
arr21 = np.array([1, 4, 5, 9], float)
arr22 = np.array([0, 1, 1, 3, 3, 1, 1], int)
# print(arr21[arr22])
# print(arr21[[0, 1, 1, 3, 3, 1, 1]])
# 多维数组选取操作，第一个种子数组存储行号，第二个种子数组存储列号
arr23 = np.array([[1, 2], [5, 6]], float)
arr24 = np.array([0, 1, 1, 0], int)
arr25 = np.array([1, 1, 0, 0], int)
print(arr23[arr24, arr25])
