# coding: utf-8

"""
    cdn

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ConvertOriginLineForDescribeCdnConfigOutput(object):
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
        'address': 'str',
        'bucket_name': 'str',
        'http_port': 'str',
        'https_port': 'str',
        'instance_type': 'str',
        'origin_host': 'str',
        'origin_type': 'str',
        'private_bucket_access': 'bool',
        'private_bucket_auth': 'PrivateBucketAuthForDescribeCdnConfigOutput',
        'region': 'str',
        'weight': 'str'
    }

    attribute_map = {
        'address': 'Address',
        'bucket_name': 'BucketName',
        'http_port': 'HttpPort',
        'https_port': 'HttpsPort',
        'instance_type': 'InstanceType',
        'origin_host': 'OriginHost',
        'origin_type': 'OriginType',
        'private_bucket_access': 'PrivateBucketAccess',
        'private_bucket_auth': 'PrivateBucketAuth',
        'region': 'Region',
        'weight': 'Weight'
    }

    def __init__(self, address=None, bucket_name=None, http_port=None, https_port=None, instance_type=None, origin_host=None, origin_type=None, private_bucket_access=None, private_bucket_auth=None, region=None, weight=None, _configuration=None):  # noqa: E501
        """ConvertOriginLineForDescribeCdnConfigOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._address = None
        self._bucket_name = None
        self._http_port = None
        self._https_port = None
        self._instance_type = None
        self._origin_host = None
        self._origin_type = None
        self._private_bucket_access = None
        self._private_bucket_auth = None
        self._region = None
        self._weight = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if bucket_name is not None:
            self.bucket_name = bucket_name
        if http_port is not None:
            self.http_port = http_port
        if https_port is not None:
            self.https_port = https_port
        if instance_type is not None:
            self.instance_type = instance_type
        if origin_host is not None:
            self.origin_host = origin_host
        if origin_type is not None:
            self.origin_type = origin_type
        if private_bucket_access is not None:
            self.private_bucket_access = private_bucket_access
        if private_bucket_auth is not None:
            self.private_bucket_auth = private_bucket_auth
        if region is not None:
            self.region = region
        if weight is not None:
            self.weight = weight

    @property
    def address(self):
        """Gets the address of this ConvertOriginLineForDescribeCdnConfigOutput.  # noqa: E501


        :return: The address of this ConvertOriginLineForDescribeCdnConfigOutput.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this ConvertOriginLineForDescribeCdnConfigOutput.


        :param address: The address of this ConvertOriginLineForDescribeCdnConfigOutput.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def bucket_name(self):
        """Gets the bucket_name of this ConvertOriginLineForDescribeCdnConfigOutput.  # noqa: E501


        :return: The bucket_name of this ConvertOriginLineForDescribeCdnConfigOutput.  # noqa: E501
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """Sets the bucket_name of this ConvertOriginLineForDescribeCdnConfigOutput.


        :param bucket_name: The bucket_name of this ConvertOriginLineForDescribeCdnConfigOutput.  # noqa: E501
        :type: str
        """

        self._bucket_name = bucket_name

    @property
    def http_port(self):
        """Gets the http_port of this ConvertOriginLineForDescribeCdnConfigOutput.  # noqa: E501


        :return: The http_port of this ConvertOriginLineForDescribeCdnConfigOutput.  # noqa: E501
        :rtype: str
        """
        return self._http_port

    @http_port.setter
    def http_port(self, http_port):
        """Sets the http_port of this ConvertOriginLineForDescribeCdnConfigOutput.


        :param http_port: The http_port of this ConvertOriginLineForDescribeCdnConfigOutput.  # noqa: E501
        :type: str
        """

        self._http_port = http_port

    @property
    def https_port(self):
        """Gets the https_port of this ConvertOriginLineForDescribeCdnConfigOutput.  # noqa: E501


        :return: The https_port of this ConvertOriginLineForDescribeCdnConfigOutput.  # noqa: E501
        :rtype: str
        """
        return self._https_port

    @https_port.setter
    def https_port(self, https_port):
        """Sets the https_port of this ConvertOriginLineForDescribeCdnConfigOutput.


        :param https_port: The https_port of this ConvertOriginLineForDescribeCdnConfigOutput.  # noqa: E501
        :type: str
        """

        self._https_port = https_port

    @property
    def instance_type(self):
        """Gets the instance_type of this ConvertOriginLineForDescribeCdnConfigOutput.  # noqa: E501


        :return: The instance_type of this ConvertOriginLineForDescribeCdnConfigOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        """Sets the instance_type of this ConvertOriginLineForDescribeCdnConfigOutput.


        :param instance_type: The instance_type of this ConvertOriginLineForDescribeCdnConfigOutput.  # noqa: E501
        :type: str
        """

        self._instance_type = instance_type

    @property
    def origin_host(self):
        """Gets the origin_host of this ConvertOriginLineForDescribeCdnConfigOutput.  # noqa: E501


        :return: The origin_host of this ConvertOriginLineForDescribeCdnConfigOutput.  # noqa: E501
        :rtype: str
        """
        return self._origin_host

    @origin_host.setter
    def origin_host(self, origin_host):
        """Sets the origin_host of this ConvertOriginLineForDescribeCdnConfigOutput.


        :param origin_host: The origin_host of this ConvertOriginLineForDescribeCdnConfigOutput.  # noqa: E501
        :type: str
        """

        self._origin_host = origin_host

    @property
    def origin_type(self):
        """Gets the origin_type of this ConvertOriginLineForDescribeCdnConfigOutput.  # noqa: E501


        :return: The origin_type of this ConvertOriginLineForDescribeCdnConfigOutput.  # noqa: E501
        :rtype: str
        """
        return self._origin_type

    @origin_type.setter
    def origin_type(self, origin_type):
        """Sets the origin_type of this ConvertOriginLineForDescribeCdnConfigOutput.


        :param origin_type: The origin_type of this ConvertOriginLineForDescribeCdnConfigOutput.  # noqa: E501
        :type: str
        """

        self._origin_type = origin_type

    @property
    def private_bucket_access(self):
        """Gets the private_bucket_access of this ConvertOriginLineForDescribeCdnConfigOutput.  # noqa: E501


        :return: The private_bucket_access of this ConvertOriginLineForDescribeCdnConfigOutput.  # noqa: E501
        :rtype: bool
        """
        return self._private_bucket_access

    @private_bucket_access.setter
    def private_bucket_access(self, private_bucket_access):
        """Sets the private_bucket_access of this ConvertOriginLineForDescribeCdnConfigOutput.


        :param private_bucket_access: The private_bucket_access of this ConvertOriginLineForDescribeCdnConfigOutput.  # noqa: E501
        :type: bool
        """

        self._private_bucket_access = private_bucket_access

    @property
    def private_bucket_auth(self):
        """Gets the private_bucket_auth of this ConvertOriginLineForDescribeCdnConfigOutput.  # noqa: E501


        :return: The private_bucket_auth of this ConvertOriginLineForDescribeCdnConfigOutput.  # noqa: E501
        :rtype: PrivateBucketAuthForDescribeCdnConfigOutput
        """
        return self._private_bucket_auth

    @private_bucket_auth.setter
    def private_bucket_auth(self, private_bucket_auth):
        """Sets the private_bucket_auth of this ConvertOriginLineForDescribeCdnConfigOutput.


        :param private_bucket_auth: The private_bucket_auth of this ConvertOriginLineForDescribeCdnConfigOutput.  # noqa: E501
        :type: PrivateBucketAuthForDescribeCdnConfigOutput
        """

        self._private_bucket_auth = private_bucket_auth

    @property
    def region(self):
        """Gets the region of this ConvertOriginLineForDescribeCdnConfigOutput.  # noqa: E501


        :return: The region of this ConvertOriginLineForDescribeCdnConfigOutput.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ConvertOriginLineForDescribeCdnConfigOutput.


        :param region: The region of this ConvertOriginLineForDescribeCdnConfigOutput.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def weight(self):
        """Gets the weight of this ConvertOriginLineForDescribeCdnConfigOutput.  # noqa: E501


        :return: The weight of this ConvertOriginLineForDescribeCdnConfigOutput.  # noqa: E501
        :rtype: str
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this ConvertOriginLineForDescribeCdnConfigOutput.


        :param weight: The weight of this ConvertOriginLineForDescribeCdnConfigOutput.  # noqa: E501
        :type: str
        """

        self._weight = weight

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
        if issubclass(ConvertOriginLineForDescribeCdnConfigOutput, dict):
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
        if not isinstance(other, ConvertOriginLineForDescribeCdnConfigOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConvertOriginLineForDescribeCdnConfigOutput):
            return True

        return self.to_dict() != other.to_dict()
