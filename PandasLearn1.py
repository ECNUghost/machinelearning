import pandas as pd
import numpy as np
import random

data = pd.read_csv("ad.data", header=None)
# print(data[1: 3])
# print(data[(data[1]> 0) & (data[1558]=='ad.')].head(4))
# print(data.ix[:3])
# print(data.iloc[:3])
# print(data.loc[:3])

# 增加新列与删除新列
# data['newcolumn'] = 'test value'
# print(data.columns)
# data = data.drop('newcolumn', 1)
# print(data.columns)

#duplicated 可以判断每一行是否对其他行重复
# print(data.duplicated())
#drop_duplicates 返回去重后的剩余元素
# print(data[1558].drop_duplicates())
# print(data[1558].head(461))
# 还可以将上述结果转换成list
# print(data[1558].drop_duplicates().tolist())
# 把标签转换为数值
# adindices = data[data.columns[-1]] == 'ad.'
# data.loc[adindices, data.columns[-1]] = 1
# nonadindices = data[data.columns[-1]] == 'nonad.'
# data.loc[nonadindices, data.columns[-1]] = 0
# print(data[1558].dtypes)
# 将标签列转换为浮点型
# data[data.columns[-1]] = data[data.columns[-1]].astype(float)
# print(data[1558])
# 用replace替换所有的？实例
# data = data.replace({'?': np.nan})
# data = data.replace({' ?': np.nan})
# data = data.replace({'  ?': np.nan})
# data = data.replace({'   ?': np.nan})
# data = data.replace({'    ?': np.nan})
# data = data.replace({'     ?': np.nan})
# 在包含缺失数据的单元格填充常量-1
# data = data.fillna(-1)
# print(data)

#拼接两个DataFrame对象
data1 = pd.DataFrame(columns=[i for i in range(1559)])
data1.loc[len(data1)] = [random.randint(0, 1) for r in range(1558)] + [1]
data1.loc[len(data1)] = [random.randint(0, 1) for r in range(1558)] + [1]
print(len(data))
datatot = pd.concat([data[:], data1[:]])
print(len(datatot))

