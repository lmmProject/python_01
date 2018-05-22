# 静态语言 vs 动态语言
# 对于静态语言（例如Java）来说，如果需要传入Animal类型，
# 则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。

# 对于Python这样的动态语言来说，则不一定需要传入Animal类型。
# 我们只需要保证传入的对象有一个run()方法就可以了：


class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')


class Timer(object):
    def run(self):
        print('Start...')


class Cat(Timer):
    def run(self):
        print('Cat is running...')


dog = Dog()
cat = Cat()

print(dog.run())
print(cat.run())
