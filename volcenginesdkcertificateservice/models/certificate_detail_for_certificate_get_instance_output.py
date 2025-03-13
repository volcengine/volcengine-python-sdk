# coding: utf-8

"""
    certificate_service

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class CertificateDetailForCertificateGetInstanceOutput(object):
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
        'chain': 'list[str]',
        'finger_print_sha1': 'str',
        'finger_print_sha256': 'str',
        'issuer': 'IssuerForCertificateGetInstanceOutput',
        'key_algorithm': 'str',
        'private_key': 'str',
        'serial_number': 'str',
        'signature_algorithm': 'str',
        'subject': 'SubjectForCertificateGetInstanceOutput'
    }

    attribute_map = {
        'chain': 'Chain',
        'finger_print_sha1': 'FingerPrintSha1',
        'finger_print_sha256': 'FingerPrintSha256',
        'issuer': 'Issuer',
        'key_algorithm': 'KeyAlgorithm',
        'private_key': 'PrivateKey',
        'serial_number': 'SerialNumber',
        'signature_algorithm': 'SignatureAlgorithm',
        'subject': 'Subject'
    }

    def __init__(self, chain=None, finger_print_sha1=None, finger_print_sha256=None, issuer=None, key_algorithm=None, private_key=None, serial_number=None, signature_algorithm=None, subject=None, _configuration=None):  # noqa: E501
        """CertificateDetailForCertificateGetInstanceOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._chain = None
        self._finger_print_sha1 = None
        self._finger_print_sha256 = None
        self._issuer = None
        self._key_algorithm = None
        self._private_key = None
        self._serial_number = None
        self._signature_algorithm = None
        self._subject = None
        self.discriminator = None

        if chain is not None:
            self.chain = chain
        if finger_print_sha1 is not None:
            self.finger_print_sha1 = finger_print_sha1
        if finger_print_sha256 is not None:
            self.finger_print_sha256 = finger_print_sha256
        if issuer is not None:
            self.issuer = issuer
        if key_algorithm is not None:
            self.key_algorithm = key_algorithm
        if private_key is not None:
            self.private_key = private_key
        if serial_number is not None:
            self.serial_number = serial_number
        if signature_algorithm is not None:
            self.signature_algorithm = signature_algorithm
        if subject is not None:
            self.subject = subject

    @property
    def chain(self):
        """Gets the chain of this CertificateDetailForCertificateGetInstanceOutput.  # noqa: E501


        :return: The chain of this CertificateDetailForCertificateGetInstanceOutput.  # noqa: E501
        :rtype: list[str]
        """
        return self._chain

    @chain.setter
    def chain(self, chain):
        """Sets the chain of this CertificateDetailForCertificateGetInstanceOutput.


        :param chain: The chain of this CertificateDetailForCertificateGetInstanceOutput.  # noqa: E501
        :type: list[str]
        """

        self._chain = chain

    @property
    def finger_print_sha1(self):
        """Gets the finger_print_sha1 of this CertificateDetailForCertificateGetInstanceOutput.  # noqa: E501


        :return: The finger_print_sha1 of this CertificateDetailForCertificateGetInstanceOutput.  # noqa: E501
        :rtype: str
        """
        return self._finger_print_sha1

    @finger_print_sha1.setter
    def finger_print_sha1(self, finger_print_sha1):
        """Sets the finger_print_sha1 of this CertificateDetailForCertificateGetInstanceOutput.


        :param finger_print_sha1: The finger_print_sha1 of this CertificateDetailForCertificateGetInstanceOutput.  # noqa: E501
        :type: str
        """

        self._finger_print_sha1 = finger_print_sha1

    @property
    def finger_print_sha256(self):
        """Gets the finger_print_sha256 of this CertificateDetailForCertificateGetInstanceOutput.  # noqa: E501


        :return: The finger_print_sha256 of this CertificateDetailForCertificateGetInstanceOutput.  # noqa: E501
        :rtype: str
        """
        return self._finger_print_sha256

    @finger_print_sha256.setter
    def finger_print_sha256(self, finger_print_sha256):
        """Sets the finger_print_sha256 of this CertificateDetailForCertificateGetInstanceOutput.


        :param finger_print_sha256: The finger_print_sha256 of this CertificateDetailForCertificateGetInstanceOutput.  # noqa: E501
        :type: str
        """

        self._finger_print_sha256 = finger_print_sha256

    @property
    def issuer(self):
        """Gets the issuer of this CertificateDetailForCertificateGetInstanceOutput.  # noqa: E501


        :return: The issuer of this CertificateDetailForCertificateGetInstanceOutput.  # noqa: E501
        :rtype: IssuerForCertificateGetInstanceOutput
        """
        return self._issuer

    @issuer.setter
    def issuer(self, issuer):
        """Sets the issuer of this CertificateDetailForCertificateGetInstanceOutput.


        :param issuer: The issuer of this CertificateDetailForCertificateGetInstanceOutput.  # noqa: E501
        :type: IssuerForCertificateGetInstanceOutput
        """

        self._issuer = issuer

    @property
    def key_algorithm(self):
        """Gets the key_algorithm of this CertificateDetailForCertificateGetInstanceOutput.  # noqa: E501


        :return: The key_algorithm of this CertificateDetailForCertificateGetInstanceOutput.  # noqa: E501
        :rtype: str
        """
        return self._key_algorithm

    @key_algorithm.setter
    def key_algorithm(self, key_algorithm):
        """Sets the key_algorithm of this CertificateDetailForCertificateGetInstanceOutput.


        :param key_algorithm: The key_algorithm of this CertificateDetailForCertificateGetInstanceOutput.  # noqa: E501
        :type: str
        """

        self._key_algorithm = key_algorithm

    @property
    def private_key(self):
        """Gets the private_key of this CertificateDetailForCertificateGetInstanceOutput.  # noqa: E501


        :return: The private_key of this CertificateDetailForCertificateGetInstanceOutput.  # noqa: E501
        :rtype: str
        """
        return self._private_key

    @private_key.setter
    def private_key(self, private_key):
        """Sets the private_key of this CertificateDetailForCertificateGetInstanceOutput.


        :param private_key: The private_key of this CertificateDetailForCertificateGetInstanceOutput.  # noqa: E501
        :type: str
        """

        self._private_key = private_key

    @property
    def serial_number(self):
        """Gets the serial_number of this CertificateDetailForCertificateGetInstanceOutput.  # noqa: E501


        :return: The serial_number of this CertificateDetailForCertificateGetInstanceOutput.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this CertificateDetailForCertificateGetInstanceOutput.


        :param serial_number: The serial_number of this CertificateDetailForCertificateGetInstanceOutput.  # noqa: E501
        :type: str
        """

        self._serial_number = serial_number

    @property
    def signature_algorithm(self):
        """Gets the signature_algorithm of this CertificateDetailForCertificateGetInstanceOutput.  # noqa: E501


        :return: The signature_algorithm of this CertificateDetailForCertificateGetInstanceOutput.  # noqa: E501
        :rtype: str
        """
        return self._signature_algorithm

    @signature_algorithm.setter
    def signature_algorithm(self, signature_algorithm):
        """Sets the signature_algorithm of this CertificateDetailForCertificateGetInstanceOutput.


        :param signature_algorithm: The signature_algorithm of this CertificateDetailForCertificateGetInstanceOutput.  # noqa: E501
        :type: str
        """

        self._signature_algorithm = signature_algorithm

    @property
    def subject(self):
        """Gets the subject of this CertificateDetailForCertificateGetInstanceOutput.  # noqa: E501


        :return: The subject of this CertificateDetailForCertificateGetInstanceOutput.  # noqa: E501
        :rtype: SubjectForCertificateGetInstanceOutput
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this CertificateDetailForCertificateGetInstanceOutput.


        :param subject: The subject of this CertificateDetailForCertificateGetInstanceOutput.  # noqa: E501
        :type: SubjectForCertificateGetInstanceOutput
        """

        self._subject = subject

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
        if issubclass(CertificateDetailForCertificateGetInstanceOutput, dict):
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
        if not isinstance(other, CertificateDetailForCertificateGetInstanceOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CertificateDetailForCertificateGetInstanceOutput):
            return True

        return self.to_dict() != other.to_dict()
