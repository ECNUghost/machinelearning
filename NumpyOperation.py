import numpy as np

# take 函数
arr1 = np.array([7, 6, 6, 9], float)
arr2 = np.array([0, 3, 1, 1], int)
arr3 = arr1.take(arr2)
# print(arr3)

arr4 = np.array([[10, 21], [62, 33]], float)
arr5 = np.array([0, 0, 1], int)
arr6 = arr4.take(arr5, axis=0)
arr7 = arr4.take(arr5, axis=1)
# print(arr4)
# print(arr6)
# print(arr7)

# put函数是take函数的逆操作 未成功运行
arr8 = np.array([2, 1, 6, 2, 1, 9], float)
arr9 = np.array([3, 10, 2], float)
arr10 = arr8.put([1, 4], arr9)
# print(arr10)

# 线性代数运算
# np.dot计算内积 X^T*X
X = np.arange(15).reshape((3, 5))
# print(X)
# print(X.T)

arr11 = np.dot(X.T, X)
# print(arr11)

arr12 = np.array([12, 43, 10], float)
arr13 = np.array([21, 42, 14], float)
# print(np.outer(arr12, arr13))  # 计算外积
# print(np.inner(arr12, arr13))  # 计算内积
# print(np.cross(arr12, arr13))  # 计算叉积

matrix = np.array([[74, 22, 10], [92, 31, 17], [21, 22, 12]], float)
# print(matrix)
# print(np.linalg.det(matrix))

# 使用inv函数生成矩阵的逆矩阵
inv_matrix = np.linalg.inv(matrix)
# print(inv_matrix)
# print(np.dot(inv_matrix, matrix))

# 矩阵的特征值和特征向量
vals, vecs = np.linalg.eig(matrix)
# print(vals)
# print(vecs)

# 计算数组元素的均值
arr14 = np.random.rand(8, 4)
print(arr14)
print(arr14.mean())
print(np.mean(arr14))
print(arr14.sum())

# mean()计算均值，std、var 计算标准差和方差，min、max求数组的最小值和最大值，argmin和argmax返回最小和最大元素的索引

