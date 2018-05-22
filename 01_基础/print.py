#转义字符
#\n换行 \t制表符 \\就是\
print('I\'m \"OK"!')
print('I\'m learing\npython\\')

#用'''...'''的格式表示多行内容,如下在控制台中输入
# print('''line1
# ... line2
# ... line3''')
# line1
# line2
# line3

#如果在.py文件中
print(r'''hello,
world,
hello,
python''')

print(True and False)
print(5>3 and 3>1)
print(not True)

#空值是Python里一个特殊的值，用None表示。
# None不能理解为0，因为0是有意义的，而None是一个特殊的空值。
print(None)
