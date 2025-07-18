# coding: utf-8

"""
    livesaas20230801

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class GetViewingRestrictionInfoRequest(object):
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
        'activity_id': 'int',
        'viewing_restriction_type': 'int'
    }

    attribute_map = {
        'activity_id': 'ActivityId',
        'viewing_restriction_type': 'ViewingRestrictionType'
    }

    def __init__(self, activity_id=None, viewing_restriction_type=None, _configuration=None):  # noqa: E501
        """GetViewingRestrictionInfoRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._activity_id = None
        self._viewing_restriction_type = None
        self.discriminator = None

        self.activity_id = activity_id
        self.viewing_restriction_type = viewing_restriction_type

    @property
    def activity_id(self):
        """Gets the activity_id of this GetViewingRestrictionInfoRequest.  # noqa: E501


        :return: The activity_id of this GetViewingRestrictionInfoRequest.  # noqa: E501
        :rtype: int
        """
        return self._activity_id

    @activity_id.setter
    def activity_id(self, activity_id):
        """Sets the activity_id of this GetViewingRestrictionInfoRequest.


        :param activity_id: The activity_id of this GetViewingRestrictionInfoRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and activity_id is None:
            raise ValueError("Invalid value for `activity_id`, must not be `None`")  # noqa: E501

        self._activity_id = activity_id

    @property
    def viewing_restriction_type(self):
        """Gets the viewing_restriction_type of this GetViewingRestrictionInfoRequest.  # noqa: E501


        :return: The viewing_restriction_type of this GetViewingRestrictionInfoRequest.  # noqa: E501
        :rtype: int
        """
        return self._viewing_restriction_type

    @viewing_restriction_type.setter
    def viewing_restriction_type(self, viewing_restriction_type):
        """Sets the viewing_restriction_type of this GetViewingRestrictionInfoRequest.


        :param viewing_restriction_type: The viewing_restriction_type of this GetViewingRestrictionInfoRequest.  # noqa: E501
        :type: int
        """
        if self._configuration.client_side_validation and viewing_restriction_type is None:
            raise ValueError("Invalid value for `viewing_restriction_type`, must not be `None`")  # noqa: E501

        self._viewing_restriction_type = viewing_restriction_type

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
        if issubclass(GetViewingRestrictionInfoRequest, dict):
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
        if not isinstance(other, GetViewingRestrictionInfoRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetViewingRestrictionInfoRequest):
            return True

        return self.to_dict() != other.to_dict()
