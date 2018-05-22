import pickle
d = dict(name='Bob', age=20, score=88)
f = open('c:/lonfile.txt', 'wb')
pickle.dump(d, f)
f.close()

# 反序列化
f = open('c:/lonfile.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)


# Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。我们先看看如何把Python对象变成一个JSON：
import json
d = dict(name = 'mmli3', age = 24, score = 99)
print(json.dumps(d))
# dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object。

# file-like Object中读取字符串并反序列化：
son_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(son_str))