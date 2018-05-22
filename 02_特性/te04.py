# 我们创建了一个generator后，基本上永远不会调用next()，
# 而是通过for循环来迭代它，并且不需要关心StopIteration的错误。
g = (x * x for x in range(10))
for n in g:
    print(n)

# 斐波拉契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易：
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a+b
        n = n + 1
    return 'done'

# 注意，赋值语句：

# a, b = b, a + b
# 相当于：

# t = (b, a + b) # t是一个tuple
# a = t[0]
# b = t[1]

fib(6)


# generator是非常强大的工具，
# 在Python中，可以简单地把列表生成式改成generator，也可以通过函数实现复杂逻辑的generator。
# 要理解generator的工作原理，它是在for循环的过程中不断计算出下一个元素，并在适当的条件结束for循环。
# 对于函数改成的generator来说，遇到return语句或者执行到函数体最后一行语句，就是结束generator的指令，
# for循环随之结束。