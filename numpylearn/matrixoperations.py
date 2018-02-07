"""
矩阵的运算
create by swm
2018/02/07
"""

import numpy as np
x = np.array([[1, 2], [3, 4]], dtype=np.float64)
y = np.array([[5, 6], [7, 8]], dtype=np.float64)
print(x + y)
print(np.add(x, y))

print(x - y)
print(np.subtract(x, y))
# 元素逐个相乘
print(x*y)
print(np.multiply(x, y))

print(x/y)
print(np.divide(x, y))

print(np.sqrt(x))

# 矩阵乘法
v = np.array([9, 10])
w = np.array([11, 12])

print(np.dot(v, w))
# 矩阵转置
print(np.multiply(v, v.T))