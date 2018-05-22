# 在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)
# print(fact(100))

# 利用递归函数移动汉诺塔:
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

move(4, 'A', 'B', 'C')