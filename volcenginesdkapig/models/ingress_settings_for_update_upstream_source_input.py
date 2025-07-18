# coding: utf-8

"""
    apig

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class IngressSettingsForUpdateUpstreamSourceInput(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'enable_all_ingress_classes': 'bool',
        'enable_all_namespaces': 'bool',
        'enable_ingress': 'bool',
        'enable_ingress_without_ingress_class': 'bool',
        'ingress_classes': 'list[str]',
        'update_status': 'bool',
        'watch_namespaces': 'list[str]'
    }

    attribute_map = {
        'enable_all_ingress_classes': 'EnableAllIngressClasses',
        'enable_all_namespaces': 'EnableAllNamespaces',
        'enable_ingress': 'EnableIngress',
        'enable_ingress_without_ingress_class': 'EnableIngressWithoutIngressClass',
        'ingress_classes': 'IngressClasses',
        'update_status': 'UpdateStatus',
        'watch_namespaces': 'WatchNamespaces'
    }

    def __init__(self, enable_all_ingress_classes=None, enable_all_namespaces=None, enable_ingress=None, enable_ingress_without_ingress_class=None, ingress_classes=None, update_status=None, watch_namespaces=None, _configuration=None):  # noqa: E501
        """IngressSettingsForUpdateUpstreamSourceInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._enable_all_ingress_classes = None
        self._enable_all_namespaces = None
        self._enable_ingress = None
        self._enable_ingress_without_ingress_class = None
        self._ingress_classes = None
        self._update_status = None
        self._watch_namespaces = None
        self.discriminator = None

        if enable_all_ingress_classes is not None:
            self.enable_all_ingress_classes = enable_all_ingress_classes
        if enable_all_namespaces is not None:
            self.enable_all_namespaces = enable_all_namespaces
        if enable_ingress is not None:
            self.enable_ingress = enable_ingress
        if enable_ingress_without_ingress_class is not None:
            self.enable_ingress_without_ingress_class = enable_ingress_without_ingress_class
        if ingress_classes is not None:
            self.ingress_classes = ingress_classes
        if update_status is not None:
            self.update_status = update_status
        if watch_namespaces is not None:
            self.watch_namespaces = watch_namespaces

    @property
    def enable_all_ingress_classes(self):
        """Gets the enable_all_ingress_classes of this IngressSettingsForUpdateUpstreamSourceInput.  # noqa: E501


        :return: The enable_all_ingress_classes of this IngressSettingsForUpdateUpstreamSourceInput.  # noqa: E501
        :rtype: bool
        """
        return self._enable_all_ingress_classes

    @enable_all_ingress_classes.setter
    def enable_all_ingress_classes(self, enable_all_ingress_classes):
        """Sets the enable_all_ingress_classes of this IngressSettingsForUpdateUpstreamSourceInput.


        :param enable_all_ingress_classes: The enable_all_ingress_classes of this IngressSettingsForUpdateUpstreamSourceInput.  # noqa: E501
        :type: bool
        """

        self._enable_all_ingress_classes = enable_all_ingress_classes

    @property
    def enable_all_namespaces(self):
        """Gets the enable_all_namespaces of this IngressSettingsForUpdateUpstreamSourceInput.  # noqa: E501


        :return: The enable_all_namespaces of this IngressSettingsForUpdateUpstreamSourceInput.  # noqa: E501
        :rtype: bool
        """
        return self._enable_all_namespaces

    @enable_all_namespaces.setter
    def enable_all_namespaces(self, enable_all_namespaces):
        """Sets the enable_all_namespaces of this IngressSettingsForUpdateUpstreamSourceInput.


        :param enable_all_namespaces: The enable_all_namespaces of this IngressSettingsForUpdateUpstreamSourceInput.  # noqa: E501
        :type: bool
        """

        self._enable_all_namespaces = enable_all_namespaces

    @property
    def enable_ingress(self):
        """Gets the enable_ingress of this IngressSettingsForUpdateUpstreamSourceInput.  # noqa: E501


        :return: The enable_ingress of this IngressSettingsForUpdateUpstreamSourceInput.  # noqa: E501
        :rtype: bool
        """
        return self._enable_ingress

    @enable_ingress.setter
    def enable_ingress(self, enable_ingress):
        """Sets the enable_ingress of this IngressSettingsForUpdateUpstreamSourceInput.


        :param enable_ingress: The enable_ingress of this IngressSettingsForUpdateUpstreamSourceInput.  # noqa: E501
        :type: bool
        """

        self._enable_ingress = enable_ingress

    @property
    def enable_ingress_without_ingress_class(self):
        """Gets the enable_ingress_without_ingress_class of this IngressSettingsForUpdateUpstreamSourceInput.  # noqa: E501


        :return: The enable_ingress_without_ingress_class of this IngressSettingsForUpdateUpstreamSourceInput.  # noqa: E501
        :rtype: bool
        """
        return self._enable_ingress_without_ingress_class

    @enable_ingress_without_ingress_class.setter
    def enable_ingress_without_ingress_class(self, enable_ingress_without_ingress_class):
        """Sets the enable_ingress_without_ingress_class of this IngressSettingsForUpdateUpstreamSourceInput.


        :param enable_ingress_without_ingress_class: The enable_ingress_without_ingress_class of this IngressSettingsForUpdateUpstreamSourceInput.  # noqa: E501
        :type: bool
        """

        self._enable_ingress_without_ingress_class = enable_ingress_without_ingress_class

    @property
    def ingress_classes(self):
        """Gets the ingress_classes of this IngressSettingsForUpdateUpstreamSourceInput.  # noqa: E501


        :return: The ingress_classes of this IngressSettingsForUpdateUpstreamSourceInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._ingress_classes

    @ingress_classes.setter
    def ingress_classes(self, ingress_classes):
        """Sets the ingress_classes of this IngressSettingsForUpdateUpstreamSourceInput.


        :param ingress_classes: The ingress_classes of this IngressSettingsForUpdateUpstreamSourceInput.  # noqa: E501
        :type: list[str]
        """

        self._ingress_classes = ingress_classes

    @property
    def update_status(self):
        """Gets the update_status of this IngressSettingsForUpdateUpstreamSourceInput.  # noqa: E501


        :return: The update_status of this IngressSettingsForUpdateUpstreamSourceInput.  # noqa: E501
        :rtype: bool
        """
        return self._update_status

    @update_status.setter
    def update_status(self, update_status):
        """Sets the update_status of this IngressSettingsForUpdateUpstreamSourceInput.


        :param update_status: The update_status of this IngressSettingsForUpdateUpstreamSourceInput.  # noqa: E501
        :type: bool
        """

        self._update_status = update_status

    @property
    def watch_namespaces(self):
        """Gets the watch_namespaces of this IngressSettingsForUpdateUpstreamSourceInput.  # noqa: E501


        :return: The watch_namespaces of this IngressSettingsForUpdateUpstreamSourceInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._watch_namespaces

    @watch_namespaces.setter
    def watch_namespaces(self, watch_namespaces):
        """Sets the watch_namespaces of this IngressSettingsForUpdateUpstreamSourceInput.


        :param watch_namespaces: The watch_namespaces of this IngressSettingsForUpdateUpstreamSourceInput.  # noqa: E501
        :type: list[str]
        """

        self._watch_namespaces = watch_namespaces

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
        if issubclass(IngressSettingsForUpdateUpstreamSourceInput, dict):
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
        if not isinstance(other, IngressSettingsForUpdateUpstreamSourceInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IngressSettingsForUpdateUpstreamSourceInput):
            return True

        return self.to_dict() != other.to_dict()
