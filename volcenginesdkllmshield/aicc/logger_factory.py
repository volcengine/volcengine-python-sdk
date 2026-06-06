import logging
import multiprocessing
import os
import sys

mutex = multiprocessing.Lock()


class Factory(object):
    @staticmethod
    def init(*args):
        """
        Initialize a global instance
        :param args:
        :return:
        """
        pass

    @staticmethod
    def get_global_instance():
        """
        Get the global instance
        :return:
        """
        pass

    @staticmethod
    def get_instance(*args):
        """
        Get an instance
        :param args:
        :return:
        """
        pass

    @staticmethod
    def _raise_value_error(invalid_type, invalid_value):
        """

        :param invalid_type: str
        :param invalid_value: str
        :return:
        """
        raise ValueError("invalid {}: {}".format(invalid_type, invalid_value))


class LoggerFactory(Factory):
    logger = None
    root_dir = ""
    task_logger_level = ""
    local_logger = {}

    @staticmethod
    def init():
        top_logger_level = os.getenv("TOP_LOGGER_LEVEL", "DEBUG").strip('"')
        log_path = os.getenv("LOGDIR", f"./jsc_log").strip('"')
        task_logger_level = os.getenv("TASK_LOGGER_LEVEL", "DEBUG").strip('"')

        LoggerFactory.task_logger_level = task_logger_level

        try:
            import bytedlogger

            bytedlogger.config_default()
            LoggerFactory.logger = logging.getLogger("top")
        except ImportError:
            LoggerFactory.logger = logging.getLogger("top")
        LoggerFactory.logger.setLevel(top_logger_level)

        if log_path is None or log_path == "":
            log_path = "/home/jeddak/log"
            print(f"Root logger path is not set, use log_path {log_path}")

        print(f"log_path: {log_path}")
        LoggerFactory.root_dir = log_path

        if not os.path.exists(log_path):
            os.makedirs(log_path)

        top_logger_path = os.path.join(log_path, "top.log")

        fh = logging.FileHandler(top_logger_path, mode="a")
        fh.setLevel(top_logger_level)
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s"
        )
        fh.setFormatter(formatter)
        LoggerFactory.logger.addHandler(fh)
        # LoggerFactory.logger.addHandler(logging.StreamHandler(sys.stdout))

    @staticmethod
    def get_global_instance():
        if LoggerFactory.logger is None:
            LoggerFactory.init()
        return LoggerFactory.logger

    @staticmethod
    def attach_logger(logger, log_path, log_file_name, logger_level, _formatter):
        with mutex:
            if not os.path.exists(log_path):
                os.makedirs(log_path)
        logger.setLevel(logger_level)
        _fh = logging.FileHandler(log_file_name, mode="a")
        _fh.setLevel(logger_level)
        # _formatter = logging.Formatter(
        #     f'%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - {logger_str} - %(message)s')
        _fh.setFormatter(_formatter)

        logger.addHandler(_fh)
        logger.addHandler(logging.StreamHandler(sys.stdout))
        return logger

    @staticmethod
    def get_local_instance(log_id="jsc_log"):
        if LoggerFactory.logger is None:
            LoggerFactory.init()

        logger_name = log_id
        if logger_name in LoggerFactory.local_logger:
            return LoggerFactory.local_logger[logger_name]

        log_path = os.path.join(LoggerFactory.root_dir, log_id)
        log_file_name = os.path.join(log_path, logger_name + ".log")

        _logger = logging.getLogger(log_id)

        _formatter = logging.Formatter(
            f"%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - {logger_name} - %(message)s"
        )
        _logger = LoggerFactory.attach_logger(
            _logger, log_path, log_file_name, LoggerFactory.task_logger_level, _formatter
        )
        LoggerFactory.local_logger[logger_name] = _logger
        return _logger
