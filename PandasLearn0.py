import pandas as pd


obj = pd.Series([3, 5, -2, 1])
# print(obj)
# print(obj.values)
# print(obj.index)
# print(obj * 2)
# print(obj[obj > 2])

# python字典可以转换为Series对象，字典的键转换为索引
data = {'a': 30, 'b': 70, 'c': 160, 'd': 5}
obj1 = pd.Series(data)
# print(obj1)
# 如果索引没有对应元素，则用NaN来填充（not a number）
index = ['a', 'b', 'c', 'd', 'e']
obj2 = pd.Series(data, index=index)
# print(obj2)

# isnull()和notnull()
# print(pd.isnull(obj2))
# print(pd.notnull(obj2))

# pandas操作data文件
data = pd.read_csv("ad.data", header=None)
# print(data.describe())
# print(data.columns)  # 获取所有列的名称
# print(data.dtypes)  # 返回所有列的实际数据类型
# print(data[1])  # 返回指定列
# print(data[[1, 20]])  # 返回多个列
# head()方法默认返回一个列的前5个元素 tail()默认返回后5个元素，可以写成head(n),tail(n),n为指定个数
print(data[1].head())
print(data[1].head(15))

