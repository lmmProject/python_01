# 匿名函数

# 当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便。

print(list(map(lambda x: x*x, [1, 2, 3, 4, 5])))


# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
f = lambda x : x*x
print(f)
print(f(5))



#装饰器

# 假设我们要增强now()函数的功能，
# 比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
# 这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。


# 本质上，decorator就是一个返回函数的高阶函数。
# 所以，我们要定义一个能打印日志的decorator，可以定义如下：
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

# 观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。
# 我们要借助Python的@语法，把decorator置于函数的定义处：
@log
def now():
    print('2015-3-25')

now()

# wrapper()函数的参数定义是(*args, **kw)，
# 因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，首先打印日志，再紧接着调用原始函数。


# 以上两种decorator的定义都没有问题，但还差最后一步。
# 因为我们讲了函数也是对象，它有__name__等属性，但你去看经过decorator装饰之后的函数，
# 它们的__name__已经从原来的'now'变成了'wrapper'：

# >>> now.__name__
# 'wrapper'
# 因为返回的那个wrapper()函数名字就是'wrapper'，
# 所以，需要把原始函数的__name__等属性复制到wrapper()函数中，
# 否则，有些依赖函数签名的代码执行就会出错。

# 不需要编写wrapper.__name__ = func.__name__这样的代码，
# Python内置的functools.wraps就是干这个事的，所以，一个完整的decorator的写法如下：

# 针对带参数的decorator：
import functools
def log_fts(text):
    def decotator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decotator


def now2():
    print('2015-3-25')

now2 = log_fts('自定义log文本')(now2)
now2()



# 偏函数

# 在介绍函数参数的时候，
# 我们讲到，通过设定参数的默认值，可以降低函数调用的难度。而偏函数也可以做到这一点。举例如下：

# int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换：
print(int('12345'))

print(int('1000000', base=2))

def int2(x, base = 2):
    return int(x, base)
print(int2('1000000'))

# functools.partial就是帮助我们创建一个偏函数的，
# 不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：
import functools
int_two = functools.partial(int, base=2)
print(int_two('1000000'))


# 当传入：

max2 = functools.partial(max, 10)
# 实际上会把10作为*args的一部分自动加到左边，也就是：

f1 = max2(5, 6, 7)
print(f1)
# 相当于：

args = (10, 5, 6, 7)
f2 = max(*args)
print(f2)
# 结果为10。
# 偏函数小结
# 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，
# 这个新函数可以固定住原函数的部分参数，从而在调用时更简单。


