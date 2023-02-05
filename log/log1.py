import logging

"""
当指定一个日志级别之后，会记录大于或等于这个日志级别的日志信息，小于的将会被丢弃，
 ==默认情况下日志打印只显示大于等于 WARNING 级别的日志。=="""
def test_logging():
    logging.debug('Python debug')
    logging.info('Python info')
    logging.warning('Python warning')
    logging.error('Python Error')
    logging.critical('Python critical')

# 打印日志级别
def test():
    logging.basicConfig(level=logging.DEBUG)
    logging.debug('Python debug')
    logging.info('Python info')
    logging.warning('Python warning')
    logging.error('Python Error')
    logging.critical('Python critical')
    logging.log(2,'test')



# test_logging()

# test()
# 日志信息记录到文件
def config_log_file():
    logging.basicConfig(filename='example.log', level=logging.DEBUG)
    logging.debug('This message should go to the log file')
    logging.info('So should this')
    logging.warning('And this, too')

def log_format():
    # logging.basicConfig(level=logging.DEBUG)
    # logging.basicConfig(format='%(levelname)s:%(message)s',level=logging.DEBUG)
    logging.basicConfig(format='%(asctime)s %(message)s',level=logging.DEBUG)
    logging.warning('is when this event was logged 1s.')
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    logging.warning('is when this event was logged.')
    logging.info('Doing something')
log_format()
