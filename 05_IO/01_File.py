# 本章的IO编程都是同步模式，异步IO由于复杂度太高，
# 后续涉及到服务器端程序开发时我们再讨论。

# f = open('c:/lonfile.txt')
# print(f.read())
# f.close()

# try:
#     f = open('c:/lonfile.txt')
#     print(f.read())
# finally:
#     if f:
#         f.close()

# 但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()
with open('c:/lonfile.txt', 'r') as f:
     # print(f.read())
    # 如果不能确定文件大小，反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便：
    for line in f.readlines():
        print(line.strip())# 把末尾的'\n'删掉



# 除了file外，还可以是内存的字节流，网络流，自定义流等等。
# file-like Object不要求从特定类继承，只要写个read()方法就行。
# StringIO就是在内存中创建的file-like Object，常用作临时缓冲。

# 要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：
with open('c:/lonfile.txt', 'r', encoding = 'gbk', errors = 'ignore') as f:
    for line in f.readlines():
        print(line.strip())

# 以'w'模式写入文件时，如果文件已存在，会直接覆盖（相当于删掉后新写入一个文件）。
# 如果我们希望追加到文件末尾怎么办？可以传入'a'以追加（append）模式写入。
with open('c:/lonfile.txt', 'a') as f:
    f.write('小狗')