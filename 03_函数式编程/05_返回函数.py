# 可以返回函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1, 3, 5, 7 , 9)
# 输出结果是一个函数<function lazy_sum.<locals>.sum at 0x0000000002F6A620>
# 每次都是一个新函数
print(f)


 
# 闭包

# 在这个例子中，我们在函数lazy_sum中又定义了函数sum，
# 并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，
# 这种称为“闭包（Closure）”的程序结构拥有极大的威力。


# 注意到返回的函数在其定义内部引用了局部变量args，
# 所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，
# 所以，闭包用起来简单，实现起来可不容易。

# 另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行。我们来看一个例子：
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs
# 全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。
# 等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
f1 = count()[0]()
f2 = count()[1]()
f3 = count()[2]()
print(f1)
print(f2)
print(f3)

# 重要
#  返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。

def count2():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs

f1 = count2()[0]()
f2 = count2()[1]()
f3 = count2()[2]()
print(f1)
print(f2)
print(f3)