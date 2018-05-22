# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
# 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），
# 只有内部可以访问，外部不能访问。

class Student(object):
    # 变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，
    # 是特殊变量，特殊变量是可以直接访问的，不是private变量，
    # 所以，不能用__name__、__score__这样的变量名。
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))


bart = Student('Bart Simpson', 59)

# “虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”
# dos中可以通过bart._Student__name访问
print(bart._Student__name)
