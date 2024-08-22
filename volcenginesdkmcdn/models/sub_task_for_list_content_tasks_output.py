# coding: utf-8

"""
    mcdn

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class SubTaskForListContentTasksOutput(object):
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
        'cloud_account_id': 'str',
        'cloud_account_name': 'str',
        'description': 'str',
        'product_type': 'str',
        'sub_product': 'str',
        'submit_at': 'int',
        'submit_status': 'str',
        'url': 'list[str]',
        'vendor': 'str',
        'vendor_task_ids': 'list[str]'
    }

    attribute_map = {
        'cloud_account_id': 'CloudAccountId',
        'cloud_account_name': 'CloudAccountName',
        'description': 'Description',
        'product_type': 'ProductType',
        'sub_product': 'SubProduct',
        'submit_at': 'SubmitAt',
        'submit_status': 'SubmitStatus',
        'url': 'Url',
        'vendor': 'Vendor',
        'vendor_task_ids': 'VendorTaskIds'
    }

    def __init__(self, cloud_account_id=None, cloud_account_name=None, description=None, product_type=None, sub_product=None, submit_at=None, submit_status=None, url=None, vendor=None, vendor_task_ids=None, _configuration=None):  # noqa: E501
        """SubTaskForListContentTasksOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cloud_account_id = None
        self._cloud_account_name = None
        self._description = None
        self._product_type = None
        self._sub_product = None
        self._submit_at = None
        self._submit_status = None
        self._url = None
        self._vendor = None
        self._vendor_task_ids = None
        self.discriminator = None

        if cloud_account_id is not None:
            self.cloud_account_id = cloud_account_id
        if cloud_account_name is not None:
            self.cloud_account_name = cloud_account_name
        if description is not None:
            self.description = description
        if product_type is not None:
            self.product_type = product_type
        if sub_product is not None:
            self.sub_product = sub_product
        if submit_at is not None:
            self.submit_at = submit_at
        if submit_status is not None:
            self.submit_status = submit_status
        if url is not None:
            self.url = url
        if vendor is not None:
            self.vendor = vendor
        if vendor_task_ids is not None:
            self.vendor_task_ids = vendor_task_ids

    @property
    def cloud_account_id(self):
        """Gets the cloud_account_id of this SubTaskForListContentTasksOutput.  # noqa: E501


        :return: The cloud_account_id of this SubTaskForListContentTasksOutput.  # noqa: E501
        :rtype: str
        """
        return self._cloud_account_id

    @cloud_account_id.setter
    def cloud_account_id(self, cloud_account_id):
        """Sets the cloud_account_id of this SubTaskForListContentTasksOutput.


        :param cloud_account_id: The cloud_account_id of this SubTaskForListContentTasksOutput.  # noqa: E501
        :type: str
        """

        self._cloud_account_id = cloud_account_id

    @property
    def cloud_account_name(self):
        """Gets the cloud_account_name of this SubTaskForListContentTasksOutput.  # noqa: E501


        :return: The cloud_account_name of this SubTaskForListContentTasksOutput.  # noqa: E501
        :rtype: str
        """
        return self._cloud_account_name

    @cloud_account_name.setter
    def cloud_account_name(self, cloud_account_name):
        """Sets the cloud_account_name of this SubTaskForListContentTasksOutput.


        :param cloud_account_name: The cloud_account_name of this SubTaskForListContentTasksOutput.  # noqa: E501
        :type: str
        """

        self._cloud_account_name = cloud_account_name

    @property
    def description(self):
        """Gets the description of this SubTaskForListContentTasksOutput.  # noqa: E501


        :return: The description of this SubTaskForListContentTasksOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SubTaskForListContentTasksOutput.


        :param description: The description of this SubTaskForListContentTasksOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def product_type(self):
        """Gets the product_type of this SubTaskForListContentTasksOutput.  # noqa: E501


        :return: The product_type of this SubTaskForListContentTasksOutput.  # noqa: E501
        :rtype: str
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        """Sets the product_type of this SubTaskForListContentTasksOutput.


        :param product_type: The product_type of this SubTaskForListContentTasksOutput.  # noqa: E501
        :type: str
        """

        self._product_type = product_type

    @property
    def sub_product(self):
        """Gets the sub_product of this SubTaskForListContentTasksOutput.  # noqa: E501


        :return: The sub_product of this SubTaskForListContentTasksOutput.  # noqa: E501
        :rtype: str
        """
        return self._sub_product

    @sub_product.setter
    def sub_product(self, sub_product):
        """Sets the sub_product of this SubTaskForListContentTasksOutput.


        :param sub_product: The sub_product of this SubTaskForListContentTasksOutput.  # noqa: E501
        :type: str
        """

        self._sub_product = sub_product

    @property
    def submit_at(self):
        """Gets the submit_at of this SubTaskForListContentTasksOutput.  # noqa: E501


        :return: The submit_at of this SubTaskForListContentTasksOutput.  # noqa: E501
        :rtype: int
        """
        return self._submit_at

    @submit_at.setter
    def submit_at(self, submit_at):
        """Sets the submit_at of this SubTaskForListContentTasksOutput.


        :param submit_at: The submit_at of this SubTaskForListContentTasksOutput.  # noqa: E501
        :type: int
        """

        self._submit_at = submit_at

    @property
    def submit_status(self):
        """Gets the submit_status of this SubTaskForListContentTasksOutput.  # noqa: E501


        :return: The submit_status of this SubTaskForListContentTasksOutput.  # noqa: E501
        :rtype: str
        """
        return self._submit_status

    @submit_status.setter
    def submit_status(self, submit_status):
        """Sets the submit_status of this SubTaskForListContentTasksOutput.


        :param submit_status: The submit_status of this SubTaskForListContentTasksOutput.  # noqa: E501
        :type: str
        """

        self._submit_status = submit_status

    @property
    def url(self):
        """Gets the url of this SubTaskForListContentTasksOutput.  # noqa: E501


        :return: The url of this SubTaskForListContentTasksOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this SubTaskForListContentTasksOutput.


        :param url: The url of this SubTaskForListContentTasksOutput.  # noqa: E501
        :type: list[str]
        """

        self._url = url

    @property
    def vendor(self):
        """Gets the vendor of this SubTaskForListContentTasksOutput.  # noqa: E501


        :return: The vendor of this SubTaskForListContentTasksOutput.  # noqa: E501
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this SubTaskForListContentTasksOutput.


        :param vendor: The vendor of this SubTaskForListContentTasksOutput.  # noqa: E501
        :type: str
        """

        self._vendor = vendor

    @property
    def vendor_task_ids(self):
        """Gets the vendor_task_ids of this SubTaskForListContentTasksOutput.  # noqa: E501


        :return: The vendor_task_ids of this SubTaskForListContentTasksOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._vendor_task_ids

    @vendor_task_ids.setter
    def vendor_task_ids(self, vendor_task_ids):
        """Sets the vendor_task_ids of this SubTaskForListContentTasksOutput.


        :param vendor_task_ids: The vendor_task_ids of this SubTaskForListContentTasksOutput.  # noqa: E501
        :type: list[str]
        """

        self._vendor_task_ids = vendor_task_ids

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
        if issubclass(SubTaskForListContentTasksOutput, dict):
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
        if not isinstance(other, SubTaskForListContentTasksOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SubTaskForListContentTasksOutput):
            return True

        return self.to_dict() != other.to_dict()