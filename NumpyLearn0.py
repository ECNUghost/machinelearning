import numpy as np

arr = np.array([2, 6, 5, 9], float)
# print(type(arr))
# print(arr.tolist())

# 创建n维数组的单位矩阵
arr0 = np.identity(5, dtype=float)
# print(arr0)

# 返回第K条对角线上元素为1的矩阵
arr1 = np.eye(3, k=0, dtype=float)
# print(arr1)

# 按照指定维度创建数组
arr2 = np.ones((2, 3), dtype=float)
# print(arr2)
arr3 = np.zeros(5, dtype=int)
# print(arr3)

# 模仿现有数组创建的数组zeros_like()或者ones_like()
arr4 = np.array([[13, 32, 31], [64, 25, 76]], float)
arr5 = np.zeros_like(arr4)
# print(arr5)

# 垂直方向合并两个数组
arr6 = np.array([1, 3, 2])
arr7 = np.array([3, 4, 6])
arr8 = np.vstack([arr6, arr7])
# print(arr8)

# 返回数组所包含的不同的元素
arr9 = np.array([2, 5, 6, 5])
arr10 = np.unique(arr9)
# 排序数组
arr11 = np.sort(arr9)
# 根据索引排序
arr12 = np.argsort(arr9)
# 使数组随机排列(test fail)
# arr13 = np.random.shuffle(arr9)
# 比较两个数组是否相等
arr14 = np.array_equal(arr9, np.array([2, 5, 5, 6]))
# print('arr10:', arr10, 'arr11:', arr11, 'arr12', arr12, 'arr14:', arr14)

matrix = np.array([[1, 2, 3], [4, 5, 6]], float)
# print(matrix, matrix[0, 1])
# print(matrix[1:2, 2:3], matrix[1, :], matrix[:, 2], matrix[-1:, -2:])

# 多维数组变一维数组
arr15 = matrix.flatten()
# print(arr15)

# 得到数组大小shape,返回数组类型dtype
# print(matrix.shape, arr15.shape, matrix.dtype)

# 数组类型转换
int_matrix = matrix.astype(np.int32)
# print(int_matrix.dtype)

# 返回数组第一维的长度
# print(len(matrix))
# 判断数组中是否含有某个元素
# print(2 in matrix, 7 in matrix)

# reshape可以调整数组维度
arr16 = np.array([0, 1, 2, 3, 4, 5, 6, 7], float)
arr17 = arr16.reshape(4, 2)
# print(arr17)

# 矩阵转置（维度互换）
arr18 = np.array(range(6), float).reshape(2, 3)
# print(arr18)
arr19 = arr18.transpose()
arr20 = arr18.T
# print(arr19)
# print(np.array_equal(arr19, arr20))

# newaxis增加维度
arr21 = np.array([0, 1, 2], float)
arr22 = arr21[:, np.newaxis]
arr23 = arr21[np.newaxis, :]
print(arr21, arr21.shape)
print(arr22, arr22.shape)
print(arr23, arr23.shape)