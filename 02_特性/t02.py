# 迭代dict
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

# 迭代字符串
for ch in 'ABC':
    print(ch)

# 如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：
from collections import Iterable

print(isinstance('abc', Iterable))
print(isinstance(123, Iterable))

# Python内置的enumerate函数可以把一个list变成索引-元素对
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)