"""
描述符类基于以下 3 个特殊方法，换句话说，这 3 个方法组成了描述符协议：
__set__(self, obj, type=None)：在设置属性时将调用这一方法（本节后续用 setter 表示）；
__get__(self, obj, value)：在读取属性时将调用这一方法（本节后续用 getter 表示）；
__delete__(self, obj)：对属性调用 del 时将调用这一方法。
其中，实现了 setter 和 getter 方法的描述符类被称为数据描述符；反之，如果只实现了 getter 方法，则称为非数据描述符。
实际上，在每次查找属性时，描述符协议中的方法都由类对象的特殊方法 __getattribute__() 调用（注意不要和 __getattr__() 弄混）。也就是说，每次使用类对象.属性（或者 getattr(类对象，属性值)）的调用方式时，都会隐式地调用 __getattribute__()，它会按照下列顺序查找该属性：
验证该属性是否为类实例对象的数据描述符；
如果不是，就查看该属性是否能在类实例对象的 __dict__ 中找到；
最后，查看该属性是否为类实例对象的非数据描述符
"""
#描述符类
# class revealAccess:
#     def __init__(self, initval = None, name = 'var'):
#         self.val = initval
#         self.name = name
#     def __get__(self, obj, objtype):
#         print("Retrieving",self.name)
#         return self.val
#     def __set__(self, obj, val):
#         print("updating",self.name)
#         self.val = val
# class myClass:
#     x = revealAccess(10,'var "x"')
#     y = 5
# m = myClass()
# print(m.x)
# print("#"*10)
# m.x = 20
# print("#"*10)
# print(m.x)
# print("#"*10)
# print(m.y)
class Student:
    def __init__(self, name):
        self.name = name
# ，通过property装饰的函数，如例子中的 math 会变成 Student 实例的属性。而对 math 属性赋值会进入 使用 math.setter 装饰函数的逻辑代码块
    @property
    def math(self):
        return self._math

    @math.setter
    def math(self, value):
        if 0 <= value <= 100:
            self._math = value
        else:
            raise ValueError("Valid value must be in [0, 100]")
std = Student("v")
# std.math = 12
print(std.__dict__)
std.math = 12
print(std.__dict__)