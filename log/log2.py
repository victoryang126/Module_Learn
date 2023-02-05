import logging
from logging.handlers import RotatingFileHandler
from datetime import time
# 创建日志器对象
logger = logging.getLogger(__name__)
# logger2 = logging.getLogger(__name__)
# 设置logger可输出日志级别范围
logger.setLevel(logging.DEBUG)
# logger2.setLevel(logging.DEBUG)
# 添加控制台handler，用于输出日志到控制台
console_handler = logging.StreamHandler()
# 添加日志文件handler，用于输出日志到文件中
file_handler = logging.FileHandler(filename='log.log', encoding='UTF-8')
#log文件基于时间生成
tf_handler = logging.handlers.TimedRotatingFileHandler(filename = 't.log', when='M', interval=1, backupCount=0, encoding=None, delay=False, utc=False, atTime=None)

# 将handler添加到日志器中
logger.addHandler(console_handler)
# logger2.addHandler(console_handler)
logger.addHandler(file_handler)
logger.addHandler(tf_handler)
# 设置格式并赋予handler
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
formatter = logging.Formatter('%(asctime)s- %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)
tf_handler.setFormatter(formatter)
# 输出不同级别日志
# logger.debug("============【开始测试】====================")
# logger.info("============【开始测试】====================")
# logger.warning("============【开始测试】====================")
# logger.critical("============【开始测试】====================")
logger.error("============【开始测试】====================")
