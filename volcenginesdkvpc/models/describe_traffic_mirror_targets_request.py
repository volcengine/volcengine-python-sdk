# coding: utf-8

"""
    vpc

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DescribeTrafficMirrorTargetsRequest(object):
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
        'max_results': 'int',
        'next_token': 'str',
        'project_name': 'str',
        'tag_filters': 'list[TagFilterForDescribeTrafficMirrorTargetsInput]',
        'traffic_mirror_target_ids': 'str',
        'traffic_mirror_target_name': 'str'
    }

    attribute_map = {
        'max_results': 'MaxResults',
        'next_token': 'NextToken',
        'project_name': 'ProjectName',
        'tag_filters': 'TagFilters',
        'traffic_mirror_target_ids': 'TrafficMirrorTargetIds',
        'traffic_mirror_target_name': 'TrafficMirrorTargetName'
    }

    def __init__(self, max_results=None, next_token=None, project_name=None, tag_filters=None, traffic_mirror_target_ids=None, traffic_mirror_target_name=None, _configuration=None):  # noqa: E501
        """DescribeTrafficMirrorTargetsRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._max_results = None
        self._next_token = None
        self._project_name = None
        self._tag_filters = None
        self._traffic_mirror_target_ids = None
        self._traffic_mirror_target_name = None
        self.discriminator = None

        if max_results is not None:
            self.max_results = max_results
        if next_token is not None:
            self.next_token = next_token
        if project_name is not None:
            self.project_name = project_name
        if tag_filters is not None:
            self.tag_filters = tag_filters
        if traffic_mirror_target_ids is not None:
            self.traffic_mirror_target_ids = traffic_mirror_target_ids
        if traffic_mirror_target_name is not None:
            self.traffic_mirror_target_name = traffic_mirror_target_name

    @property
    def max_results(self):
        """Gets the max_results of this DescribeTrafficMirrorTargetsRequest.  # noqa: E501


        :return: The max_results of this DescribeTrafficMirrorTargetsRequest.  # noqa: E501
        :rtype: int
        """
        return self._max_results

    @max_results.setter
    def max_results(self, max_results):
        """Sets the max_results of this DescribeTrafficMirrorTargetsRequest.


        :param max_results: The max_results of this DescribeTrafficMirrorTargetsRequest.  # noqa: E501
        :type: int
        """

        self._max_results = max_results

    @property
    def next_token(self):
        """Gets the next_token of this DescribeTrafficMirrorTargetsRequest.  # noqa: E501


        :return: The next_token of this DescribeTrafficMirrorTargetsRequest.  # noqa: E501
        :rtype: str
        """
        return self._next_token

    @next_token.setter
    def next_token(self, next_token):
        """Sets the next_token of this DescribeTrafficMirrorTargetsRequest.


        :param next_token: The next_token of this DescribeTrafficMirrorTargetsRequest.  # noqa: E501
        :type: str
        """

        self._next_token = next_token

    @property
    def project_name(self):
        """Gets the project_name of this DescribeTrafficMirrorTargetsRequest.  # noqa: E501


        :return: The project_name of this DescribeTrafficMirrorTargetsRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this DescribeTrafficMirrorTargetsRequest.


        :param project_name: The project_name of this DescribeTrafficMirrorTargetsRequest.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def tag_filters(self):
        """Gets the tag_filters of this DescribeTrafficMirrorTargetsRequest.  # noqa: E501


        :return: The tag_filters of this DescribeTrafficMirrorTargetsRequest.  # noqa: E501
        :rtype: list[TagFilterForDescribeTrafficMirrorTargetsInput]
        """
        return self._tag_filters

    @tag_filters.setter
    def tag_filters(self, tag_filters):
        """Sets the tag_filters of this DescribeTrafficMirrorTargetsRequest.


        :param tag_filters: The tag_filters of this DescribeTrafficMirrorTargetsRequest.  # noqa: E501
        :type: list[TagFilterForDescribeTrafficMirrorTargetsInput]
        """

        self._tag_filters = tag_filters

    @property
    def traffic_mirror_target_ids(self):
        """Gets the traffic_mirror_target_ids of this DescribeTrafficMirrorTargetsRequest.  # noqa: E501


        :return: The traffic_mirror_target_ids of this DescribeTrafficMirrorTargetsRequest.  # noqa: E501
        :rtype: str
        """
        return self._traffic_mirror_target_ids

    @traffic_mirror_target_ids.setter
    def traffic_mirror_target_ids(self, traffic_mirror_target_ids):
        """Sets the traffic_mirror_target_ids of this DescribeTrafficMirrorTargetsRequest.


        :param traffic_mirror_target_ids: The traffic_mirror_target_ids of this DescribeTrafficMirrorTargetsRequest.  # noqa: E501
        :type: str
        """

        self._traffic_mirror_target_ids = traffic_mirror_target_ids

    @property
    def traffic_mirror_target_name(self):
        """Gets the traffic_mirror_target_name of this DescribeTrafficMirrorTargetsRequest.  # noqa: E501


        :return: The traffic_mirror_target_name of this DescribeTrafficMirrorTargetsRequest.  # noqa: E501
        :rtype: str
        """
        return self._traffic_mirror_target_name

    @traffic_mirror_target_name.setter
    def traffic_mirror_target_name(self, traffic_mirror_target_name):
        """Sets the traffic_mirror_target_name of this DescribeTrafficMirrorTargetsRequest.


        :param traffic_mirror_target_name: The traffic_mirror_target_name of this DescribeTrafficMirrorTargetsRequest.  # noqa: E501
        :type: str
        """

        self._traffic_mirror_target_name = traffic_mirror_target_name

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
        if issubclass(DescribeTrafficMirrorTargetsRequest, dict):
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
        if not isinstance(other, DescribeTrafficMirrorTargetsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DescribeTrafficMirrorTargetsRequest):
            return True

        return self.to_dict() != other.to_dict()
