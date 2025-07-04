# coding: utf-8

"""
    ml_platform20240701

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class StopJobRequest(object):
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
        'diagnose_names': 'list[str]',
        'dry_run': 'bool',
        'id': 'str',
        'reason': 'str'
    }

    attribute_map = {
        'diagnose_names': 'DiagnoseNames',
        'dry_run': 'DryRun',
        'id': 'Id',
        'reason': 'Reason'
    }

    def __init__(self, diagnose_names=None, dry_run=None, id=None, reason=None, _configuration=None):  # noqa: E501
        """StopJobRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._diagnose_names = None
        self._dry_run = None
        self._id = None
        self._reason = None
        self.discriminator = None

        if diagnose_names is not None:
            self.diagnose_names = diagnose_names
        if dry_run is not None:
            self.dry_run = dry_run
        self.id = id
        if reason is not None:
            self.reason = reason

    @property
    def diagnose_names(self):
        """Gets the diagnose_names of this StopJobRequest.  # noqa: E501


        :return: The diagnose_names of this StopJobRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._diagnose_names

    @diagnose_names.setter
    def diagnose_names(self, diagnose_names):
        """Sets the diagnose_names of this StopJobRequest.


        :param diagnose_names: The diagnose_names of this StopJobRequest.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["EnvironmentalDiagnosis", "PythonDetection", "LogDetection"]  # noqa: E501
        if (self._configuration.client_side_validation and
                not set(diagnose_names).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `diagnose_names` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(diagnose_names) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._diagnose_names = diagnose_names

    @property
    def dry_run(self):
        """Gets the dry_run of this StopJobRequest.  # noqa: E501


        :return: The dry_run of this StopJobRequest.  # noqa: E501
        :rtype: bool
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        """Sets the dry_run of this StopJobRequest.


        :param dry_run: The dry_run of this StopJobRequest.  # noqa: E501
        :type: bool
        """

        self._dry_run = dry_run

    @property
    def id(self):
        """Gets the id of this StopJobRequest.  # noqa: E501


        :return: The id of this StopJobRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StopJobRequest.


        :param id: The id of this StopJobRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def reason(self):
        """Gets the reason of this StopJobRequest.  # noqa: E501


        :return: The reason of this StopJobRequest.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this StopJobRequest.


        :param reason: The reason of this StopJobRequest.  # noqa: E501
        :type: str
        """

        self._reason = reason

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
        if issubclass(StopJobRequest, dict):
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
        if not isinstance(other, StopJobRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StopJobRequest):
            return True

        return self.to_dict() != other.to_dict()
