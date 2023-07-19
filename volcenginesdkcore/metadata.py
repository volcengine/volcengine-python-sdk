# coding: utf-8

import pprint
import re  # noqa: F401

import six


class ResponseMetadata(object):
    swagger_types = {
        'service': 'str',
        'request_id': 'str',
        'action': 'str',
        'version': 'str',
        'region': 'str'
    }

    attribute_map = {
        'service': 'Service',
        'request_id': 'RequestId',
        'action': 'Action',
        'version': 'Version',
        'region': 'Region'
    }

    def __init__(self, service=None, request_id=None, action=None, version=None, region=None):
        self._service = None
        self._request_id = None
        self._action = None
        self._version = None
        self._region = None
        self.discriminator = None

        if service is not None:
            self.service = service
        if request_id is not None:
            self.request_id = request_id
        if action is not None:
            self.action = action
        if version is not None:
            self.version = version
        if region is not None:
            self.region = region

    @property
    def service(self):
        return self._service

    @service.setter
    def service(self, service):
        self._service = service

    @property
    def request_id(self):
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        self._request_id = request_id

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, action):
        self._action = action

    @property
    def version(self):
        return self._version

    @version.setter
    def version(self, version):
        self._version = version

    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, region):
        self._region = region

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ResponseMetadata, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ResponseMetadata):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ResponseMetadata):
            return True

        return self.to_dict() != other.to_dict()
