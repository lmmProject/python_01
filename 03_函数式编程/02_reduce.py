# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
# 这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算

from functools import reduce
def add(x, y):
    return x + y

print(reduce(add, [1, 2, 3]))


DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))


print(str2int('1234'))

# 还可以用lambda函数进一步简化成：
def char2num(s):
    return DIGITS[s]
def strtoint(s):
    return reduce(lambda x, y: x*10 + y, map(char2num, s))

print(strtoint('123'))