# MixIn
# 在设计类的继承关系时，通常，主线都是单一继承下来的，
# 例如，Ostrich继承自Bird。但是，如果需要“混入”额外的功能，通过多重继承就可以实现，
# 比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。

# class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
#     pass

# 小结
# 由于Python允许使用多重继承，因此，MixIn就是一种常见的设计。


class Student(object):
    def __init__(self, name):
        self.name = name

print(Student('Michael'))

class Student1(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name

print(Student1('Michael'))

# 显示变量调用的是__repr__()
# 两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串
# __repr__()是为调试服务的
s = Student1('Michael')
print(s)



# __iter__()方法，该方法返回一个迭代对象，
# 然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，
# 直到遇到StopIteration错误时退出循环
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:
            raise StopIteration()
        return self.a

for n in Fib():
    print(n)


# print(Fib()[5])
# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
class Fib1(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a+b
        return a

print(Fib1()[5])

# print(Fib1()[5:10])
# 对于Fib却报错。原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice
# 要正确实现一个__getitem__()还是有很多工作要做的



# __getattr__
# 正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。
class Student1(object):
    def __init__(self):
        self.name = 'Michael'
    def __getattr__(self, attr):
        if attr == 'score':
            return 99

s = Student1()
print(s.name)
print(s.score)

# 返回函数也是完全可以的：
class Student2(object):
    def __getattr__(self, attr):
        if attr == 'age':
            return lambda : 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)


# __call__
# 一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用instance.method()来调用
class Student3(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

s3 = Student3('Michael')
s3()



# 小结
# Python的class允许定义许多定制方法，可以让我们非常方便地生成特定的类。