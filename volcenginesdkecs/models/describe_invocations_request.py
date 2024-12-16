# coding: utf-8

"""
    ecs

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeInvocationsRequest(object):
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
        'command_id': 'str',
        'command_name': 'str',
        'command_type': 'str',
        'content_encoding': 'str',
        'invocation_id': 'str',
        'invocation_name': 'str',
        'invocation_status': 'str',
        'page_number': 'int',
        'page_size': 'int',
        'project_name': 'str',
        'repeat_mode': 'str',
        'tag_filters': 'list[TagFilterForDescribeInvocationsInput]'
    }

    attribute_map = {
        'command_id': 'CommandId',
        'command_name': 'CommandName',
        'command_type': 'CommandType',
        'content_encoding': 'ContentEncoding',
        'invocation_id': 'InvocationId',
        'invocation_name': 'InvocationName',
        'invocation_status': 'InvocationStatus',
        'page_number': 'PageNumber',
        'page_size': 'PageSize',
        'project_name': 'ProjectName',
        'repeat_mode': 'RepeatMode',
        'tag_filters': 'TagFilters'
    }

    def __init__(self, command_id=None, command_name=None, command_type=None, content_encoding=None, invocation_id=None, invocation_name=None, invocation_status=None, page_number=None, page_size=None, project_name=None, repeat_mode=None, tag_filters=None, _configuration=None):  # noqa: E501
        """DescribeInvocationsRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._command_id = None
        self._command_name = None
        self._command_type = None
        self._content_encoding = None
        self._invocation_id = None
        self._invocation_name = None
        self._invocation_status = None
        self._page_number = None
        self._page_size = None
        self._project_name = None
        self._repeat_mode = None
        self._tag_filters = None
        self.discriminator = None

        if command_id is not None:
            self.command_id = command_id
        if command_name is not None:
            self.command_name = command_name
        if command_type is not None:
            self.command_type = command_type
        if content_encoding is not None:
            self.content_encoding = content_encoding
        if invocation_id is not None:
            self.invocation_id = invocation_id
        if invocation_name is not None:
            self.invocation_name = invocation_name
        if invocation_status is not None:
            self.invocation_status = invocation_status
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        if project_name is not None:
            self.project_name = project_name
        if repeat_mode is not None:
            self.repeat_mode = repeat_mode
        if tag_filters is not None:
            self.tag_filters = tag_filters

    @property
    def command_id(self):
        """Gets the command_id of this DescribeInvocationsRequest.  # noqa: E501


        :return: The command_id of this DescribeInvocationsRequest.  # noqa: E501
        :rtype: str
        """
        return self._command_id

    @command_id.setter
    def command_id(self, command_id):
        """Sets the command_id of this DescribeInvocationsRequest.


        :param command_id: The command_id of this DescribeInvocationsRequest.  # noqa: E501
        :type: str
        """

        self._command_id = command_id

    @property
    def command_name(self):
        """Gets the command_name of this DescribeInvocationsRequest.  # noqa: E501


        :return: The command_name of this DescribeInvocationsRequest.  # noqa: E501
        :rtype: str
        """
        return self._command_name

    @command_name.setter
    def command_name(self, command_name):
        """Sets the command_name of this DescribeInvocationsRequest.


        :param command_name: The command_name of this DescribeInvocationsRequest.  # noqa: E501
        :type: str
        """

        self._command_name = command_name

    @property
    def command_type(self):
        """Gets the command_type of this DescribeInvocationsRequest.  # noqa: E501


        :return: The command_type of this DescribeInvocationsRequest.  # noqa: E501
        :rtype: str
        """
        return self._command_type

    @command_type.setter
    def command_type(self, command_type):
        """Sets the command_type of this DescribeInvocationsRequest.


        :param command_type: The command_type of this DescribeInvocationsRequest.  # noqa: E501
        :type: str
        """

        self._command_type = command_type

    @property
    def content_encoding(self):
        """Gets the content_encoding of this DescribeInvocationsRequest.  # noqa: E501


        :return: The content_encoding of this DescribeInvocationsRequest.  # noqa: E501
        :rtype: str
        """
        return self._content_encoding

    @content_encoding.setter
    def content_encoding(self, content_encoding):
        """Sets the content_encoding of this DescribeInvocationsRequest.


        :param content_encoding: The content_encoding of this DescribeInvocationsRequest.  # noqa: E501
        :type: str
        """

        self._content_encoding = content_encoding

    @property
    def invocation_id(self):
        """Gets the invocation_id of this DescribeInvocationsRequest.  # noqa: E501


        :return: The invocation_id of this DescribeInvocationsRequest.  # noqa: E501
        :rtype: str
        """
        return self._invocation_id

    @invocation_id.setter
    def invocation_id(self, invocation_id):
        """Sets the invocation_id of this DescribeInvocationsRequest.


        :param invocation_id: The invocation_id of this DescribeInvocationsRequest.  # noqa: E501
        :type: str
        """

        self._invocation_id = invocation_id

    @property
    def invocation_name(self):
        """Gets the invocation_name of this DescribeInvocationsRequest.  # noqa: E501


        :return: The invocation_name of this DescribeInvocationsRequest.  # noqa: E501
        :rtype: str
        """
        return self._invocation_name

    @invocation_name.setter
    def invocation_name(self, invocation_name):
        """Sets the invocation_name of this DescribeInvocationsRequest.


        :param invocation_name: The invocation_name of this DescribeInvocationsRequest.  # noqa: E501
        :type: str
        """

        self._invocation_name = invocation_name

    @property
    def invocation_status(self):
        """Gets the invocation_status of this DescribeInvocationsRequest.  # noqa: E501


        :return: The invocation_status of this DescribeInvocationsRequest.  # noqa: E501
        :rtype: str
        """
        return self._invocation_status

    @invocation_status.setter
    def invocation_status(self, invocation_status):
        """Sets the invocation_status of this DescribeInvocationsRequest.


        :param invocation_status: The invocation_status of this DescribeInvocationsRequest.  # noqa: E501
        :type: str
        """

        self._invocation_status = invocation_status

    @property
    def page_number(self):
        """Gets the page_number of this DescribeInvocationsRequest.  # noqa: E501


        :return: The page_number of this DescribeInvocationsRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this DescribeInvocationsRequest.


        :param page_number: The page_number of this DescribeInvocationsRequest.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this DescribeInvocationsRequest.  # noqa: E501


        :return: The page_size of this DescribeInvocationsRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this DescribeInvocationsRequest.


        :param page_size: The page_size of this DescribeInvocationsRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def project_name(self):
        """Gets the project_name of this DescribeInvocationsRequest.  # noqa: E501


        :return: The project_name of this DescribeInvocationsRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this DescribeInvocationsRequest.


        :param project_name: The project_name of this DescribeInvocationsRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def repeat_mode(self):
        """Gets the repeat_mode of this DescribeInvocationsRequest.  # noqa: E501


        :return: The repeat_mode of this DescribeInvocationsRequest.  # noqa: E501
        :rtype: str
        """
        return self._repeat_mode

    @repeat_mode.setter
    def repeat_mode(self, repeat_mode):
        """Sets the repeat_mode of this DescribeInvocationsRequest.


        :param repeat_mode: The repeat_mode of this DescribeInvocationsRequest.  # noqa: E501
        :type: str
        """

        self._repeat_mode = repeat_mode

    @property
    def tag_filters(self):
        """Gets the tag_filters of this DescribeInvocationsRequest.  # noqa: E501


        :return: The tag_filters of this DescribeInvocationsRequest.  # noqa: E501
        :rtype: list[TagFilterForDescribeInvocationsInput]
        """
        return self._tag_filters

    @tag_filters.setter
    def tag_filters(self, tag_filters):
        """Sets the tag_filters of this DescribeInvocationsRequest.


        :param tag_filters: The tag_filters of this DescribeInvocationsRequest.  # noqa: E501
        :type: list[TagFilterForDescribeInvocationsInput]
        """

        self._tag_filters = tag_filters

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
        if issubclass(DescribeInvocationsRequest, dict):
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
        if not isinstance(other, DescribeInvocationsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeInvocationsRequest):
            return True

        return self.to_dict() != other.to_dict()
