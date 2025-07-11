# coding: utf-8

"""
    volc_observe

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ApplyObjectGroupsByAlertTemplateRequest(object):
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
        'alert_template_id': 'str',
        'apply_objects': 'list[ApplyObjectForApplyObjectGroupsByAlertTemplateInput]',
        'project_name': 'str'
    }

    attribute_map = {
        'alert_template_id': 'AlertTemplateId',
        'apply_objects': 'ApplyObjects',
        'project_name': 'ProjectName'
    }

    def __init__(self, alert_template_id=None, apply_objects=None, project_name=None, _configuration=None):  # noqa: E501
        """ApplyObjectGroupsByAlertTemplateRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._alert_template_id = None
        self._apply_objects = None
        self._project_name = None
        self.discriminator = None

        self.alert_template_id = alert_template_id
        if apply_objects is not None:
            self.apply_objects = apply_objects
        self.project_name = project_name

    @property
    def alert_template_id(self):
        """Gets the alert_template_id of this ApplyObjectGroupsByAlertTemplateRequest.  # noqa: E501


        :return: The alert_template_id of this ApplyObjectGroupsByAlertTemplateRequest.  # noqa: E501
        :rtype: str
        """
        return self._alert_template_id

    @alert_template_id.setter
    def alert_template_id(self, alert_template_id):
        """Sets the alert_template_id of this ApplyObjectGroupsByAlertTemplateRequest.


        :param alert_template_id: The alert_template_id of this ApplyObjectGroupsByAlertTemplateRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and alert_template_id is None:
            raise ValueError("Invalid value for `alert_template_id`, must not be `None`")  # noqa: E501

        self._alert_template_id = alert_template_id

    @property
    def apply_objects(self):
        """Gets the apply_objects of this ApplyObjectGroupsByAlertTemplateRequest.  # noqa: E501


        :return: The apply_objects of this ApplyObjectGroupsByAlertTemplateRequest.  # noqa: E501
        :rtype: list[ApplyObjectForApplyObjectGroupsByAlertTemplateInput]
        """
        return self._apply_objects

    @apply_objects.setter
    def apply_objects(self, apply_objects):
        """Sets the apply_objects of this ApplyObjectGroupsByAlertTemplateRequest.


        :param apply_objects: The apply_objects of this ApplyObjectGroupsByAlertTemplateRequest.  # noqa: E501
        :type: list[ApplyObjectForApplyObjectGroupsByAlertTemplateInput]
        """

        self._apply_objects = apply_objects

    @property
    def project_name(self):
        """Gets the project_name of this ApplyObjectGroupsByAlertTemplateRequest.  # noqa: E501


        :return: The project_name of this ApplyObjectGroupsByAlertTemplateRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this ApplyObjectGroupsByAlertTemplateRequest.


        :param project_name: The project_name of this ApplyObjectGroupsByAlertTemplateRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and project_name is None:
            raise ValueError("Invalid value for `project_name`, must not be `None`")  # noqa: E501

        self._project_name = project_name

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
        if issubclass(ApplyObjectGroupsByAlertTemplateRequest, dict):
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
        if not isinstance(other, ApplyObjectGroupsByAlertTemplateRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ApplyObjectGroupsByAlertTemplateRequest):
            return True

        return self.to_dict() != other.to_dict()
