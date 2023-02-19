

import functools
import logging
import sys
import traceback

def exception_hook3(exc_type, exc_value, exc_traceback):
    logging.critical("Uncaught exception:", exc_info=(exc_type, exc_value, exc_traceback))

def analyze_exception(e):
    tb = e.__traceback__
    # local_vars = e.__traceback__.tb_frame.f_locals
    # print(local_vars)
    while tb:
        filename = tb.tb_frame.f_code.co_filename
        name = tb.tb_frame.f_code.co_name
        line_no = tb.tb_lineno
        print(f"File {filename} line {line_no}, in {name}")
        tb = tb.tb_next

def func_monitor(func):


    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('call %s():' % func.__name__)
        # print('args = {}'.format(*args))
        ret = None
        try :
            # ret = func(*args, **kwargs)
            # print('finished  %s():' % func.__name__)
            return func(*args, **kwargs)
        except Exception as e:
            # pass
            # analyze_exception(e)
            print(traceback.format_exc())
            raise e
        # return ret

    return wrapper
a = [1,2]

@func_monitor
def p_with_monitor(lis):
    print(lis[3])


def p(lis):
    print(lis[3])

@func_monitor
def p_with_monitor2(lis):
    try:
        print(lis[3])
    except Exception as e:
        print("Function exception")
        print(traceback.format_exc())
# sys.excepthook = exception_hook3


p_with_monitor2(a)

print("#"*10)
p_with_monitor(a)
# try:
#     try:
#         c = p(a)
#     except Exception as e:
#         print(traceback.format_exc())
#         raise e
# except Exception as e:
#     # exc_type, exc_value, exc_traceback = sys.exc_info()
#     # print(exc_value)
#     # traceback.print_tb(exc_traceback)
#     # traceback.print_exception(exc_type, exc_value, exc_traceback, limit=None, file=sys.stdout)
#     print(traceback.format_exc())

# """
# print("#"*30)
# try:
#     c = p_with_monitor(a)
# except Exception as e:
#     print("#"*30)
    # exc_type, exc_value, exc_traceback = sys.exc_info()
    # print(exc_value)
    # traceback.print_tb(exc_traceback)
    # traceback.print_exception(exc_type, exc_value, exc_traceback, limit=None, file=sys.stdout)
    # print(traceback.format_exc())
# """
    # tb = e.__traceback__
    # # local_vars = e.__traceback__.tb_frame.f_locals
    # # print(local_vars)
    # while tb:
    #     filename = tb.tb_frame.f_code.co_filename
    #     name = tb.tb_frame.f_code.co_name
    #     line_no = tb.tb_lineno
    #     print(f"File {filename} line {line_no}, in {name}")

        # local_vars = tb.tb_frame.f_locals
        # tb = tb.tb_next

    # print(e)
    # print(e.__traceback__.tb_frame.f_globals["__file__"])  # 发生异常所在的文件
    # # print(e.__traceback__.tb_frame.f_globals.keys())
    # # print(e.__traceback__.tb_frame.f_globals.values())
    # print(e.__traceback__.tb_frame.f_code.co_name)
    # print(e.__traceback__.tb_frame.f_code.co_filename)
    # print(e.__traceback__.tb_lineno)
    # local_vars = e.__traceback__.tb_frame.f_locals
    # print(local_vars)