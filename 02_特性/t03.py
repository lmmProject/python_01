# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
print(list(range(1, 11)))

print([x * x for x in range(1, 11)])

# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
print([x * x for x in range(1, 11) if x % 2 == 0])

# 还可以使用两层循环，可以生成全排列：
print([m + n for m in 'ABC' for n in 'XYZ'])

# 运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：
import os
print([d for d in os.listdir('.')])


d = {'x': 'A', 'y': 'B', 'z': 'c'}
print ([k + '=' + v for k, v in d.items()])
print ([k + '=' + v.lower() for k, v in d.items()])