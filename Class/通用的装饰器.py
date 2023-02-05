# 通用的装饰器
def decorator(func):
    # 内部函数
    def inner(*args, **kwargs):
        # 在内部函数里面对需要装饰的函数进行装饰
        print('call %s():' % func.__name__)
        # print('args = {}'.format(*args))
        # print('args = {}'.format(**kwargs))
        print("在内部函数里面对需要装饰的函数进行装饰：" + str(func))
        # 真正执行需要装饰的函数的地方：func(*args, **kwargs)哪个函数需要装饰就去执行哪个函数的代码
        result = func(*args, **kwargs)
        return result

    # 外部函数返回内部函数
    return inner


# 不带参数的需要装饰的函数
@decorator
def work():
    print("不带参数的函数")


# 带参数的需要装饰的函数
@decorator
def add_num(a, b):
    print(a + b)


# 带返回值的需要装饰的函数
@decorator
def add(a, b):
    return a + b


if __name__ == '__main__':
    # work()
    add_num(8, 4)
    num = add(a=2, b=5)
    print(num)