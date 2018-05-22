# metaclass
# 除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。

# 先定义metaclass，就可以创建类，最后创建实例

# metaclass是Python面向对象里最难理解，也是最难使用的魔术代码。
# 正常情况下，你不会碰到需要使用metaclass的情况，所以，以下内容看不懂也没关系，因为基本上你不会用到。




# ORM就是一个典型的例子。
# 对象-关系映射，就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表

# 编写底层模块的第一步，就是先把调用接口写出来。
class User(Model):
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')



# 首先来定义Field类，它负责保存数据库表的字段名和字段类型：
class Field(object):
    def __init__(self, mame, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

# 在Field的基础上，进一步定义各种类型的Field，比如StringField，IntegerField等等：
class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

#下一步，就是编写最复杂的ModelMetaclass了：
class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mapping = dict()
        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = name  # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)

class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

# 在ModelMetaclass中，一共做了几件事情：
# 1.排除掉对Model类的修改；
# 2.在当前类（比如User）中查找定义的类的所有属性，如果找到一个Field属性，
#   就把它保存到一个__mappings__的dict中，同时从类属性中删除该Field属性，
#   否则，容易造成运行时错误（实例的属性会遮盖类的同名属性）；
# 3.把表名保存到__table__中，这里简化为表名默认为类名。

u = User(id = '12345', name = 'Michael', email = 'test@orm.org', password = 'my-pwd')
u.save()