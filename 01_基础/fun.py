# 绝对值的函数abs
print(abs(-20))

print(max(2, 5, 1, 30))

# 数据类型转换
int('123')
float('12.34')
str(100)
print(bool(1))
print(bool('1'))
print(bool(''))
print(bool(None))

# 函数对象的引用
a = abs
print(a(-1))


# 函数的定义
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-9))


# pass作为占位符，让代码能运行起来
age = 22
if age >= 18:
    pass


# 数据类型检查可以用内置函数isinstance()实现
def my_abs1(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


# my_abs1('A')


# Python的函数返回多值其实就是返回一个tuple，但写起来更方便。

# 小结
# 定义函数时，需要确定函数名和参数个数；
# 如果有必要，可以先对参数的数据类型做检查；
# 函数体内部可以用return随时返回函数结果；
# 函数执行完毕也没有return语句时，自动return None。
# 函数可以同时返回多个值，但其实就是一个tuple

import math

print(math.sqrt(2))


def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(5, 3))


# 默认参数,最大的好处是能降低调用函数的难度
def power1(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power1(5))


# 默认参数必须指向不变对象！None是不变的对象，而[]是一个可变的对象
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


print(add_end())


# Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return print(sum)


calc(1, 2)

nums = [1, 2, 3]
calc(nums[0], nums[1], nums[2])
# *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见
calc(*nums)


# 关键字参数有什么用？它可以扩展函数的功能。
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，
# kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)


# 我们希望检查是否有city和job参数
def person1(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        pass
    print('name:', name, 'age:', age, 'other:', kw)


# 但是调用者仍可以传入不受限制的关键字参数
person1('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)


# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。
def person2(name, age, *, city, job):
    print(name, age, city, job)


# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
person2('Jack', 24, city='Beijing', job='Engineer')
# Python解释器把这4个参数均视为位置参数
# person2('Jack', 24, city='Beijing', job='Engineer', zipcode=123)
person2('Jack', 24, job='Engineer', city='Beijing')

# 注意 ，如果缺少*，Python解释器将无法识别位置参数和命名关键字参数

# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
# 这5种参数都可以组合使用。
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
