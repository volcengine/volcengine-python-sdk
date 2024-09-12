# coding: utf-8

"""
    alb

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class ModifyListenerAttributesRequest(object):
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
        'acl_ids': 'list[str]',
        'acl_status': 'str',
        'acl_type': 'str',
        'ca_certificate_id': 'str',
        'cert_center_certificate_id': 'str',
        'certificate_id': 'str',
        'certificate_source': 'str',
        'client_address_transmission_protocol': 'str',
        'customized_cfg_id': 'str',
        'description': 'str',
        'domain_extensions': 'list[DomainExtensionForModifyListenerAttributesInput]',
        'enable_http2': 'str',
        'enable_quic': 'str',
        'enabled': 'str',
        'listener_id': 'str',
        'listener_name': 'str',
        'proxy_protocol_disabled': 'str',
        'server_group_id': 'str'
    }

    attribute_map = {
        'acl_ids': 'AclIds',
        'acl_status': 'AclStatus',
        'acl_type': 'AclType',
        'ca_certificate_id': 'CACertificateId',
        'cert_center_certificate_id': 'CertCenterCertificateId',
        'certificate_id': 'CertificateId',
        'certificate_source': 'CertificateSource',
        'client_address_transmission_protocol': 'ClientAddressTransmissionProtocol',
        'customized_cfg_id': 'CustomizedCfgId',
        'description': 'Description',
        'domain_extensions': 'DomainExtensions',
        'enable_http2': 'EnableHttp2',
        'enable_quic': 'EnableQuic',
        'enabled': 'Enabled',
        'listener_id': 'ListenerId',
        'listener_name': 'ListenerName',
        'proxy_protocol_disabled': 'ProxyProtocolDisabled',
        'server_group_id': 'ServerGroupId'
    }

    def __init__(self, acl_ids=None, acl_status=None, acl_type=None, ca_certificate_id=None, cert_center_certificate_id=None, certificate_id=None, certificate_source=None, client_address_transmission_protocol=None, customized_cfg_id=None, description=None, domain_extensions=None, enable_http2=None, enable_quic=None, enabled=None, listener_id=None, listener_name=None, proxy_protocol_disabled=None, server_group_id=None, _configuration=None):  # noqa: E501
        """ModifyListenerAttributesRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._acl_ids = None
        self._acl_status = None
        self._acl_type = None
        self._ca_certificate_id = None
        self._cert_center_certificate_id = None
        self._certificate_id = None
        self._certificate_source = None
        self._client_address_transmission_protocol = None
        self._customized_cfg_id = None
        self._description = None
        self._domain_extensions = None
        self._enable_http2 = None
        self._enable_quic = None
        self._enabled = None
        self._listener_id = None
        self._listener_name = None
        self._proxy_protocol_disabled = None
        self._server_group_id = None
        self.discriminator = None

        if acl_ids is not None:
            self.acl_ids = acl_ids
        if acl_status is not None:
            self.acl_status = acl_status
        if acl_type is not None:
            self.acl_type = acl_type
        if ca_certificate_id is not None:
            self.ca_certificate_id = ca_certificate_id
        if cert_center_certificate_id is not None:
            self.cert_center_certificate_id = cert_center_certificate_id
        if certificate_id is not None:
            self.certificate_id = certificate_id
        if certificate_source is not None:
            self.certificate_source = certificate_source
        if client_address_transmission_protocol is not None:
            self.client_address_transmission_protocol = client_address_transmission_protocol
        if customized_cfg_id is not None:
            self.customized_cfg_id = customized_cfg_id
        if description is not None:
            self.description = description
        if domain_extensions is not None:
            self.domain_extensions = domain_extensions
        if enable_http2 is not None:
            self.enable_http2 = enable_http2
        if enable_quic is not None:
            self.enable_quic = enable_quic
        if enabled is not None:
            self.enabled = enabled
        self.listener_id = listener_id
        if listener_name is not None:
            self.listener_name = listener_name
        if proxy_protocol_disabled is not None:
            self.proxy_protocol_disabled = proxy_protocol_disabled
        if server_group_id is not None:
            self.server_group_id = server_group_id

    @property
    def acl_ids(self):
        """Gets the acl_ids of this ModifyListenerAttributesRequest.  # noqa: E501


        :return: The acl_ids of this ModifyListenerAttributesRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._acl_ids

    @acl_ids.setter
    def acl_ids(self, acl_ids):
        """Sets the acl_ids of this ModifyListenerAttributesRequest.


        :param acl_ids: The acl_ids of this ModifyListenerAttributesRequest.  # noqa: E501
        :type: list[str]
        """

        self._acl_ids = acl_ids

    @property
    def acl_status(self):
        """Gets the acl_status of this ModifyListenerAttributesRequest.  # noqa: E501


        :return: The acl_status of this ModifyListenerAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._acl_status

    @acl_status.setter
    def acl_status(self, acl_status):
        """Sets the acl_status of this ModifyListenerAttributesRequest.


        :param acl_status: The acl_status of this ModifyListenerAttributesRequest.  # noqa: E501
        :type: str
        """

        self._acl_status = acl_status

    @property
    def acl_type(self):
        """Gets the acl_type of this ModifyListenerAttributesRequest.  # noqa: E501


        :return: The acl_type of this ModifyListenerAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._acl_type

    @acl_type.setter
    def acl_type(self, acl_type):
        """Sets the acl_type of this ModifyListenerAttributesRequest.


        :param acl_type: The acl_type of this ModifyListenerAttributesRequest.  # noqa: E501
        :type: str
        """

        self._acl_type = acl_type

    @property
    def ca_certificate_id(self):
        """Gets the ca_certificate_id of this ModifyListenerAttributesRequest.  # noqa: E501


        :return: The ca_certificate_id of this ModifyListenerAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._ca_certificate_id

    @ca_certificate_id.setter
    def ca_certificate_id(self, ca_certificate_id):
        """Sets the ca_certificate_id of this ModifyListenerAttributesRequest.


        :param ca_certificate_id: The ca_certificate_id of this ModifyListenerAttributesRequest.  # noqa: E501
        :type: str
        """

        self._ca_certificate_id = ca_certificate_id

    @property
    def cert_center_certificate_id(self):
        """Gets the cert_center_certificate_id of this ModifyListenerAttributesRequest.  # noqa: E501


        :return: The cert_center_certificate_id of this ModifyListenerAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._cert_center_certificate_id

    @cert_center_certificate_id.setter
    def cert_center_certificate_id(self, cert_center_certificate_id):
        """Sets the cert_center_certificate_id of this ModifyListenerAttributesRequest.


        :param cert_center_certificate_id: The cert_center_certificate_id of this ModifyListenerAttributesRequest.  # noqa: E501
        :type: str
        """

        self._cert_center_certificate_id = cert_center_certificate_id

    @property
    def certificate_id(self):
        """Gets the certificate_id of this ModifyListenerAttributesRequest.  # noqa: E501


        :return: The certificate_id of this ModifyListenerAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        """Sets the certificate_id of this ModifyListenerAttributesRequest.


        :param certificate_id: The certificate_id of this ModifyListenerAttributesRequest.  # noqa: E501
        :type: str
        """

        self._certificate_id = certificate_id

    @property
    def certificate_source(self):
        """Gets the certificate_source of this ModifyListenerAttributesRequest.  # noqa: E501


        :return: The certificate_source of this ModifyListenerAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._certificate_source

    @certificate_source.setter
    def certificate_source(self, certificate_source):
        """Sets the certificate_source of this ModifyListenerAttributesRequest.


        :param certificate_source: The certificate_source of this ModifyListenerAttributesRequest.  # noqa: E501
        :type: str
        """

        self._certificate_source = certificate_source

    @property
    def client_address_transmission_protocol(self):
        """Gets the client_address_transmission_protocol of this ModifyListenerAttributesRequest.  # noqa: E501


        :return: The client_address_transmission_protocol of this ModifyListenerAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_address_transmission_protocol

    @client_address_transmission_protocol.setter
    def client_address_transmission_protocol(self, client_address_transmission_protocol):
        """Sets the client_address_transmission_protocol of this ModifyListenerAttributesRequest.


        :param client_address_transmission_protocol: The client_address_transmission_protocol of this ModifyListenerAttributesRequest.  # noqa: E501
        :type: str
        """

        self._client_address_transmission_protocol = client_address_transmission_protocol

    @property
    def customized_cfg_id(self):
        """Gets the customized_cfg_id of this ModifyListenerAttributesRequest.  # noqa: E501


        :return: The customized_cfg_id of this ModifyListenerAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._customized_cfg_id

    @customized_cfg_id.setter
    def customized_cfg_id(self, customized_cfg_id):
        """Sets the customized_cfg_id of this ModifyListenerAttributesRequest.


        :param customized_cfg_id: The customized_cfg_id of this ModifyListenerAttributesRequest.  # noqa: E501
        :type: str
        """

        self._customized_cfg_id = customized_cfg_id

    @property
    def description(self):
        """Gets the description of this ModifyListenerAttributesRequest.  # noqa: E501


        :return: The description of this ModifyListenerAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ModifyListenerAttributesRequest.


        :param description: The description of this ModifyListenerAttributesRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def domain_extensions(self):
        """Gets the domain_extensions of this ModifyListenerAttributesRequest.  # noqa: E501


        :return: The domain_extensions of this ModifyListenerAttributesRequest.  # noqa: E501
        :rtype: list[DomainExtensionForModifyListenerAttributesInput]
        """
        return self._domain_extensions

    @domain_extensions.setter
    def domain_extensions(self, domain_extensions):
        """Sets the domain_extensions of this ModifyListenerAttributesRequest.


        :param domain_extensions: The domain_extensions of this ModifyListenerAttributesRequest.  # noqa: E501
        :type: list[DomainExtensionForModifyListenerAttributesInput]
        """

        self._domain_extensions = domain_extensions

    @property
    def enable_http2(self):
        """Gets the enable_http2 of this ModifyListenerAttributesRequest.  # noqa: E501


        :return: The enable_http2 of this ModifyListenerAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._enable_http2

    @enable_http2.setter
    def enable_http2(self, enable_http2):
        """Sets the enable_http2 of this ModifyListenerAttributesRequest.


        :param enable_http2: The enable_http2 of this ModifyListenerAttributesRequest.  # noqa: E501
        :type: str
        """

        self._enable_http2 = enable_http2

    @property
    def enable_quic(self):
        """Gets the enable_quic of this ModifyListenerAttributesRequest.  # noqa: E501


        :return: The enable_quic of this ModifyListenerAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._enable_quic

    @enable_quic.setter
    def enable_quic(self, enable_quic):
        """Sets the enable_quic of this ModifyListenerAttributesRequest.


        :param enable_quic: The enable_quic of this ModifyListenerAttributesRequest.  # noqa: E501
        :type: str
        """

        self._enable_quic = enable_quic

    @property
    def enabled(self):
        """Gets the enabled of this ModifyListenerAttributesRequest.  # noqa: E501


        :return: The enabled of this ModifyListenerAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ModifyListenerAttributesRequest.


        :param enabled: The enabled of this ModifyListenerAttributesRequest.  # noqa: E501
        :type: str
        """

        self._enabled = enabled

    @property
    def listener_id(self):
        """Gets the listener_id of this ModifyListenerAttributesRequest.  # noqa: E501


        :return: The listener_id of this ModifyListenerAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._listener_id

    @listener_id.setter
    def listener_id(self, listener_id):
        """Sets the listener_id of this ModifyListenerAttributesRequest.


        :param listener_id: The listener_id of this ModifyListenerAttributesRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and listener_id is None:
            raise ValueError("Invalid value for `listener_id`, must not be `None`")  # noqa: E501

        self._listener_id = listener_id

    @property
    def listener_name(self):
        """Gets the listener_name of this ModifyListenerAttributesRequest.  # noqa: E501


        :return: The listener_name of this ModifyListenerAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._listener_name

    @listener_name.setter
    def listener_name(self, listener_name):
        """Sets the listener_name of this ModifyListenerAttributesRequest.


        :param listener_name: The listener_name of this ModifyListenerAttributesRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                listener_name is not None and len(listener_name) > 128):
            raise ValueError("Invalid value for `listener_name`, length must be less than or equal to `128`")  # noqa: E501
        if (self._configuration.client_side_validation and
                listener_name is not None and len(listener_name) < 1):
            raise ValueError("Invalid value for `listener_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._listener_name = listener_name

    @property
    def proxy_protocol_disabled(self):
        """Gets the proxy_protocol_disabled of this ModifyListenerAttributesRequest.  # noqa: E501


        :return: The proxy_protocol_disabled of this ModifyListenerAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._proxy_protocol_disabled

    @proxy_protocol_disabled.setter
    def proxy_protocol_disabled(self, proxy_protocol_disabled):
        """Sets the proxy_protocol_disabled of this ModifyListenerAttributesRequest.


        :param proxy_protocol_disabled: The proxy_protocol_disabled of this ModifyListenerAttributesRequest.  # noqa: E501
        :type: str
        """

        self._proxy_protocol_disabled = proxy_protocol_disabled

    @property
    def server_group_id(self):
        """Gets the server_group_id of this ModifyListenerAttributesRequest.  # noqa: E501


        :return: The server_group_id of this ModifyListenerAttributesRequest.  # noqa: E501
        :rtype: str
        """
        return self._server_group_id

    @server_group_id.setter
    def server_group_id(self, server_group_id):
        """Sets the server_group_id of this ModifyListenerAttributesRequest.


        :param server_group_id: The server_group_id of this ModifyListenerAttributesRequest.  # noqa: E501
        :type: str
        """

        self._server_group_id = server_group_id

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
        if issubclass(ModifyListenerAttributesRequest, dict):
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
        if not isinstance(other, ModifyListenerAttributesRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ModifyListenerAttributesRequest):
            return True

        return self.to_dict() != other.to_dict()
