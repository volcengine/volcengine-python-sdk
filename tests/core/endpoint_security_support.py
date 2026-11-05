# coding: utf-8
"""Endpoint 校验回归公用桩：仅使用占位凭证，屏蔽真实网络和宿主环境变量。"""
import os
import socket
import unittest

import six

from volcenginesdkcore import Configuration
from volcenginesdkcore.endpoint.validation import EndpointValidationError

# 能改写 host 结构的注入输入（region / service 均需拦截）。
INJECTION_LABELS = [
    ('at', u'cn-beijing@127.0.0.1'), ('port', u'cn-beijing:443'), ('slash', u'cn/beijing'),
    ('query', u'cn?beijing'), ('fragment', u'cn#beijing'), ('space', u'cn beijing'),
    ('tab', u'cn\tbeijing'), ('lf', u'cn\nbeijing'), ('cr', u'cn\rbeijing'),
    ('nul', u'cn\x00beijing'), ('dot', u'evil.com'), ('percent', u'cn%2fbeijing'),
    ('backslash', u'cn\\beijing'), ('unicode', u'北京'), ('mixed_unicode', u'cn-北京'),
    ('trailing_lf', u'cn-beijing\n'),
    # 额外覆盖：host 注入的完整形态和 Unicode 变体。
    ('at_path', u'cn-beijing@127.0.0.1/'), ('evil_fragment', u'evil.com#'), ('crlf', u'cn-beijing\r\n'),
    ('del', u'cn-beijing\x7f'), ('fullwidth', u'ｃｎ-beijing'), ('line_separator', u'cn\u2028beijing'),
]

# 字符集合法但首尾规则不满足的输入。
EDGE_LABELS = [
    ('digit_first', u'1cn-beijing'), ('single_digit', u'1'), ('hyphen_first', u'-cn-beijing'),
    ('underscore_first', u'_ecs'), ('hyphen_last', u'cn-beijing-'), ('underscore_last', u'rds_mysql_'),
    ('single_hyphen', u'-'), ('single_underscore', u'_'),
]

INVALID_LABELS = INJECTION_LABELS + EDGE_LABELS

# Python 特有：非字符串值不可能是合法 host label，同样以错误码拒绝。
NON_STRING_LABELS = [('int', 42), ('bool', False), ('list', []), ('dict', {}), ('bytearray', bytearray(b'cn'))]
if six.PY3:
    NON_STRING_LABELS.append(('bytes', b'cn-beijing'))

VALID_LABELS = [u'cn-beijing', u'ap-southeast-1', u'a', u'rds_mysql', u'Redis', u'Rds_mysql-2', u'']

LABEL_RULE = ("must start with a letter, end with a letter or digit, "
              "and contain only letters, digits, '-' and '_'")


def expected_message(name, quoted, reason):
    return u'invalid %s %s: %s, %s %s' % (name, quoted, reason, name, LABEL_RULE)


class EndpointSecurityTestCase(unittest.TestCase):
    def setUp(self):
        # 测试只暴露自己设置的环境变量（AK/SK、双栈开关等），不读取宿主环境。
        self.replace(os, 'environ', {})
        self.replace(Configuration, '_default', None)
        self.network_attempts = []

        def blocked(*args, **kwargs):
            self.network_attempts.append(True)
            raise AssertionError('测试禁止真实网络访问')

        self.replace(socket.socket, 'connect', blocked)
        self.replace(socket, 'create_connection', blocked)
        self.replace(socket, 'getaddrinfo', blocked)

    def replace(self, owner, name, value):
        existed = name in vars(owner)
        original = vars(owner).get(name)
        setattr(owner, name, value)
        if existed:
            self.addCleanup(setattr, owner, name, original)
        else:
            self.addCleanup(delattr, owner, name)

    def assert_rejected(self, code, fn, *args, **kwargs):
        with self.assertRaises(EndpointValidationError) as caught:
            fn(*args, **kwargs)
        error = caught.exception
        self.assertIsInstance(error, ValueError)
        self.assertEqual(code, error.code)
        self.assertEqual(u'%s: %s' % (code, error.message), six.text_type(error) if six.PY3 else
                         str(error).decode('utf-8'))
        self.assertEqual([], self.network_attempts)
        return error

    def configuration(self, region='cn-beijing'):
        conf = Configuration()
        conf.ak = 'placeholder-ak'
        conf.sk = 'placeholder-sk'
        conf.region = region
        conf.auto_retry = False
        conf.connection_pool_maxsize = 1
        conf.num_pools = 1
        conf.use_dual_stack = False
        return conf
