import logging


class GlobalLogger(object):

    class __LoggerObject(object):

        def __init__(self, logger_name, level):

            self.logger_name = logger_name
            self.level = level
            self.logger = None

        def get_logger(self):
            if not self.logger:
                level_map = {"DEBUG": logging.DEBUG,
                             "WARNING": logging.WARNING,
                             "INFO": logging.INFO,
                             "ERROR": logging.ERROR}
                log_level = level_map.get(self.level, logging.DEBUG)
                self.logger = logging.getLogger(self.logger_name)
                self.logger.setLevel(log_level)
                formatter = logging.Formatter('%(asctime)s - %(name)s - %(pathname)s[line:%(lineno)d]'
                                              ' - %(levelname)s: %(message)s')
                ch = logging.StreamHandler()
                ch.setLevel(log_level)
                ch.setFormatter(formatter)
                self.logger.addHandler(ch)
            return self.logger

    instance = None

    def __new__(cls, logger_name, level):

        if cls.instance is None:
            cls.instance = cls.__LoggerObject(logger_name, level)
        return cls.instance
