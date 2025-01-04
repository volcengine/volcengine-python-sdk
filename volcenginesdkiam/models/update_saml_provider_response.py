# coding: utf-8

"""
    iam

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class UpdateSAMLProviderResponse(object):
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
        'create_date': 'str',
        'description': 'str',
        'saml_provider_name': 'str',
        'sso_type': 'int',
        'status': 'int',
        'trn': 'str',
        'update_date': 'str'
    }

    attribute_map = {
        'create_date': 'CreateDate',
        'description': 'Description',
        'saml_provider_name': 'SAMLProviderName',
        'sso_type': 'SSOType',
        'status': 'Status',
        'trn': 'Trn',
        'update_date': 'UpdateDate'
    }

    def __init__(self, create_date=None, description=None, saml_provider_name=None, sso_type=None, status=None, trn=None, update_date=None, _configuration=None):  # noqa: E501
        """UpdateSAMLProviderResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._create_date = None
        self._description = None
        self._saml_provider_name = None
        self._sso_type = None
        self._status = None
        self._trn = None
        self._update_date = None
        self.discriminator = None

        if create_date is not None:
            self.create_date = create_date
        if description is not None:
            self.description = description
        if saml_provider_name is not None:
            self.saml_provider_name = saml_provider_name
        if sso_type is not None:
            self.sso_type = sso_type
        if status is not None:
            self.status = status
        if trn is not None:
            self.trn = trn
        if update_date is not None:
            self.update_date = update_date

    @property
    def create_date(self):
        """Gets the create_date of this UpdateSAMLProviderResponse.  # noqa: E501


        :return: The create_date of this UpdateSAMLProviderResponse.  # noqa: E501
        :rtype: str
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this UpdateSAMLProviderResponse.


        :param create_date: The create_date of this UpdateSAMLProviderResponse.  # noqa: E501
        :type: str
        """

        self._create_date = create_date

    @property
    def description(self):
        """Gets the description of this UpdateSAMLProviderResponse.  # noqa: E501


        :return: The description of this UpdateSAMLProviderResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateSAMLProviderResponse.


        :param description: The description of this UpdateSAMLProviderResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def saml_provider_name(self):
        """Gets the saml_provider_name of this UpdateSAMLProviderResponse.  # noqa: E501


        :return: The saml_provider_name of this UpdateSAMLProviderResponse.  # noqa: E501
        :rtype: str
        """
        return self._saml_provider_name

    @saml_provider_name.setter
    def saml_provider_name(self, saml_provider_name):
        """Sets the saml_provider_name of this UpdateSAMLProviderResponse.


        :param saml_provider_name: The saml_provider_name of this UpdateSAMLProviderResponse.  # noqa: E501
        :type: str
        """

        self._saml_provider_name = saml_provider_name

    @property
    def sso_type(self):
        """Gets the sso_type of this UpdateSAMLProviderResponse.  # noqa: E501


        :return: The sso_type of this UpdateSAMLProviderResponse.  # noqa: E501
        :rtype: int
        """
        return self._sso_type

    @sso_type.setter
    def sso_type(self, sso_type):
        """Sets the sso_type of this UpdateSAMLProviderResponse.


        :param sso_type: The sso_type of this UpdateSAMLProviderResponse.  # noqa: E501
        :type: int
        """

        self._sso_type = sso_type

    @property
    def status(self):
        """Gets the status of this UpdateSAMLProviderResponse.  # noqa: E501


        :return: The status of this UpdateSAMLProviderResponse.  # noqa: E501
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateSAMLProviderResponse.


        :param status: The status of this UpdateSAMLProviderResponse.  # noqa: E501
        :type: int
        """

        self._status = status

    @property
    def trn(self):
        """Gets the trn of this UpdateSAMLProviderResponse.  # noqa: E501


        :return: The trn of this UpdateSAMLProviderResponse.  # noqa: E501
        :rtype: str
        """
        return self._trn

    @trn.setter
    def trn(self, trn):
        """Sets the trn of this UpdateSAMLProviderResponse.


        :param trn: The trn of this UpdateSAMLProviderResponse.  # noqa: E501
        :type: str
        """

        self._trn = trn

    @property
    def update_date(self):
        """Gets the update_date of this UpdateSAMLProviderResponse.  # noqa: E501


        :return: The update_date of this UpdateSAMLProviderResponse.  # noqa: E501
        :rtype: str
        """
        return self._update_date

    @update_date.setter
    def update_date(self, update_date):
        """Sets the update_date of this UpdateSAMLProviderResponse.


        :param update_date: The update_date of this UpdateSAMLProviderResponse.  # noqa: E501
        :type: str
        """

        self._update_date = update_date

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
        if issubclass(UpdateSAMLProviderResponse, dict):
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
        if not isinstance(other, UpdateSAMLProviderResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, UpdateSAMLProviderResponse):
            return True

        return self.to_dict() != other.to_dict()
