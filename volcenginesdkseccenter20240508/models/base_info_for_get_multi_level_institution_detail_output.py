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


class BaseInfoForGetMultiLevelInstitutionDetailOutput(object):
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
        'create_time': 'int',
        'elkeidup_id': 'str',
        'institution_id': 'str',
        'institution_name': 'str',
        'remark': 'str',
        'update_time': 'int'
    }

    attribute_map = {
        'create_time': 'CreateTime',
        'elkeidup_id': 'ElkeidupID',
        'institution_id': 'InstitutionID',
        'institution_name': 'InstitutionName',
        'remark': 'Remark',
        'update_time': 'UpdateTime'
    }

    def __init__(self, create_time=None, elkeidup_id=None, institution_id=None, institution_name=None, remark=None, update_time=None, _configuration=None):  # noqa: E501
        """BaseInfoForGetMultiLevelInstitutionDetailOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._create_time = None
        self._elkeidup_id = None
        self._institution_id = None
        self._institution_name = None
        self._remark = None
        self._update_time = None
        self.discriminator = None

        if create_time is not None:
            self.create_time = create_time
        if elkeidup_id is not None:
            self.elkeidup_id = elkeidup_id
        if institution_id is not None:
            self.institution_id = institution_id
        if institution_name is not None:
            self.institution_name = institution_name
        if remark is not None:
            self.remark = remark
        if update_time is not None:
            self.update_time = update_time

    @property
    def create_time(self):
        """Gets the create_time of this BaseInfoForGetMultiLevelInstitutionDetailOutput.  # noqa: E501


        :return: The create_time of this BaseInfoForGetMultiLevelInstitutionDetailOutput.  # noqa: E501
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this BaseInfoForGetMultiLevelInstitutionDetailOutput.


        :param create_time: The create_time of this BaseInfoForGetMultiLevelInstitutionDetailOutput.  # noqa: E501
        :type: int
        """

        self._create_time = create_time

    @property
    def elkeidup_id(self):
        """Gets the elkeidup_id of this BaseInfoForGetMultiLevelInstitutionDetailOutput.  # noqa: E501


        :return: The elkeidup_id of this BaseInfoForGetMultiLevelInstitutionDetailOutput.  # noqa: E501
        :rtype: str
        """
        return self._elkeidup_id

    @elkeidup_id.setter
    def elkeidup_id(self, elkeidup_id):
        """Sets the elkeidup_id of this BaseInfoForGetMultiLevelInstitutionDetailOutput.


        :param elkeidup_id: The elkeidup_id of this BaseInfoForGetMultiLevelInstitutionDetailOutput.  # noqa: E501
        :type: str
        """

        self._elkeidup_id = elkeidup_id

    @property
    def institution_id(self):
        """Gets the institution_id of this BaseInfoForGetMultiLevelInstitutionDetailOutput.  # noqa: E501


        :return: The institution_id of this BaseInfoForGetMultiLevelInstitutionDetailOutput.  # noqa: E501
        :rtype: str
        """
        return self._institution_id

    @institution_id.setter
    def institution_id(self, institution_id):
        """Sets the institution_id of this BaseInfoForGetMultiLevelInstitutionDetailOutput.


        :param institution_id: The institution_id of this BaseInfoForGetMultiLevelInstitutionDetailOutput.  # noqa: E501
        :type: str
        """

        self._institution_id = institution_id

    @property
    def institution_name(self):
        """Gets the institution_name of this BaseInfoForGetMultiLevelInstitutionDetailOutput.  # noqa: E501


        :return: The institution_name of this BaseInfoForGetMultiLevelInstitutionDetailOutput.  # noqa: E501
        :rtype: str
        """
        return self._institution_name

    @institution_name.setter
    def institution_name(self, institution_name):
        """Sets the institution_name of this BaseInfoForGetMultiLevelInstitutionDetailOutput.


        :param institution_name: The institution_name of this BaseInfoForGetMultiLevelInstitutionDetailOutput.  # noqa: E501
        :type: str
        """

        self._institution_name = institution_name

    @property
    def remark(self):
        """Gets the remark of this BaseInfoForGetMultiLevelInstitutionDetailOutput.  # noqa: E501


        :return: The remark of this BaseInfoForGetMultiLevelInstitutionDetailOutput.  # noqa: E501
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this BaseInfoForGetMultiLevelInstitutionDetailOutput.


        :param remark: The remark of this BaseInfoForGetMultiLevelInstitutionDetailOutput.  # noqa: E501
        :type: str
        """

        self._remark = remark

    @property
    def update_time(self):
        """Gets the update_time of this BaseInfoForGetMultiLevelInstitutionDetailOutput.  # noqa: E501


        :return: The update_time of this BaseInfoForGetMultiLevelInstitutionDetailOutput.  # noqa: E501
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this BaseInfoForGetMultiLevelInstitutionDetailOutput.


        :param update_time: The update_time of this BaseInfoForGetMultiLevelInstitutionDetailOutput.  # noqa: E501
        :type: int
        """

        self._update_time = update_time

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
        if issubclass(BaseInfoForGetMultiLevelInstitutionDetailOutput, dict):
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
        if not isinstance(other, BaseInfoForGetMultiLevelInstitutionDetailOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BaseInfoForGetMultiLevelInstitutionDetailOutput):
            return True

        return self.to_dict() != other.to_dict()
