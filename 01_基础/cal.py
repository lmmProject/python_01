import math   # 导入 math 模块

# 变量的定义，条件语句
a = 100
if a >= 0:
    print(math.pow(2, 32))
else:
    print(-a/2)

# 动态语言
a = a + 10.0
print(a)

a = 'abc'
b = a
a = 'xyz'
print(b)

# 整数的地板除//永远是整数，即使除不尽
print(10 // 3)
print(10 % 3)

# ASCII编码,大写字母A的编码是65，小写字母z的编码是122
print("获取字符串的整数表示ord():")
print(ord('a'))
print(chr(20013))
# 1个中文字符经过UTF-8编码后通常会占用3个字节
print(len('中'.encode('utf-8')))

# %运算符就是用来格式化字符串的
print('%2d-%02d' % (3,1))
print('%.2f' % 3.1425926)

r = 85/72
print('%.1f%%' % r)