# coding: utf-8
"""region / service 校验规则：精确错误信息、穷举与等价正则比对、Go %q 转义。"""
import itertools
import re
import unittest

import six

from endpoint_security_support import (
    EndpointSecurityTestCase, INVALID_LABELS, NON_STRING_LABELS, VALID_LABELS, expected_message,
)
from volcenginesdkcore.endpoint import validation
from volcenginesdkcore.endpoint.validation import (
    ERR_CODE_INVALID_REGION, ERR_CODE_INVALID_SERVICE, EndpointValidationError, EndpointValidationTypeError,
    validate_region, validate_service, validate_service_and_region,
)

# 与 Go 版一致的等价正则；fullmatch 语义用 \Z，兼容 Python 2.7。
EQUIVALENT = re.compile(r'[A-Za-z]([A-Za-z0-9_-]*[A-Za-z0-9])?\Z')

VALIDATORS = [('region', ERR_CODE_INVALID_REGION, validate_region),
              ('service', ERR_CODE_INVALID_SERVICE, validate_service)]


def _matches(data):
    """Reference result on raw bytes (latin-1 maps each byte to one char)."""
    return len(data) == 0 or EQUIVALENT.match(bytes(data).decode('latin-1')) is not None


class EndpointLabelSecurityTest(EndpointSecurityTestCase):
    def test_error_codes(self):
        self.assertEqual('InvalidRegion', ERR_CODE_INVALID_REGION)
        self.assertEqual('InvalidService', ERR_CODE_INVALID_SERVICE)

    def test_valid_labels_and_empty_values_pass(self):
        for value in VALID_LABELS + [None]:
            for _, _, validator in VALIDATORS:
                self.assertIsNone(validator(value))
            self.assertIsNone(validate_service_and_region(value, value))
        if six.PY2:
            self.assertIsNone(validate_region(b'cn-beijing'))

    def test_illegal_character_full_message(self):
        cases = [
            (u'cn-beijing@127.0.0.1', u'"cn-beijing@127.0.0.1"', 10),
            (u'cn-beijing:443', u'"cn-beijing:443"', 10),
            (u'cn/beijing', u'"cn/beijing"', 2),
            (u'cn\\beijing', u'"cn\\\\beijing"', 2),
            (u'cn\tbeijing', u'"cn\\tbeijing"', 2),
            (u'cn\nbeijing', u'"cn\\nbeijing"', 2),
            (u'cn\rbeijing', u'"cn\\rbeijing"', 2),
            (u'cn\x00beijing', u'"cn\\x00beijing"', 2),
            (u'cn-beijing\x7f', u'"cn-beijing\\x7f"', 10),
            (u'evil.com', u'"evil.com"', 4),
            (u'北京', u'"北京"', 0),
            # Go 逐字节判断：'北' 的第一个 UTF-8 字节下标为 3。
            (u'cn-北京', u'"cn-北京"', 3),
            (u'cn\u2028beijing', u'"cn\\u2028beijing"', 2),
            (u'1cn@x', u'"1cn@x"', 3),  # 先查字符集，再查首尾
        ]
        for name, code, validator in VALIDATORS:
            for value, quoted, index in cases:
                error = self.assert_rejected(code, validator, value)
                self.assertEqual(expected_message(name, quoted, u'illegal character at index %d' % index),
                                 error.message)

    def test_must_start_with_letter_full_message(self):
        for name, code, validator in VALIDATORS:
            for value in [u'1cn-beijing', u'1', u'-cn-beijing', u'_ecs', u'-', u'_', u'9a', u'-cn-']:
                error = self.assert_rejected(code, validator, value)
                self.assertEqual(expected_message(name, u'"%s"' % value, u'must start with a letter'),
                                 error.message)

    def test_must_not_end_with_hyphen_or_underscore_full_message(self):
        for name, code, validator in VALIDATORS:
            for value in [u'cn-beijing-', u'rds_mysql_', u'a-', u'a_']:
                error = self.assert_rejected(code, validator, value)
                self.assertEqual(expected_message(name, u'"%s"' % value, u"must not end with '-' or '_'"),
                                 error.message)

    def test_full_string_format(self):
        error = self.assert_rejected('InvalidService', validate_service, u'evil.com#')
        self.assertEqual(
            u'InvalidService: invalid service "evil.com#": illegal character at index 4, service must start '
            u"with a letter, end with a letter or digit, and contain only letters, digits, '-' and '_'",
            six.text_type(error) if six.PY3 else str(error).decode('utf-8'))

    def test_service_is_validated_before_region(self):
        self.assert_rejected('InvalidService', validate_service_and_region, u'ecs@x', u'cn@x')
        self.assert_rejected('InvalidRegion', validate_service_and_region, u'ecs', u'cn@x')

    def test_non_string_values_rejected_with_code(self):
        for name, code, validator in VALIDATORS:
            for _, value in NON_STRING_LABELS:
                error = self.assert_rejected(code, validator, value)
                # Python 惯例：类型错误同时是 TypeError，且保留错误码。
                self.assertIsInstance(error, EndpointValidationTypeError)
                self.assertIsInstance(error, TypeError)
                self.assertEqual(u'invalid %s %r: must be a string, not %s, %s must start with a letter, end with '
                                 u"a letter or digit, and contain only letters, digits, '-' and '_'"
                                 % (name, value, type(value).__name__, name), error.message)

    def test_invalid_string_values_are_not_type_errors(self):
        for _, code, validator in VALIDATORS:
            error = self.assert_rejected(code, validator, u'cn@x')
            self.assertNotIsInstance(error, TypeError)

    def test_exhaustive_single_and_double_bytes_equivalent_to_regex(self):
        alphabet = [bytearray([b]) for b in range(256)]
        candidates = alphabet + [a + b for a, b in itertools.product(alphabet, repeat=2)]
        self.assertEqual(256 + 256 * 256, len(candidates))
        for data in candidates:
            reason = validation._validate_endpoint_label(bytes(data) if six.PY2 else data)
            self.assertEqual(_matches(data), reason == '', repr(bytes(data)))

    def test_exhaustive_ascii_text_equivalent_to_regex(self):
        # 公开函数在 text 输入上的穷举：所有 ASCII 单字符与双字符组合。
        chars = [six.unichr(i) for i in range(128)]
        for value in chars + [a + b for a, b in itertools.product(chars, repeat=2)]:
            accepted = True
            try:
                validate_region(value)
            except EndpointValidationError as error:
                self.assertEqual('InvalidRegion', error.code)
                accepted = False
            self.assertEqual(EQUIVALENT.match(value) is not None, accepted, repr(value))

    def test_rule_specific_regression_examples(self):
        # 每条规则单独删除时都会被这里捕获（变异自检用）。
        self.assertEqual('illegal character at index 1', validation._validate_endpoint_label(u'a.b'))
        self.assertEqual('must start with a letter', validation._validate_endpoint_label(u'1a'))
        self.assertEqual("must not end with '-' or '_'", validation._validate_endpoint_label(u'a-'))
        self.assertEqual('', validation._validate_endpoint_label(u'a1'))


def _invalid_test(code, validator, value):
    def test(self):
        self.assert_rejected(code, validator, value)
    return test


for _name, _value in INVALID_LABELS:
    setattr(EndpointLabelSecurityTest, 'test_region_rejects_' + _name,
            _invalid_test('InvalidRegion', validate_region, _value))
    setattr(EndpointLabelSecurityTest, 'test_service_rejects_' + _name,
            _invalid_test('InvalidService', validate_service, _value))


if __name__ == '__main__':
    unittest.main()
