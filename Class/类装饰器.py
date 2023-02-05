# 类装饰器
class MyDecorator(object):
    # 初始化需要装饰的函数
    def __init__(self, func):
        # 私有化func
        self.__func = func

    # 实现__call__方法；把类的实例对象变成一个可调用对象
    def __call__(self, *args, **kwargs):
        # 在__call__方法里面对需要装饰的函数进行装饰
        print("如果想说话")
        self.__func()


# 需要装饰的函数
# @MyDecorator => say = MyDecorator(say)
@MyDecorator
def say():
    print("大声的说出来")

class Warp(object):
    def __init__(self):
        pass

    def __call__(self, obj):
        obj.name = 'warp'
        return obj

@Warp()
def foo():
    pass

if __name__ == '__main__':
    say()
    print(foo.name)