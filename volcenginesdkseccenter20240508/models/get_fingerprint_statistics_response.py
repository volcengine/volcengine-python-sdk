# coding: utf-8

"""
    seccenter20240508

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class GetFingerprintStatisticsResponse(object):
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
        'app': 'int',
        'container': 'int',
        'cron': 'int',
        'integrity': 'int',
        'kmod': 'int',
        'port': 'int',
        'process': 'int',
        'service': 'int',
        'software': 'int',
        'user': 'int',
        'web': 'int'
    }

    attribute_map = {
        'app': 'App',
        'container': 'Container',
        'cron': 'Cron',
        'integrity': 'Integrity',
        'kmod': 'Kmod',
        'port': 'Port',
        'process': 'Process',
        'service': 'Service',
        'software': 'Software',
        'user': 'User',
        'web': 'Web'
    }

    def __init__(self, app=None, container=None, cron=None, integrity=None, kmod=None, port=None, process=None, service=None, software=None, user=None, web=None, _configuration=None):  # noqa: E501
        """GetFingerprintStatisticsResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._app = None
        self._container = None
        self._cron = None
        self._integrity = None
        self._kmod = None
        self._port = None
        self._process = None
        self._service = None
        self._software = None
        self._user = None
        self._web = None
        self.discriminator = None

        if app is not None:
            self.app = app
        if container is not None:
            self.container = container
        if cron is not None:
            self.cron = cron
        if integrity is not None:
            self.integrity = integrity
        if kmod is not None:
            self.kmod = kmod
        if port is not None:
            self.port = port
        if process is not None:
            self.process = process
        if service is not None:
            self.service = service
        if software is not None:
            self.software = software
        if user is not None:
            self.user = user
        if web is not None:
            self.web = web

    @property
    def app(self):
        """Gets the app of this GetFingerprintStatisticsResponse.  # noqa: E501


        :return: The app of this GetFingerprintStatisticsResponse.  # noqa: E501
        :rtype: int
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this GetFingerprintStatisticsResponse.


        :param app: The app of this GetFingerprintStatisticsResponse.  # noqa: E501
        :type: int
        """

        self._app = app

    @property
    def container(self):
        """Gets the container of this GetFingerprintStatisticsResponse.  # noqa: E501


        :return: The container of this GetFingerprintStatisticsResponse.  # noqa: E501
        :rtype: int
        """
        return self._container

    @container.setter
    def container(self, container):
        """Sets the container of this GetFingerprintStatisticsResponse.


        :param container: The container of this GetFingerprintStatisticsResponse.  # noqa: E501
        :type: int
        """

        self._container = container

    @property
    def cron(self):
        """Gets the cron of this GetFingerprintStatisticsResponse.  # noqa: E501


        :return: The cron of this GetFingerprintStatisticsResponse.  # noqa: E501
        :rtype: int
        """
        return self._cron

    @cron.setter
    def cron(self, cron):
        """Sets the cron of this GetFingerprintStatisticsResponse.


        :param cron: The cron of this GetFingerprintStatisticsResponse.  # noqa: E501
        :type: int
        """

        self._cron = cron

    @property
    def integrity(self):
        """Gets the integrity of this GetFingerprintStatisticsResponse.  # noqa: E501


        :return: The integrity of this GetFingerprintStatisticsResponse.  # noqa: E501
        :rtype: int
        """
        return self._integrity

    @integrity.setter
    def integrity(self, integrity):
        """Sets the integrity of this GetFingerprintStatisticsResponse.


        :param integrity: The integrity of this GetFingerprintStatisticsResponse.  # noqa: E501
        :type: int
        """

        self._integrity = integrity

    @property
    def kmod(self):
        """Gets the kmod of this GetFingerprintStatisticsResponse.  # noqa: E501


        :return: The kmod of this GetFingerprintStatisticsResponse.  # noqa: E501
        :rtype: int
        """
        return self._kmod

    @kmod.setter
    def kmod(self, kmod):
        """Sets the kmod of this GetFingerprintStatisticsResponse.


        :param kmod: The kmod of this GetFingerprintStatisticsResponse.  # noqa: E501
        :type: int
        """

        self._kmod = kmod

    @property
    def port(self):
        """Gets the port of this GetFingerprintStatisticsResponse.  # noqa: E501


        :return: The port of this GetFingerprintStatisticsResponse.  # noqa: E501
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this GetFingerprintStatisticsResponse.


        :param port: The port of this GetFingerprintStatisticsResponse.  # noqa: E501
        :type: int
        """

        self._port = port

    @property
    def process(self):
        """Gets the process of this GetFingerprintStatisticsResponse.  # noqa: E501


        :return: The process of this GetFingerprintStatisticsResponse.  # noqa: E501
        :rtype: int
        """
        return self._process

    @process.setter
    def process(self, process):
        """Sets the process of this GetFingerprintStatisticsResponse.


        :param process: The process of this GetFingerprintStatisticsResponse.  # noqa: E501
        :type: int
        """

        self._process = process

    @property
    def service(self):
        """Gets the service of this GetFingerprintStatisticsResponse.  # noqa: E501


        :return: The service of this GetFingerprintStatisticsResponse.  # noqa: E501
        :rtype: int
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this GetFingerprintStatisticsResponse.


        :param service: The service of this GetFingerprintStatisticsResponse.  # noqa: E501
        :type: int
        """

        self._service = service

    @property
    def software(self):
        """Gets the software of this GetFingerprintStatisticsResponse.  # noqa: E501


        :return: The software of this GetFingerprintStatisticsResponse.  # noqa: E501
        :rtype: int
        """
        return self._software

    @software.setter
    def software(self, software):
        """Sets the software of this GetFingerprintStatisticsResponse.


        :param software: The software of this GetFingerprintStatisticsResponse.  # noqa: E501
        :type: int
        """

        self._software = software

    @property
    def user(self):
        """Gets the user of this GetFingerprintStatisticsResponse.  # noqa: E501


        :return: The user of this GetFingerprintStatisticsResponse.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this GetFingerprintStatisticsResponse.


        :param user: The user of this GetFingerprintStatisticsResponse.  # noqa: E501
        :type: int
        """

        self._user = user

    @property
    def web(self):
        """Gets the web of this GetFingerprintStatisticsResponse.  # noqa: E501


        :return: The web of this GetFingerprintStatisticsResponse.  # noqa: E501
        :rtype: int
        """
        return self._web

    @web.setter
    def web(self, web):
        """Sets the web of this GetFingerprintStatisticsResponse.


        :param web: The web of this GetFingerprintStatisticsResponse.  # noqa: E501
        :type: int
        """

        self._web = web

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
        if issubclass(GetFingerprintStatisticsResponse, dict):
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
        if not isinstance(other, GetFingerprintStatisticsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetFingerprintStatisticsResponse):
            return True

        return self.to_dict() != other.to_dict()
