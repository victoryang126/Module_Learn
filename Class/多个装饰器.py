# 第二层装饰器
def second_decorator(func):
    print("我是第二层装饰器")

    def second_inner():
        func()

    return second_inner


# 第一个层装饰器
def first_decorator(func):
    print("我是第一层装饰器")

    def first_inner():
        func()

    return first_inner


"""
需要装饰的函数
多个装饰器装饰同一个函数时，先执行内部的装饰器，然后再执行外部的装饰器，是一个由内到外的装饰过程
原理：content = second_decorator(first_decorator(content))
执行步骤:
1. content = first_decorator(content)，内部装饰器完成后：content = first_inner
2. content = second_decorator(fist_decorator.first_inner)，外部装饰器完成后：content = second_inner
3. 调用content()：
4. 调用second_inner()
5. 调用second_inner.func()：func是由第二层装饰器second_decorator传入的first_inner
6. 调用first_inner()
7. 调用first_inner.func()：func是由第一层装饰器first_decorator传入的content
8. 调用真正的content()函数
9. 把content()的结果返回给first_inner().func()
10. 把first_inner().func()拿到的结果返回给second_inner().func()
11. 最后把second_inner().func()拿到的结果返回给调用content()的地方
前1，2步骤是加载模块时立即执行的
"""


@second_decorator
@first_decorator
def content():
    print("我是需要装饰的函数")


if __name__ == '__main__':

    content()