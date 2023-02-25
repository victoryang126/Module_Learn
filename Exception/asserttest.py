"""
Python assert（断言）用于判断一个表达式，在表达式条件为 false 的时候触发异常。
断言可以在条件不满足程序运行的情况下直接返回错误，而不必等待程序运行后出现崩溃的情况，例如我们的代码只能在 Linux 系统下运行，可以先判断当前系统是否符合条件
assert expression
等价于：
if not expression:
    raise AssertionError
"""
assert 1==1    # 条件为 true 正常执行
assert 1==2    # 条件为 false 触发异常
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# AssertionErro
assert 1==2, '1 不等于 2'