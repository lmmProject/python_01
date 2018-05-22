# StringIO顾名思义就是在内存中读写str。

from io import StringIO
f = StringIO()
f.write('hello')
f.write(' world')
print(f.getvalue())

f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

# StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。

from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
# 请注意，写入的不是str，而是经过UTF-8编码的bytes。