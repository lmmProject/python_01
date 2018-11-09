# Python提供了切片（Slice）操作符，能大大简化这种操作

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# 取前N个元素，也就是索引为0-(N-1)的元素，可以用循环：
r = []
n = 3
for i in range(n):
    r.append(L[i])

print(r)

# 切片操作
print(L[0:3])
print(L[:3])

L = list(range(100))
# 后十个
print(L[-10:])

# 前10个数，每两个取一个：
print(L[:10:2])

# 所有数，每5个取一个：
print(L[::5])

# 甚至什么都不写，只写[:]就可以原样复制一个list：

# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
