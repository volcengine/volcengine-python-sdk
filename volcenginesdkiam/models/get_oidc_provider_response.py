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


class GetOIDCProviderResponse(object):
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
        'client_i_ds': 'list[str]',
        'create_date': 'str',
        'description': 'str',
        'issuance_limit_time': 'int',
        'issuer_url': 'str',
        'oidc_provider_name': 'str',
        'thumbprints': 'list[str]',
        'trn': 'str',
        'update_date': 'str'
    }

    attribute_map = {
        'client_i_ds': 'ClientIDs',
        'create_date': 'CreateDate',
        'description': 'Description',
        'issuance_limit_time': 'IssuanceLimitTime',
        'issuer_url': 'IssuerURL',
        'oidc_provider_name': 'OIDCProviderName',
        'thumbprints': 'Thumbprints',
        'trn': 'Trn',
        'update_date': 'UpdateDate'
    }

    def __init__(self, client_i_ds=None, create_date=None, description=None, issuance_limit_time=None, issuer_url=None, oidc_provider_name=None, thumbprints=None, trn=None, update_date=None, _configuration=None):  # noqa: E501
        """GetOIDCProviderResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._client_i_ds = None
        self._create_date = None
        self._description = None
        self._issuance_limit_time = None
        self._issuer_url = None
        self._oidc_provider_name = None
        self._thumbprints = None
        self._trn = None
        self._update_date = None
        self.discriminator = None

        if client_i_ds is not None:
            self.client_i_ds = client_i_ds
        if create_date is not None:
            self.create_date = create_date
        if description is not None:
            self.description = description
        if issuance_limit_time is not None:
            self.issuance_limit_time = issuance_limit_time
        if issuer_url is not None:
            self.issuer_url = issuer_url
        if oidc_provider_name is not None:
            self.oidc_provider_name = oidc_provider_name
        if thumbprints is not None:
            self.thumbprints = thumbprints
        if trn is not None:
            self.trn = trn
        if update_date is not None:
            self.update_date = update_date

    @property
    def client_i_ds(self):
        """Gets the client_i_ds of this GetOIDCProviderResponse.  # noqa: E501


        :return: The client_i_ds of this GetOIDCProviderResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._client_i_ds

    @client_i_ds.setter
    def client_i_ds(self, client_i_ds):
        """Sets the client_i_ds of this GetOIDCProviderResponse.


        :param client_i_ds: The client_i_ds of this GetOIDCProviderResponse.  # noqa: E501
        :type: list[str]
        """

        self._client_i_ds = client_i_ds

    @property
    def create_date(self):
        """Gets the create_date of this GetOIDCProviderResponse.  # noqa: E501


        :return: The create_date of this GetOIDCProviderResponse.  # noqa: E501
        :rtype: str
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this GetOIDCProviderResponse.


        :param create_date: The create_date of this GetOIDCProviderResponse.  # noqa: E501
        :type: str
        """

        self._create_date = create_date

    @property
    def description(self):
        """Gets the description of this GetOIDCProviderResponse.  # noqa: E501


        :return: The description of this GetOIDCProviderResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GetOIDCProviderResponse.


        :param description: The description of this GetOIDCProviderResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def issuance_limit_time(self):
        """Gets the issuance_limit_time of this GetOIDCProviderResponse.  # noqa: E501


        :return: The issuance_limit_time of this GetOIDCProviderResponse.  # noqa: E501
        :rtype: int
        """
        return self._issuance_limit_time

    @issuance_limit_time.setter
    def issuance_limit_time(self, issuance_limit_time):
        """Sets the issuance_limit_time of this GetOIDCProviderResponse.


        :param issuance_limit_time: The issuance_limit_time of this GetOIDCProviderResponse.  # noqa: E501
        :type: int
        """

        self._issuance_limit_time = issuance_limit_time

    @property
    def issuer_url(self):
        """Gets the issuer_url of this GetOIDCProviderResponse.  # noqa: E501


        :return: The issuer_url of this GetOIDCProviderResponse.  # noqa: E501
        :rtype: str
        """
        return self._issuer_url

    @issuer_url.setter
    def issuer_url(self, issuer_url):
        """Sets the issuer_url of this GetOIDCProviderResponse.


        :param issuer_url: The issuer_url of this GetOIDCProviderResponse.  # noqa: E501
        :type: str
        """

        self._issuer_url = issuer_url

    @property
    def oidc_provider_name(self):
        """Gets the oidc_provider_name of this GetOIDCProviderResponse.  # noqa: E501


        :return: The oidc_provider_name of this GetOIDCProviderResponse.  # noqa: E501
        :rtype: str
        """
        return self._oidc_provider_name

    @oidc_provider_name.setter
    def oidc_provider_name(self, oidc_provider_name):
        """Sets the oidc_provider_name of this GetOIDCProviderResponse.


        :param oidc_provider_name: The oidc_provider_name of this GetOIDCProviderResponse.  # noqa: E501
        :type: str
        """

        self._oidc_provider_name = oidc_provider_name

    @property
    def thumbprints(self):
        """Gets the thumbprints of this GetOIDCProviderResponse.  # noqa: E501


        :return: The thumbprints of this GetOIDCProviderResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._thumbprints

    @thumbprints.setter
    def thumbprints(self, thumbprints):
        """Sets the thumbprints of this GetOIDCProviderResponse.


        :param thumbprints: The thumbprints of this GetOIDCProviderResponse.  # noqa: E501
        :type: list[str]
        """

        self._thumbprints = thumbprints

    @property
    def trn(self):
        """Gets the trn of this GetOIDCProviderResponse.  # noqa: E501


        :return: The trn of this GetOIDCProviderResponse.  # noqa: E501
        :rtype: str
        """
        return self._trn

    @trn.setter
    def trn(self, trn):
        """Sets the trn of this GetOIDCProviderResponse.


        :param trn: The trn of this GetOIDCProviderResponse.  # noqa: E501
        :type: str
        """

        self._trn = trn

    @property
    def update_date(self):
        """Gets the update_date of this GetOIDCProviderResponse.  # noqa: E501


        :return: The update_date of this GetOIDCProviderResponse.  # noqa: E501
        :rtype: str
        """
        return self._update_date

    @update_date.setter
    def update_date(self, update_date):
        """Sets the update_date of this GetOIDCProviderResponse.


        :param update_date: The update_date of this GetOIDCProviderResponse.  # noqa: E501
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
        if issubclass(GetOIDCProviderResponse, dict):
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
        if not isinstance(other, GetOIDCProviderResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetOIDCProviderResponse):
            return True

        return self.to_dict() != other.to_dict()
