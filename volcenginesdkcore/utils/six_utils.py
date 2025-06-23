# coding: utf-8

import six


def get_abstract_meta_class():
    if six.PY3:
        from abc import ABC
        return ABC

    from abc import ABCMeta
    return six.with_metaclass(ABCMeta)
