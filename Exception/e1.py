

import functools
import logging
import sys

def exception_hook3(exc_type, exc_value, exc_traceback):
    logging.critical("Uncaught exception:", exc_info=(exc_type, exc_value, exc_traceback))


def func_monitor(func):

    try:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('call %s():' % func.__name__)
            # print('args = {}'.format(*args))
            return func(*args, **kwargs)
    except Exception as e:
        print("TT")
    return wrapper
a = [1,2]

@func_monitor
def p(lis):
    print("TT")
    print(lis[3])

sys.excepthook = exception_hook3



try:
    p(a)
except Exception as e:
    tb = e.__traceback__
    while tb:
        filename = tb.tb_frame.f_code.co_filename
        name = tb.tb_frame.f_code.co_name
        line_no = tb.tb_lineno
        print(f"File {filename} line {line_no}, in {name}")

        local_vars = tb.tb_frame.f_locals
        tb = tb.tb_next

    # print(e)
    # print(e.__traceback__.tb_frame.f_globals["__file__"])  # 发生异常所在的文件
    # # print(e.__traceback__.tb_frame.f_globals.keys())
    # # print(e.__traceback__.tb_frame.f_globals.values())
    # print(e.__traceback__.tb_frame.f_code.co_name)
    # print(e.__traceback__.tb_frame.f_code.co_filename)
    # print(e.__traceback__.tb_lineno)
    # local_vars = e.__traceback__.tb_frame.f_locals
    # print(local_vars)