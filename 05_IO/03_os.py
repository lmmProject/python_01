import os
# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
print(os.name)
# 获取详细的系统信息uname()函数，在Windows上不提供
# print(os.uname())

print(os.environ)

# 查看当前目录的绝对路径:
print(os.path.abspath('.'))

# # 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
# >>> os.path.join('/Users/michael', 'testdir')
# '/Users/michael/testdir'
# # 然后创建一个目录:
# >>> os.mkdir('/Users/michael/testdir')
# # 删掉一个目录:
# >>> os.rmdir('/Users/michael/testdir')


# 小结
# Python的os模块封装了操作系统的目录和文件操作，要注意这些函数有的在os模块中，有的在os.path模块中。