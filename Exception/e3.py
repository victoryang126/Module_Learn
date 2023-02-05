def decorator_example(func):
    print("Decorator called")

    def inner_function(*args, **kwargs):
        print("调用该函数")
        func(*args, **kwargs)
        print("函数的执行已经结束")
    return inner_function

@decorator_example
def some_function():
    print("正在执行函数")


def area_square(length):
    try:
        print(length**2)
    except TypeError:
        print("area_square只接受数字作为参数")


def area_circle(radius):
    try:
        print(3.142 * radius**2)
    except TypeError:
        print("area_circle只接受数字作为参数")


def area_rectangle(length, breadth):
    try:
        print(length * breadth)
    except TypeError:
        print("area_rectangle only takes numbers as the argument")


def exception_handler(func):
    def inner_function(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except TypeError:
            print(f"{func.__name__} only takes numbers as the argument")
    return inner_function


@exception_handler
def area_square(length):
    print(length * length)


@exception_handler
def area_circle(radius):
    print(3.14 * radius * radius)


@exception_handler
def area_rectangle(length, breadth):
    print(length * breadth)


area_square(2)
area_circle(2)
area_rectangle(2, 4)
area_square("some_str")
area_circle("some_other_str")
area_rectangle("some_other_rectangle")


# some_function()