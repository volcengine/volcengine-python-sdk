# coding: utf-8

"""
    emr

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class RunApplicationActionRequest(object):
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
        'action_name': 'str',
        'application_name': 'str',
        'client_token': 'str',
        'cluster_id': 'str',
        'command_params': 'list[CommandParamForRunApplicationActionInput]',
        'remark': 'str',
        'component_name': 'str'
    }

    attribute_map = {
        'action_name': 'ActionName',
        'application_name': 'ApplicationName',
        'client_token': 'ClientToken',
        'cluster_id': 'ClusterId',
        'command_params': 'CommandParams',
        'remark': 'Remark',
        'component_name': 'componentName'
    }

    def __init__(self, action_name=None, application_name=None, client_token=None, cluster_id=None, command_params=None, remark=None, component_name=None, _configuration=None):  # noqa: E501
        """RunApplicationActionRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._action_name = None
        self._application_name = None
        self._client_token = None
        self._cluster_id = None
        self._command_params = None
        self._remark = None
        self._component_name = None
        self.discriminator = None

        self.action_name = action_name
        self.application_name = application_name
        if client_token is not None:
            self.client_token = client_token
        self.cluster_id = cluster_id
        if command_params is not None:
            self.command_params = command_params
        self.remark = remark
        if component_name is not None:
            self.component_name = component_name

    @property
    def action_name(self):
        """Gets the action_name of this RunApplicationActionRequest.  # noqa: E501


        :return: The action_name of this RunApplicationActionRequest.  # noqa: E501
        :rtype: str
        """
        return self._action_name

    @action_name.setter
    def action_name(self, action_name):
        """Sets the action_name of this RunApplicationActionRequest.


        :param action_name: The action_name of this RunApplicationActionRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and action_name is None:
            raise ValueError("Invalid value for `action_name`, must not be `None`")  # noqa: E501

        self._action_name = action_name

    @property
    def application_name(self):
        """Gets the application_name of this RunApplicationActionRequest.  # noqa: E501


        :return: The application_name of this RunApplicationActionRequest.  # noqa: E501
        :rtype: str
        """
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        """Sets the application_name of this RunApplicationActionRequest.


        :param application_name: The application_name of this RunApplicationActionRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and application_name is None:
            raise ValueError("Invalid value for `application_name`, must not be `None`")  # noqa: E501

        self._application_name = application_name

    @property
    def client_token(self):
        """Gets the client_token of this RunApplicationActionRequest.  # noqa: E501


        :return: The client_token of this RunApplicationActionRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_token

    @client_token.setter
    def client_token(self, client_token):
        """Sets the client_token of this RunApplicationActionRequest.


        :param client_token: The client_token of this RunApplicationActionRequest.  # noqa: E501
        :type: str
        """

        self._client_token = client_token

    @property
    def cluster_id(self):
        """Gets the cluster_id of this RunApplicationActionRequest.  # noqa: E501


        :return: The cluster_id of this RunApplicationActionRequest.  # noqa: E501
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this RunApplicationActionRequest.


        :param cluster_id: The cluster_id of this RunApplicationActionRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and cluster_id is None:
            raise ValueError("Invalid value for `cluster_id`, must not be `None`")  # noqa: E501

        self._cluster_id = cluster_id

    @property
    def command_params(self):
        """Gets the command_params of this RunApplicationActionRequest.  # noqa: E501


        :return: The command_params of this RunApplicationActionRequest.  # noqa: E501
        :rtype: list[CommandParamForRunApplicationActionInput]
        """
        return self._command_params

    @command_params.setter
    def command_params(self, command_params):
        """Sets the command_params of this RunApplicationActionRequest.


        :param command_params: The command_params of this RunApplicationActionRequest.  # noqa: E501
        :type: list[CommandParamForRunApplicationActionInput]
        """

        self._command_params = command_params

    @property
    def remark(self):
        """Gets the remark of this RunApplicationActionRequest.  # noqa: E501


        :return: The remark of this RunApplicationActionRequest.  # noqa: E501
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this RunApplicationActionRequest.


        :param remark: The remark of this RunApplicationActionRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and remark is None:
            raise ValueError("Invalid value for `remark`, must not be `None`")  # noqa: E501

        self._remark = remark

    @property
    def component_name(self):
        """Gets the component_name of this RunApplicationActionRequest.  # noqa: E501


        :return: The component_name of this RunApplicationActionRequest.  # noqa: E501
        :rtype: str
        """
        return self._component_name

    @component_name.setter
    def component_name(self, component_name):
        """Sets the component_name of this RunApplicationActionRequest.


        :param component_name: The component_name of this RunApplicationActionRequest.  # noqa: E501
        :type: str
        """

        self._component_name = component_name

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
        if issubclass(RunApplicationActionRequest, dict):
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
        if not isinstance(other, RunApplicationActionRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RunApplicationActionRequest):
            return True

        return self.to_dict() != other.to_dict()
