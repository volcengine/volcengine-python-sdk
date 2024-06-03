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


class BatchUpdateCdnConfigResponse(object):
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
        'deploy_result': 'list[DeployResultForBatchUpdateCdnConfigOutput]'
    }

    attribute_map = {
        'deploy_result': 'DeployResult'
    }

    def __init__(self, deploy_result=None, _configuration=None):  # noqa: E501
        """BatchUpdateCdnConfigResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._deploy_result = None
        self.discriminator = None

        if deploy_result is not None:
            self.deploy_result = deploy_result

    @property
    def deploy_result(self):
        """Gets the deploy_result of this BatchUpdateCdnConfigResponse.  # noqa: E501


        :return: The deploy_result of this BatchUpdateCdnConfigResponse.  # noqa: E501
        :rtype: list[DeployResultForBatchUpdateCdnConfigOutput]
        """
        return self._deploy_result

    @deploy_result.setter
    def deploy_result(self, deploy_result):
        """Sets the deploy_result of this BatchUpdateCdnConfigResponse.


        :param deploy_result: The deploy_result of this BatchUpdateCdnConfigResponse.  # noqa: E501
        :type: list[DeployResultForBatchUpdateCdnConfigOutput]
        """

        self._deploy_result = deploy_result

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
        if issubclass(BatchUpdateCdnConfigResponse, dict):
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
        if not isinstance(other, BatchUpdateCdnConfigResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BatchUpdateCdnConfigResponse):
            return True

        return self.to_dict() != other.to_dict()