import logging
import colorlog
"""
%(asctime)s
表示人类易读的 LogRecord 生成时间。 默认形式为 '2003-07-08 16:49:45,896' （逗号之后的数字为时间的毫秒部分
%(created)f
LogRecord 被创建的时间（即 time.time() 的返回值）

%(filename)s
pathname 的文件名部分。
%(funcName)s
函数名包括调用日志记录.

%(levelname)s
消息文本记录级别（'DEBUG'，'INFO'，'WARNING'，'ERROR'，'CRITICAL'）

%(levelno)s
消息数字的记录级别 (DEBUG, INFO, WARNING, ERROR, CRITICAL).

%(lineno)d
发出日志记录调用所在的源行号（如果可用）。

%(message)s
记入日志的消息，即 msg % args 的结果。 这是在发起调用 Formatter.format() 时设置的。
%(module)s
模块 (filename 的名称部分)。

%(name)s
用于记录调用的日志记录器名称。
%(pathname)s
发出日志记录调用的源文件的完整路径名（如果可用）。
%(process)d
进程ID（如果可用）
%(processName)s
进程名（如果可用）
%(thread)d
线程ID（如果可用）
%(threadName)s
线程名（如果可用）
"""
# 创建日志器对象
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# 设置handler
console_handler = logging.StreamHandler()

# 添加处理器
logger.addHandler(console_handler)

# 设置格式
# formatter = logging.Formatter('%(asctime)s  %(created)f  %(name)s  %(levelname)s  %(filename)s  %(funcName)s  '
#                               '%(levelno)s  %(lineno)d  %(module)s  %(msecs)d  %(pathname)s  %(process)d  '
#                               '%(processName)s  %(relativeCreated)d  %(thread)d  %(threadName)s  %(message)s')

formatter = logging.Formatter('%(asctime)s  %(levelname)s  %(filename)s  %(funcName)s  '
                              ' %(lineno)d  %(module)s   %(pathname)s '
                              '  %(message)s')
color_config = {
    'DEBUG': 'black',
    'INFO': 'green',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'red',
}
# console_fmt = '%(log_color)s%(asctime)s-%(threadName)s-%(filename)s-[line:%(lineno)d]-%(levelname)s: %(message)s'
console_fmt = '%(log_color)s%(asctime)s-%(levelname)s-%(filename)s %(funcName)s -[line:%(lineno)d]-s %(module)s  %(pathname)s: %(message)s'
# console_fmt = '%(log_color)\s%(asctime)s  %(levelname)s  %(filename)s  %(funcName)s  %(lineno)d %(module)s  %(pathname)s  %(message)s'
console_formatter = colorlog.ColoredFormatter(fmt=console_fmt, log_colors=color_config)
console_handler.setFormatter(console_formatter)
# formatter = logging.Formatter('${name} - ${levelname} - ${message}', style='$')
# formatter = logging.Formatter('{name} - {levelname} - {message}', style='{')


if __name__ == '__main__':
    # 输出日志记录
    logger.debug("============【开始测试】====================")
    logger.info("============【开始测试】====================")
    logger.warning("============【开始测试】====================")
    logger.error("============【开始测试】====================")
    logger.critical("============【开始测试】====================")
