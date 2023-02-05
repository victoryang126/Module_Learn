import sys

def exception_hook(exc_type, exc_value, tb):
    print('Traceback:')
    filename = tb.tb_frame.f_code.co_filename
    name = tb.tb_frame.f_code.co_name
    line_no = tb.tb_lineno
    print(f"File {filename} line {line_no}, in {name}")

    # Exception type 和 value
    print(f"{exc_type.__name__}, Message: {exc_value}")


"""
由上面的例子可以看出，traceback对象(tb)本质上是一个链表 - 存储着所有出现的exceptions。因此可以使用tb_next对tb进行遍历，并打印每一个异常的信息。在此基础上，还可以使用tb_frame.f_locals属性将变量输出到console中，这有助于调试代码。

使用traceback对象输出异常信息是可行的，但是比较麻烦，此外输出的信息可读性较差。更方便的做法是使用traceback模块，该模块内置了许多提取异常信息的辅助函数
"""
def exception_hook2(exc_type, exc_value, tb):

    local_vars = {}
    while tb:
        filename = tb.tb_frame.f_code.co_filename
        name = tb.tb_frame.f_code.co_name
        line_no = tb.tb_lineno
        print(f"File {filename} line {line_no}, in {name}")

        local_vars = tb.tb_frame.f_locals
        tb = tb.tb_next
    print(f"Local variables in top frame: {local_vars}")

import logging
logging.basicConfig(
    level=logging.CRITICAL,
    format='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
    datefmt='%H:%M:%S',
    stream=sys.stdout
)

def exception_hook3(exc_type, exc_value, exc_traceback):
    logging.critical("Uncaught exception:", exc_info=(exc_type, exc_value, exc_traceback))

# sys.excepthook = exception_hook2



def do_stuff():
    # 写一段会产生异常的代码
    raise ValueError("Some error message")

do_stuff()