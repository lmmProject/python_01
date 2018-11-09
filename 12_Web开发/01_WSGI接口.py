# 正确的做法是底层代码由专门的服务器软件实现，我们用Python专注于生成HTML文档。
# 因为我们不希望接触到TCP连接、HTTP原始请求和响应格式，
# 所以，需要一个统一的接口，让我们专心用Python编写Web业务。

# 这个接口就是WSGI：Web Server Gateway Interface。

# WSGI接口定义非常简单，它只要求Web开发者实现一个函数，就可以响应HTTP请求。
# 我们来看一个最简单的Web版本的“Hello, web!”：
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']
# 上面的application()函数就是符合WSGI标准的一个HTTP处理函数，它接收两个参数：
# environ：一个包含所有HTTP请求信息的dict对象；
# start_response：一个发送HTTP响应的函数。


# Python内置了一个WSGI服务器，这个模块叫wsgiref，它是用纯Python编写的WSGI服务器的参考实现。
# 所谓“参考实现”是指该实现完全符合WSGI标准，但是不考虑任何运行效率，仅供开发和测试使用。

# 如果你觉得这个Web应用太简单了，可以稍微改造一下，
# 从environ里读取PATH_INFO，这样可以显示更加动态的内容：
def application1(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]


# 从wsgiref模块导入:
from wsgiref.simple_server import make_server

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 8000, application1)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()

# 小结
# 无论多么复杂的Web应用程序，入口都是一个WSGI处理函数。
# HTTP请求的所有输入信息都可以通过environ获得，
# HTTP响应的输出都可以通过start_response()加上函数返回值作为Body。
#
# 复杂的Web应用程序，光靠一个WSGI函数来处理还是太底层了，
# 我们需要在WSGI之上再抽象出Web框架，进一步简化Web开发。

