import logging
import colorlog
import traceback

class Log:
    def __init__(self, name=None, log_level=logging.DEBUG,mode = "a"):
        # 获取logger对象
        self.logger = logging.getLogger(name)

        # 指定最低日志级别：（critical > error > warning > info > debug）
        self.logger.setLevel(log_level)

        # 日志格化字符串
        console_fmt = '%(log_color)s%(asctime)s-%(threadName)s-%(filename)s-[line:%(lineno)d]-%(levelname)s: %(message)s'
        file_fmt = '%(asctime)s-%(threadName)s-%(filename)s-[line:%(lineno)d]-%(levelname)s: %(message)s'

        # 控制台输出不同级别日志颜色设置
        color_config = {
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'purple',
        }

        console_formatter = colorlog.ColoredFormatter(fmt=console_fmt, log_colors=color_config)
        file_formatter = logging.Formatter(fmt=file_fmt)

        # 输出到控制台
        console_handler = logging.StreamHandler()
        # 输出到文件
        file_handler = logging.FileHandler(filename=name, mode='w', encoding='utf-8')

        # 设置日志格式
        console_handler.setFormatter(console_formatter)
        file_handler.setFormatter(file_formatter)

        # 处理器设置日志级别，不同处理器可各自设置级别，默认使用logger日志级别
        # console_handler.setLevel(logging.WARNING)
        file_handler.setLevel(logging.ERROR)  # 只有error和critical级别才会写入日志文件

        # logger添加处理器
        # 避免重复打印日志
        if not self.logger.handlers:
            self.logger.addHandler(console_handler)
            self.logger.addHandler(file_handler)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)
log = Log(name='log.txt', log_level=logging.WARNING)
def p_with_monitor(lis):
    try:
        print(lis[3])
    except Exception as e:
        # print(traceback.format_exc())
        log.critical("Critical")
        # log.critical(traceback.format_exc())
        # analyze_exception()
if __name__ == '__main__':
    # 控制台只会显示warning及以上级别日志信息，而log.txt文件中则会记录error及以上级别日志信息
    log.critical("CR")
    # a = [1, 2]
    #
    # p_with_monitor(a[3])


