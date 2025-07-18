# coding: utf-8

"""
    livesaas

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ListActivityMediaAPIRequest(object):
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
        'folder_id': 'int',
        'include_sub_folder': 'bool',
        'name': 'str',
        'order_key': 'str',
        'page_num': 'int',
        'page_size': 'int',
        'search_type': 'int',
        'source_type': 'int',
        'vid': 'str'
    }

    attribute_map = {
        'folder_id': 'FolderId',
        'include_sub_folder': 'IncludeSubFolder',
        'name': 'Name',
        'order_key': 'OrderKey',
        'page_num': 'PageNum',
        'page_size': 'PageSize',
        'search_type': 'SearchType',
        'source_type': 'SourceType',
        'vid': 'Vid'
    }

    def __init__(self, folder_id=None, include_sub_folder=None, name=None, order_key=None, page_num=None, page_size=None, search_type=None, source_type=None, vid=None, _configuration=None):  # noqa: E501
        """ListActivityMediaAPIRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._folder_id = None
        self._include_sub_folder = None
        self._name = None
        self._order_key = None
        self._page_num = None
        self._page_size = None
        self._search_type = None
        self._source_type = None
        self._vid = None
        self.discriminator = None

        if folder_id is not None:
            self.folder_id = folder_id
        if include_sub_folder is not None:
            self.include_sub_folder = include_sub_folder
        if name is not None:
            self.name = name
        if order_key is not None:
            self.order_key = order_key
        if page_num is not None:
            self.page_num = page_num
        if page_size is not None:
            self.page_size = page_size
        self.search_type = search_type
        if source_type is not None:
            self.source_type = source_type
        if vid is not None:
            self.vid = vid

    @property
    def folder_id(self):
        """Gets the folder_id of this ListActivityMediaAPIRequest.  # noqa: E501


        :return: The folder_id of this ListActivityMediaAPIRequest.  # noqa: E501
        :rtype: int
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        """Sets the folder_id of this ListActivityMediaAPIRequest.


        :param folder_id: The folder_id of this ListActivityMediaAPIRequest.  # noqa: E501
        :type: int
        """

        self._folder_id = folder_id

    @property
    def include_sub_folder(self):
        """Gets the include_sub_folder of this ListActivityMediaAPIRequest.  # noqa: E501


        :return: The include_sub_folder of this ListActivityMediaAPIRequest.  # noqa: E501
        :rtype: bool
        """
        return self._include_sub_folder

    @include_sub_folder.setter
    def include_sub_folder(self, include_sub_folder):
        """Sets the include_sub_folder of this ListActivityMediaAPIRequest.


        :param include_sub_folder: The include_sub_folder of this ListActivityMediaAPIRequest.  # noqa: E501
        :type: bool
        """

        self._include_sub_folder = include_sub_folder

    @property
    def name(self):
        """Gets the name of this ListActivityMediaAPIRequest.  # noqa: E501


        :return: The name of this ListActivityMediaAPIRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListActivityMediaAPIRequest.


        :param name: The name of this ListActivityMediaAPIRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def order_key(self):
        """Gets the order_key of this ListActivityMediaAPIRequest.  # noqa: E501


        :return: The order_key of this ListActivityMediaAPIRequest.  # noqa: E501
        :rtype: str
        """
        return self._order_key

    @order_key.setter
    def order_key(self, order_key):
        """Sets the order_key of this ListActivityMediaAPIRequest.


        :param order_key: The order_key of this ListActivityMediaAPIRequest.  # noqa: E501
        :type: str
        """

        self._order_key = order_key

    @property
    def page_num(self):
        """Gets the page_num of this ListActivityMediaAPIRequest.  # noqa: E501


        :return: The page_num of this ListActivityMediaAPIRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_num

    @page_num.setter
    def page_num(self, page_num):
        """Sets the page_num of this ListActivityMediaAPIRequest.


        :param page_num: The page_num of this ListActivityMediaAPIRequest.  # noqa: E501
        :type: int
        """

        self._page_num = page_num

    @property
    def page_size(self):
        """Gets the page_size of this ListActivityMediaAPIRequest.  # noqa: E501


        :return: The page_size of this ListActivityMediaAPIRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ListActivityMediaAPIRequest.


        :param page_size: The page_size of this ListActivityMediaAPIRequest.  # noqa: E501
        :type: int
        """

        self._page_size = page_size

    @property
    def search_type(self):
        """Gets the search_type of this ListActivityMediaAPIRequest.  # noqa: E501


        :return: The search_type of this ListActivityMediaAPIRequest.  # noqa: E501
        :rtype: int
        """
        return self._search_type

    @search_type.setter
    def search_type(self, search_type):
        """Sets the search_type of this ListActivityMediaAPIRequest.


        :param search_type: The search_type of this ListActivityMediaAPIRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and search_type is None:
            raise ValueError("Invalid value for `search_type`, must not be `None`")  # noqa: E501

        self._search_type = search_type

    @property
    def source_type(self):
        """Gets the source_type of this ListActivityMediaAPIRequest.  # noqa: E501


        :return: The source_type of this ListActivityMediaAPIRequest.  # noqa: E501
        :rtype: int
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this ListActivityMediaAPIRequest.


        :param source_type: The source_type of this ListActivityMediaAPIRequest.  # noqa: E501
        :type: int
        """

        self._source_type = source_type

    @property
    def vid(self):
        """Gets the vid of this ListActivityMediaAPIRequest.  # noqa: E501


        :return: The vid of this ListActivityMediaAPIRequest.  # noqa: E501
        :rtype: str
        """
        return self._vid

    @vid.setter
    def vid(self, vid):
        """Sets the vid of this ListActivityMediaAPIRequest.


        :param vid: The vid of this ListActivityMediaAPIRequest.  # noqa: E501
        :type: str
        """

        self._vid = vid

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
        if issubclass(ListActivityMediaAPIRequest, dict):
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
        if not isinstance(other, ListActivityMediaAPIRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListActivityMediaAPIRequest):
            return True

        return self.to_dict() != other.to_dict()
