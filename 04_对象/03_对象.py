# 使用__slots__
# 只允许对Student实例添加name和age属性。
# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性
class Student(object):
    __slots__ = ('name', 'age')
    pass


s = Student()
s.name = 'hello'
s.age = 25
# 'Student' object has no attribute 'score'
# s.score = 99

# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的


# Python内置的@property装饰器就是负责把一个方法变成属性调用的：
class Student1(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100!')
        self._score = value


s1 = Student1()
s1.score = 60

print(s1.score)
# ValueError: score must between 0~100!
# s1.score = 999

# 注意到这个神奇的@property，我们在对实例属性操作的时候，就知道该属性很可能不是直接暴露的，
# 而是通过getter和setter方法来实现的。

# 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
class Student2(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth

    # 上面的birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来。
# 小结
# @property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，
# 这样，程序运行时就减少了出错的可能性。