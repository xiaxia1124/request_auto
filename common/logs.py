import os, time, logging
import colorlog


class Log(object):
    """
    log日志类
    """

    def __init__(self):
        # 日志存放目录
        log_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'logs')
        # 如果不存在这个logs文件夹，则自动创建
        if not os.path.exists(log_path):
            os.mkdir(log_path)
        # 在日志路径下添加日志文件名
        self.logname = os.path.join(log_path, '%s.log' % time.strftime('%Y_%m_%d'))
        # logger日志对象初始化
        self.logger = logging.getLogger()
        # 设置日志等级
        self.logger.setLevel(logging.DEBUG)
        # 日志输出格式
        self.formatter = logging.Formatter('\n[%(asctime)s]-%(levelname)s:%(message)s')
        # 自定义颜色输出格式
        # self.formatter = colorlog.ColoredFormatter('%(log_color)s[%(asctime)s]-%(levelname)s:%(message)s',
        #                                                  log_colors={
        #                                                      'DEBUG': 'cyan',
        #                                                      'INFO': 'green',
        #                                                      'WARNING': 'yellow',
        #                                                      'ERROR': 'red'
        #                                                  })

    def __console(self, level, message):
        # 创建一个FileHandler用于写到本地
        fh = logging.FileHandler(self.logname, 'a', 'utf-8')
        # 设置日志等级
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)
        # 创建一个StreamHandler用于输出控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)
        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        # 为了避免日志输入重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        fh.close()

    def debug(self, message):
        self.__console('debug', message)

    def info(self, message):
        self.__console('info', message)

    def warning(self, message):
        self.__console('warning', message)

    def error(self, message):
        self.__console('error', message)