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


class ScaleInNodeGroupResponse(object):
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
        'cluster_id': 'str',
        'operation_id': 'str',
        'result_data': 'ResultDataForScaleInNodeGroupOutput'
    }

    attribute_map = {
        'cluster_id': 'ClusterId',
        'operation_id': 'OperationId',
        'result_data': 'ResultData'
    }

    def __init__(self, cluster_id=None, operation_id=None, result_data=None, _configuration=None):  # noqa: E501
        """ScaleInNodeGroupResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cluster_id = None
        self._operation_id = None
        self._result_data = None
        self.discriminator = None

        if cluster_id is not None:
            self.cluster_id = cluster_id
        if operation_id is not None:
            self.operation_id = operation_id
        if result_data is not None:
            self.result_data = result_data

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ScaleInNodeGroupResponse.  # noqa: E501


        :return: The cluster_id of this ScaleInNodeGroupResponse.  # noqa: E501
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ScaleInNodeGroupResponse.


        :param cluster_id: The cluster_id of this ScaleInNodeGroupResponse.  # noqa: E501
        :type: str
        """

        self._cluster_id = cluster_id

    @property
    def operation_id(self):
        """Gets the operation_id of this ScaleInNodeGroupResponse.  # noqa: E501


        :return: The operation_id of this ScaleInNodeGroupResponse.  # noqa: E501
        :rtype: str
        """
        return self._operation_id

    @operation_id.setter
    def operation_id(self, operation_id):
        """Sets the operation_id of this ScaleInNodeGroupResponse.


        :param operation_id: The operation_id of this ScaleInNodeGroupResponse.  # noqa: E501
        :type: str
        """

        self._operation_id = operation_id

    @property
    def result_data(self):
        """Gets the result_data of this ScaleInNodeGroupResponse.  # noqa: E501


        :return: The result_data of this ScaleInNodeGroupResponse.  # noqa: E501
        :rtype: ResultDataForScaleInNodeGroupOutput
        """
        return self._result_data

    @result_data.setter
    def result_data(self, result_data):
        """Sets the result_data of this ScaleInNodeGroupResponse.


        :param result_data: The result_data of this ScaleInNodeGroupResponse.  # noqa: E501
        :type: ResultDataForScaleInNodeGroupOutput
        """

        self._result_data = result_data

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
        if issubclass(ScaleInNodeGroupResponse, dict):
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
        if not isinstance(other, ScaleInNodeGroupResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ScaleInNodeGroupResponse):
            return True

        return self.to_dict() != other.to_dict()
