# coding: utf-8

"""
    ga

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ListBasicEndpointGroupsRequest(object):
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
        'accelerator_id': 'str',
        'page_num': 'int',
        'page_size': 'int'
    }

    attribute_map = {
        'accelerator_id': 'AcceleratorId',
        'page_num': 'PageNum',
        'page_size': 'PageSize'
    }

    def __init__(self, accelerator_id=None, page_num=None, page_size=None, _configuration=None):  # noqa: E501
        """ListBasicEndpointGroupsRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._accelerator_id = None
        self._page_num = None
        self._page_size = None
        self.discriminator = None

        if accelerator_id is not None:
            self.accelerator_id = accelerator_id
        if page_num is not None:
            self.page_num = page_num
        if page_size is not None:
            self.page_size = page_size

    @property
    def accelerator_id(self):
        """Gets the accelerator_id of this ListBasicEndpointGroupsRequest.  # noqa: E501


        :return: The accelerator_id of this ListBasicEndpointGroupsRequest.  # noqa: E501
        :rtype: str
        """
        return self._accelerator_id

    @accelerator_id.setter
    def accelerator_id(self, accelerator_id):
        """Sets the accelerator_id of this ListBasicEndpointGroupsRequest.


        :param accelerator_id: The accelerator_id of this ListBasicEndpointGroupsRequest.  # noqa: E501
        :type: str
        """

        self._accelerator_id = accelerator_id

    @property
    def page_num(self):
        """Gets the page_num of this ListBasicEndpointGroupsRequest.  # noqa: E501


        :return: The page_num of this ListBasicEndpointGroupsRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_num

    @page_num.setter
    def page_num(self, page_num):
        """Sets the page_num of this ListBasicEndpointGroupsRequest.


        :param page_num: The page_num of this ListBasicEndpointGroupsRequest.  # noqa: E501
        :type: int
        """

        self._page_num = page_num

    @property
    def page_size(self):
        """Gets the page_size of this ListBasicEndpointGroupsRequest.  # noqa: E501


        :return: The page_size of this ListBasicEndpointGroupsRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ListBasicEndpointGroupsRequest.


        :param page_size: The page_size of this ListBasicEndpointGroupsRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

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
        if issubclass(ListBasicEndpointGroupsRequest, dict):
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
        if not isinstance(other, ListBasicEndpointGroupsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListBasicEndpointGroupsRequest):
            return True

        return self.to_dict() != other.to_dict()
