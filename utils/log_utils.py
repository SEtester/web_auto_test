import logging.handlers
import time




class GetLogger():
    logger = None

    @classmethod
    def get_logger(cls):
        if cls.logger == None:
            # 日志器实例
            cls.logger = logging.getLogger()

            # 设置日志级别
            cls.logger .setLevel(level=logging.INFO)

            # 控制台处理器实例
            ch = logging.StreamHandler()

            # 以时间切分日志文件处理器
            filename = '../logs' + '/' + time.strftime('%Y%m%d') + 'WebUiTestLog.log'
            th = logging.handlers.TimedRotatingFileHandler(filename=filename, when='midnight', interval=1,
                                                           backupCount=30, encoding='utf-8')

            # 设置日志格式
            fmt = "%(asctime)s %(levelname)s [%(name)s] [filename: %(filename)s - moudle: %(module)s - func: %(funcName)s  %(lineno)d line] - %(message)s"
            fm = logging.Formatter(fmt)

            # 将日志格式添加到处理器
            ch.setFormatter(fm)
            th.setFormatter(fm)

            # 将处理器添加到日志器
            cls.logger .addHandler(ch)
            cls.logger .addHandler(th)
        return cls.logger

if __name__ == '__main__':
    logger = GetLogger().get_logger()
    logger.info("info信息被执行")
    logger.error("error信息被执行")