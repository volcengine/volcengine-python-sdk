# coding: utf-8

from __future__ import print_function

import logging

# Try using Enum (which comes with Py3 / you can pip install enum34 for Py2)
try:
    from enum import Enum
except Exception:
    Enum = None

SDK_DEBUGGER_LOG_NAME = "com.volcengine.sdkcore"


if Enum is not None:
    # ========== Implementation based on Enum (preferred) ==========
    class LogLevel(Enum):
        # Base bit (starting from low bit 0)
        LOG_DEBUG_OFF = (0,)
        LOG_DEBUG_WITH_REQUEST = (1,)
        LOG_DEBUG_WITH_REQUEST_BODY = (2, 'LOG_DEBUG_WITH_REQUEST')
        LOG_DEBUG_WITH_REQUEST_ID = (3, 'LOG_DEBUG_WITH_REQUEST')
        LOG_DEBUG_WITH_RESPONSE = (4, 'LOG_DEBUG_WITH_REQUEST')
        LOG_DEBUG_WITH_RESPONSE_BODY = (5, 'LOG_DEBUG_WITH_RESPONSE')
        LOG_DEBUG_WITH_SIGNING = (6, 'LOG_DEBUG_WITH_REQUEST')
        LOG_DEBUG_WITH_ENDPOINT = (7, 'LOG_DEBUG_WITH_REQUEST')
        LOG_DEBUG_WITH_REQUEST_RETRIES = (8, 'LOG_DEBUG_WITH_REQUEST')
        LOG_DEBUG_WITH_CONFIG = (9, 'LOG_DEBUG_WITH_REQUEST')
        # Special: represents "include all debug items", mask will be assigned dynamically after class definition
        LOG_DEBUG_ALL = (-1,)

        def __init__(self, bit_index, *parents):
            # Record bit index
            object.__setattr__(self, 'bit_index', bit_index)

            # Calculate mask; ALL uses -1 as a placeholder, assigned later
            if bit_index >= 0:
                m = 1 << bit_index
                cls = type(self)  # Key: do not directly use class name, compatible during enum construction
                for p in parents:
                    parent = p if isinstance(p, cls) else cls[p]
                    m |= parent.mask
                object.__setattr__(self, 'mask', m)
            else:
                object.__setattr__(self, 'mask', 0)

        @classmethod
        def combine(cls, *modes):
            """Combine multiple modes into flags"""
            if not modes:
                return cls.LOG_DEBUG_OFF.mask
            f = 0
            for m in modes:
                f |= m.mask
            return f

        def matches(self, flags):
            """Check whether the current mode is contained in flags"""
            return (flags & self.mask) == self.mask

    # Calculate mask for LOG_DEBUG_ALL after class loading
    _all = 0
    for lv in LogLevel:
        if lv not in (LogLevel.LOG_DEBUG_OFF, LogLevel.LOG_DEBUG_ALL):
            _all |= lv.mask
    object.__setattr__(LogLevel.LOG_DEBUG_ALL, 'mask', _all)

else:
    # ========== Pure Python fallback implementation when Enum is not available ==========
    class _Level(object):
        __slots__ = ('name', 'bit_index', 'mask')

        def __init__(self, name, bit_index, parents=None):
            self.name = name
            self.bit_index = bit_index
            if bit_index >= 0:
                m = 1 << bit_index
                if parents:
                    for p in parents:
                        m |= p.mask
                self.mask = m
            else:
                self.mask = 0  # Placeholder, ALL will be assigned later by OR-ing all masks

        def matches(self, flags):
            return (flags & self.mask) == self.mask

        def __repr__(self):
            return '<LogLevel {0} mask=0x{1:X}>'.format(self.name, self.mask)

    class LogLevel(object):
        """Enum fallback container: provides the same constants and API as Enum"""
        # Define base and parent levels first
        LOG_DEBUG_OFF = _Level('LOG_DEBUG_OFF', 0)
        LOG_DEBUG_WITH_REQUEST = _Level('LOG_DEBUG_WITH_REQUEST', 1)

        LOG_DEBUG_WITH_RESPONSE = _Level('LOG_DEBUG_WITH_RESPONSE', 4, [LOG_DEBUG_WITH_REQUEST])

        # Levels dependent on parents
        LOG_DEBUG_WITH_REQUEST_BODY = _Level('LOG_DEBUG_WITH_REQUEST_BODY', 2, [LOG_DEBUG_WITH_REQUEST])
        LOG_DEBUG_WITH_REQUEST_ID = _Level('LOG_DEBUG_WITH_REQUEST_ID', 3, [LOG_DEBUG_WITH_REQUEST])
        LOG_DEBUG_WITH_RESPONSE_BODY = _Level('LOG_DEBUG_WITH_RESPONSE_BODY', 5, [LOG_DEBUG_WITH_RESPONSE])
        LOG_DEBUG_WITH_SIGNING = _Level('LOG_DEBUG_WITH_SIGNING', 6, [LOG_DEBUG_WITH_REQUEST])
        LOG_DEBUG_WITH_ENDPOINT = _Level('LOG_DEBUG_WITH_ENDPOINT', 7, [LOG_DEBUG_WITH_REQUEST])
        LOG_DEBUG_WITH_REQUEST_RETRIES = _Level('LOG_DEBUG_WITH_REQUEST_RETRIES', 8, [LOG_DEBUG_WITH_REQUEST])
        LOG_DEBUG_WITH_CONFIG = _Level('LOG_DEBUG_WITH_CONFIG', 9, [LOG_DEBUG_WITH_REQUEST])

        LOG_DEBUG_ALL = _Level('LOG_DEBUG_ALL', -1)  # Placeholder, will be OR-ed later

        @classmethod
        def _all_levels(cls):
            # Used for internal aggregation
            return [
                cls.LOG_DEBUG_OFF,
                cls.LOG_DEBUG_WITH_REQUEST,
                cls.LOG_DEBUG_WITH_REQUEST_BODY,
                cls.LOG_DEBUG_WITH_REQUEST_ID,
                cls.LOG_DEBUG_WITH_RESPONSE,
                cls.LOG_DEBUG_WITH_RESPONSE_BODY,
                cls.LOG_DEBUG_WITH_SIGNING,
                cls.LOG_DEBUG_WITH_ENDPOINT,
                cls.LOG_DEBUG_WITH_REQUEST_RETRIES,
                cls.LOG_DEBUG_WITH_CONFIG,
                cls.LOG_DEBUG_ALL,
            ]

        @classmethod
        def combine(cls, *modes):
            if not modes:
                return cls.LOG_DEBUG_OFF.mask
            f = 0
            for m in modes:
                f |= m.mask
            return f

    # Calculate mask for LOG_DEBUG_ALL
    _all_mask = 0
    for _lv in LogLevel._all_levels():
        if _lv.name not in ('LOG_DEBUG_OFF', 'LOG_DEBUG_ALL'):
            _all_mask |= _lv.mask
    LogLevel.LOG_DEBUG_ALL.mask = _all_mask


class SdkCoreLogger(logging.Logger):

    def __init__(self, name, debug=False, log_level=0):
        # In Python 2.7, must explicitly call parent __init__
        if debug:
            logging.Logger.__init__(self, name, logging.DEBUG)
        else:
            logging.Logger.__init__(self, name, logging.WARNING)
        self._log_level = int(log_level)

    # ---- Custom bit control ----
    def set_log_level(self, log_level):
        self._log_level = int(log_level)

    def get_log_level(self):
        return self._log_level

    def is_enabled_for_loglevel(self, level_enum):
        # Does not change logging's native level semantics, only adds an extra bit filter
        return level_enum.matches(self._log_level)

    @staticmethod
    def get_sdk_logger(name,
                       debug=False,
                       log_level=0,
                       fmt="%(asctime)s [%(threadName)s] %(levelname)s %(name)s:%(lineno)d - %(message)s",
                       datefmt="%Y-%m-%d %H:%M:%S"):
        """
        Create an SdkLogger with Handler.
        - base_level: standard logging minimum level
        - log_flags: your custom LogLevel bitmask
        """
        # No global pollution: only subclass used for the returned logger
        # If you want to globally setLoggerClass, call logging.setLoggerClass(SdkLogger) at module init
        logger = SdkCoreLogger(name, debug=debug, log_level=log_level)

        if not logger.handlers:
            h = logging.StreamHandler()
            if debug:
                h.setLevel(logging.DEBUG)
            else:
                h.setLevel(logging.WARNING)
            try:
                formatter = logging.Formatter(fmt=fmt, datefmt=datefmt)
            except TypeError:
                # Compatibility with very old logging versions (almost never used)
                formatter = logging.Formatter(fmt)
            h.setFormatter(formatter)
            logger.addHandler(h)

        logger.propagate = False  # Avoid bubbling up to root logger
        return logger

    # ---- New API: debug with "function bit" ----
    def debugx(self, curr_log_level_enum, msg, *args, **kwargs):
        """
        Debug with "function bit".
        Conditions:
          1) Standard logging level allowed (Logger.level / Handler.level)
          2) Custom bit included (self._log_level)
        Only then will it output.
        """
        if self.isEnabledFor(logging.DEBUG) and self.is_enabled_for_loglevel(curr_log_level_enum):
            # Keep consistent with logging convention, parameters use % placeholder, formatted in Handler/Formatter
            self.debug(msg, *args, **kwargs)

    def debug_sign(self, msg, *args, **kwargs):
        self.debugx(LogLevel.LOG_DEBUG_WITH_SIGNING, "[Sign] " + msg, *args, **kwargs)

    def debug_endpoint(self, msg, *args, **kwargs):
        self.debugx(LogLevel.LOG_DEBUG_WITH_ENDPOINT, "[Endpoint] " + msg, *args, **kwargs)

    def debug_retry(self, msg, *args, **kwargs):
        self.debugx(LogLevel.LOG_DEBUG_WITH_REQUEST, "[Retry] " + msg, *args, **kwargs)

    def debug_config(self, msg, *args, **kwargs):
        self.debugx(LogLevel.LOG_DEBUG_WITH_CONFIG, "[Config] " + msg, *args, **kwargs)

    def debug_request(self, msg, *args, **kwargs):
        is_body = kwargs.pop('is_body', False)
        if is_body:
            self.debugx(LogLevel.LOG_DEBUG_WITH_REQUEST_BODY, "[Request] " + msg, *args, **kwargs)
        else:
            self.debugx(LogLevel.LOG_DEBUG_WITH_REQUEST, "[Request] " + msg, *args, **kwargs)

    def debug_response(self, msg, *args, **kwargs):
        is_body = kwargs.pop('is_body', False)
        if is_body:
            self.debugx(LogLevel.LOG_DEBUG_WITH_RESPONSE_BODY, "[Response] " + msg, *args, **kwargs)
        else:
            self.debugx(LogLevel.LOG_DEBUG_WITH_RESPONSE, "[Response] " + msg, *args, **kwargs)

sdk_core_logger =   SdkCoreLogger.get_sdk_logger(SDK_DEBUGGER_LOG_NAME, debug=False, log_level=LogLevel.LOG_DEBUG_ALL.mask)
