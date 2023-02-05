import functools


def log(func):
    def wrapper(*args, **kwargs):
        print('call %s():' % func.__name__)
        # print('args = {}'.format(*args))
        return func(*args, **kwargs)

    # print("finished")
    return wrapper
"""
值得注意的是@functools.wraps(func)，这是python提供的装饰器。它能把原函数的元信息拷贝到装饰器里面的 func 函数中
。函数的元信息包括docstring、name、参数列表等等。可以尝试去除@functools.wraps(func)
，你会发现test.__name__的输出变成了wrapper"""

@log
def test(p,a):
    # print(test.__name__ + " param: " + p)
    return p,a
test("I'm a param","T")
# print(test.__name__)
def log_with_param(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('call %s():' % func.__name__)
            print('args = {}'.format(*args))
            print('log_param = {}'.format(text))
            return func(*args, **kwargs)

        return wrapper

    return decorator

@log_with_param("param")
def test_with_param(p):
    print(test_with_param.__name__)
#

# test_with_param("TT")