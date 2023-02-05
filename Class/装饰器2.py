"""
1. 装饰器功能特点

功能特点：

不修改已有函数的源代码
不修改已有函数的调用方式
给已有函数增加额外的功能

2. 装饰器语法糖写法

Python提供了一个装饰函数更加简单的写法，也就是装饰器语法糖写法，通过语法糖的方式也可以完成对已有函数的装饰

语法糖格式：

@装饰器名称

3. 装饰器使用的场景

函数执行时间的统计
日志记录
权限验证单
例模式竞争
资源管理
"""
import time
# 外部函数：定义装饰器：func：需要装饰的已有函数
def decorator(func):
    # 内部函数
    def inner():
        # 3. 在内部函数里面对已有函数添加额外功能
        print("登录验证通过")
        # 执行需要装饰的函数
        func()

    # 外部函数返回内部函数
    return inner


# 1. 不修改已有函数的源代码
def comment():
    print("发表评论")

# 装饰器的执行时机是在加载模块时立即执行，对需要装饰的函数进行装饰
# @decorator 是对comment = decorator(comment)进行了封装
@decorator
def comment_decorator():
    print("发表评论")

def execute_time(func):
    def inner():
        # 在内部函数对需要装饰的函数进行装饰
        # 执行目标函数之前的时间(这个时间是当前距离1970-1-1:0:0:1的时间差)
        start = time.time()
        # 执行目标函数
        func()
        # 执行目标函数之后的时间
        end = time.time()
        # 执行目标函数所需要的时间
        result = end - start
        # 输出日志信息
        print("执行work函数所需要的时间: ", result)

    return inner


@execute_time
def work():
    for i in range(10000):
        # print(i)
        pass
# 装饰器
def decorator_1(func):
    # 内部函数：装饰需要装饰的函数时，内部函数的类型要和需要装饰的函数的类型保持一致
    def inner(a, b):
        # 在内部函数对需要装饰的函数进行装饰
        print("现在计算的是：", a, "+", b)
        func(a, b)
    # 外部函数返回内部函数
    return inner


# 计算两个数之和
@decorator_1
def add_num(a, b):
    print(a + b) 

# 装饰器：这个装饰器也是通用的装饰器写法
def decorator_3(func):
    # 内部函数：内部函数的类型和需要装饰的函数的类型保持一致
    def inner(*args, **kwargs):
        num = func(*args, **kwargs)
        return num
    return inner

@decorator_3
def add_num_3(*args, **kwargs):
    num = 0

    # args：元组类型
    for value in args:
        num += value

    # kwargs：字典类型，
    for value in kwargs.values():
        num += value
    return num

if __name__ == '__main__':
    # 调用装饰器对已有函数进行装饰: comment = inner，此时comment是内部函数的实例
    # comment = decorator(comment)
    # 2. 不修改已有函数的调用方式
    # comment()：相当于调用内部函数inner()
    # comment()
    # comment_decorator()
    # work()
    # add_num(1,2)
    result1 = add_num_3(1, 3, 5)
    print(add_num_3.__name__)
    print("result1: ", result1)
    result2 = add_num_3(a=3, b=1)
    print("result2: ", result2)