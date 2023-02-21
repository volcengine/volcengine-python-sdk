# coding: utf-8
# Borrowed from https://github.com/amirziai/flatten

# python 2 and python 3 compatibility library
import six


class Flatten(object):

    def __init__(self, nested_dict, separator=".", start_index=1, root_keys_to_ignore=None, replace_separators=None):
        """
        :param nested_dict: dictionary we want to flatten
        :param start_index: start index for list param
        :param separator: string to separate dictionary keys by
        :param root_keys_to_ignore: set of root keys to ignore from flattening
        :param str replace_separators: Replace separators within keys
        """
        self.nested_dict = nested_dict
        self.separator = separator
        self.start_index = start_index
        self.root_keys_to_ignore = root_keys_to_ignore
        self.replace_separators = replace_separators

    def flat(self):
        if not isinstance(self.nested_dict, dict):
            raise TypeError("flatten requires a dictionary input")

        if not isinstance(self.separator, six.string_types):
            raise TypeError("separator must be string")

        if self.root_keys_to_ignore is None:
            root_keys_to_ignore = set()

        if len(self.nested_dict) == 0:
            return {}

        # This global dictionary stores the flattened keys and values and is
        # ultimately returned
        flattened_dict = dict()

        def _flatten(object_, key):
            """
            For dict, list and set objects_ calls itself on the elements and for
            other types assigns the object_ to
            the corresponding key in the global flattened_dict
            :param object_: object to flatten
            :param key: carries the concatenated key for the object_
            :return: None
            """
            # Empty object can't be iterated, take as is
            if not object_:
                flattened_dict[key] = object_
            # These object types support iteration
            elif isinstance(object_, dict):
                for object_key in object_:
                    if not (not key and object_key in root_keys_to_ignore):
                        _flatten(
                            object_[object_key],
                            self._construct_key(
                                key,
                                self.separator,
                                object_key,
                                replace_separators=self.replace_separators))
            elif isinstance(object_, (list, set, tuple)):
                for index, item in enumerate(object_):
                    _flatten(
                        item,
                        self._construct_key(
                            key,
                            self.separator,
                            index + self.start_index,
                            replace_separators=self.replace_separators))
            # Anything left take as is
            else:
                flattened_dict[key] = object_

        _flatten(self.nested_dict, None)
        return flattened_dict

    def _construct_key(self, previous_key, separator, new_key, replace_separators=None):
        """
        Returns the new_key if no previous key exists, otherwise concatenates
        previous key, separator, and new_key
        :param previous_key:
        :param separator:
        :param new_key:
        :param str replace_separators: Replace separators within keys
        :return: a string if previous_key exists and simply passes through the
        new_key otherwise
        """
        if replace_separators is not None:
            new_key = str(new_key).replace(separator, replace_separators)
        if previous_key:
            return u"{}{}{}".format(previous_key, separator, new_key)
        else:
            return new_key
