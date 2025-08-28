import numpy as np

# # 首先创建结构化数据类型
# dt = np.dtype([('age',np.int8)]) 
# print(dt)
# [('age', 'i1')]

# 将数据类型应用于 ndarray 对象
# dt = np.dtype([('age',np.int8)]) 
# a = np.array([(10,),(20,),(30,)], dtype = dt) 
# print(a)
# [(10,) (20,) (30,)]

# dt = np.dtype([('age','i4'), ('score', float)])
# x = np.array([(14,33),(15,55),(19,22)], dtype=dt)
# print(x)
# [(14, 33.) (15, 55.) (19, 22.)]