
#有序的list
classmates = ['张三', '李四']

print('%s%d' % ('list集合长度：', len(classmates)))
print('{0}{1}'.format('list集合长度：', len(classmates)))

#最后一个元素的索引是len(classmates) - 1
#如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素
print(classmates[-1])
# 以此类推，可以获取倒数第2个、倒数第3个：
print(classmates[-2])
# IndexError: list index out of range
# print(classmates[-3])



classmates.append("李四新")
print(classmates)
classmates.pop()
print(classmates)

# 有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
t = (1,2)
print(t)

#"可变的"tuple
#实际上变化的是，list内的元素，而对于tuple来说，所指向的list并没有变
t = ('a', 'b', ['A', 'B'])
print(t)
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)


