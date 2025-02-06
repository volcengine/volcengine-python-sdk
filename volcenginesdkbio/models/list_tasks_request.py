# coding: utf-8

"""
    bio

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ListTasksRequest(object):
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
        'page_number': 'int',
        'page_size': 'int',
        'run_id': 'str',
        'workspace_id': 'str'
    }

    attribute_map = {
        'page_number': 'PageNumber',
        'page_size': 'PageSize',
        'run_id': 'RunID',
        'workspace_id': 'WorkspaceID'
    }

    def __init__(self, page_number=None, page_size=None, run_id=None, workspace_id=None, _configuration=None):  # noqa: E501
        """ListTasksRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._page_number = None
        self._page_size = None
        self._run_id = None
        self._workspace_id = None
        self.discriminator = None

        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        self.run_id = run_id
        self.workspace_id = workspace_id

    @property
    def page_number(self):
        """Gets the page_number of this ListTasksRequest.  # noqa: E501


        :return: The page_number of this ListTasksRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this ListTasksRequest.


        :param page_number: The page_number of this ListTasksRequest.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                page_number is not None and page_number < 1):  # noqa: E501
            raise ValueError("Invalid value for `page_number`, must be a value greater than or equal to `1`")  # noqa: E501

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this ListTasksRequest.  # noqa: E501


        :return: The page_size of this ListTasksRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ListTasksRequest.


        :param page_size: The page_size of this ListTasksRequest.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                page_size is not None and page_size > 100):  # noqa: E501
            raise ValueError("Invalid value for `page_size`, must be a value less than or equal to `100`")  # noqa: E501
        if (self._configuration.client_side_validation and
                page_size is not None and page_size < 0):  # noqa: E501
            raise ValueError("Invalid value for `page_size`, must be a value greater than or equal to `0`")  # noqa: E501

        self._page_size = page_size

    @property
    def run_id(self):
        """Gets the run_id of this ListTasksRequest.  # noqa: E501


        :return: The run_id of this ListTasksRequest.  # noqa: E501
        :rtype: str
        """
        return self._run_id

    @run_id.setter
    def run_id(self, run_id):
        """Sets the run_id of this ListTasksRequest.


        :param run_id: The run_id of this ListTasksRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and run_id is None:
            raise ValueError("Invalid value for `run_id`, must not be `None`")  # noqa: E501

        self._run_id = run_id

    @property
    def workspace_id(self):
        """Gets the workspace_id of this ListTasksRequest.  # noqa: E501


        :return: The workspace_id of this ListTasksRequest.  # noqa: E501
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this ListTasksRequest.


        :param workspace_id: The workspace_id of this ListTasksRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and workspace_id is None:
            raise ValueError("Invalid value for `workspace_id`, must not be `None`")  # noqa: E501

        self._workspace_id = workspace_id

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
        if issubclass(ListTasksRequest, dict):
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
        if not isinstance(other, ListTasksRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListTasksRequest):
            return True

        return self.to_dict() != other.to_dict()
