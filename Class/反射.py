# 通过字符串操作对象或者模块的成员（属性、方法），基于字符串驱动的，可以反射的对象包含:
"""
1、反射类中的变量 : 静态属性,类方法，静态方法
2、反射对象中的变量、对象属性、普通方法
3、反射模块中的变量
4、反射本文件中的变量
def getattr(__o: object, __name: str, __default: None) -> Any | None: ...
获取对象或者类或者模块中是否有某个属性，可以设置默认值
def hasattr(__obj: object, __name: str) -> bool: ...
判断对象或者类或者模块中是否存在某个属性，返回布尔值
def setattr(__obj: object, __name: str, __value: Any) -> None: ...
设置对象或者类或者模块中某个属性（方法也可以）的值
def delattr(__obj: object, __name: str) -> None: ...
删除对象或者类或者模块中属性或方法
"""
class Test:

    name = "mike"

    def __init__(self, name) -> None:
        self.name = name

    def run(self):
        print("run")

    @staticmethod
    def static_method():
        print("static_method")

    @classmethod
    def class_method(cls):
        print("class_method")


# 获取类属性
print(getattr(Test, "name", None))
# 获取静态方法
print(getattr(Test, "static_method", None))
print(getattr(Test, "static_method", None)())
# 获取类方法
print(getattr(Test, "class_method", None))
print(getattr(Test, "class_method", None)())

t = Test("tom")
# 获取对象中的属性
print(getattr(t, "name", None))
# 设置对象中的属性
setattr(t, "age", 18)
print(getattr(t, "age", None))
# 删除对象中的属性
delattr(t, "name")
# 判断是否存在属性
print(hasattr(t, "name"))
print(getattr(t, "name", None))
# 获取对象中的实例方法
print(getattr(t, "run", None))
print(getattr(t, "run", None)())

# import sys
#
# number = 1
# print(hasattr(sys.modules[__name__], "number"))