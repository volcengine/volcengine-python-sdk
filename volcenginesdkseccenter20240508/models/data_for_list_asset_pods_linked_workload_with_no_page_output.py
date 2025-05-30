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


class DataForListAssetPodsLinkedWorkloadWithNoPageOutput(object):
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
        'instance_id': 'str',
        'pod_id': 'str',
        'pod_name': 'str'
    }

    attribute_map = {
        'instance_id': 'InstanceId',
        'pod_id': 'PodId',
        'pod_name': 'PodName'
    }

    def __init__(self, instance_id=None, pod_id=None, pod_name=None, _configuration=None):  # noqa: E501
        """DataForListAssetPodsLinkedWorkloadWithNoPageOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._instance_id = None
        self._pod_id = None
        self._pod_name = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if pod_id is not None:
            self.pod_id = pod_id
        if pod_name is not None:
            self.pod_name = pod_name

    @property
    def instance_id(self):
        """Gets the instance_id of this DataForListAssetPodsLinkedWorkloadWithNoPageOutput.  # noqa: E501


        :return: The instance_id of this DataForListAssetPodsLinkedWorkloadWithNoPageOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this DataForListAssetPodsLinkedWorkloadWithNoPageOutput.


        :param instance_id: The instance_id of this DataForListAssetPodsLinkedWorkloadWithNoPageOutput.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def pod_id(self):
        """Gets the pod_id of this DataForListAssetPodsLinkedWorkloadWithNoPageOutput.  # noqa: E501


        :return: The pod_id of this DataForListAssetPodsLinkedWorkloadWithNoPageOutput.  # noqa: E501
        :rtype: str
        """
        return self._pod_id

    @pod_id.setter
    def pod_id(self, pod_id):
        """Sets the pod_id of this DataForListAssetPodsLinkedWorkloadWithNoPageOutput.


        :param pod_id: The pod_id of this DataForListAssetPodsLinkedWorkloadWithNoPageOutput.  # noqa: E501
        :type: str
        """

        self._pod_id = pod_id

    @property
    def pod_name(self):
        """Gets the pod_name of this DataForListAssetPodsLinkedWorkloadWithNoPageOutput.  # noqa: E501


        :return: The pod_name of this DataForListAssetPodsLinkedWorkloadWithNoPageOutput.  # noqa: E501
        :rtype: str
        """
        return self._pod_name

    @pod_name.setter
    def pod_name(self, pod_name):
        """Sets the pod_name of this DataForListAssetPodsLinkedWorkloadWithNoPageOutput.


        :param pod_name: The pod_name of this DataForListAssetPodsLinkedWorkloadWithNoPageOutput.  # noqa: E501
        :type: str
        """

        self._pod_name = pod_name

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
        if issubclass(DataForListAssetPodsLinkedWorkloadWithNoPageOutput, dict):
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
        if not isinstance(other, DataForListAssetPodsLinkedWorkloadWithNoPageOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataForListAssetPodsLinkedWorkloadWithNoPageOutput):
            return True

        return self.to_dict() != other.to_dict()
