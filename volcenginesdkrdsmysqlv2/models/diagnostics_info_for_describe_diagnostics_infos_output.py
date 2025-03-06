# coding: utf-8

"""
    rds_mysql_v2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DiagnosticsInfoForDescribeDiagnosticsInfosOutput(object):
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
        'diagnostics_items': 'list[DiagnosticsItemForDescribeDiagnosticsInfosOutput]',
        'diagnostics_record_id': 'str',
        'diagnostics_result': 'str',
        'ecs_info': 'EcsInfoForDescribeDiagnosticsInfosOutput',
        'endpoint_info': 'EndpointInfoForDescribeDiagnosticsInfosOutput',
        'instance_id': 'str',
        'public_address_info': 'PublicAddressInfoForDescribeDiagnosticsInfosOutput'
    }

    attribute_map = {
        'diagnostics_items': 'DiagnosticsItems',
        'diagnostics_record_id': 'DiagnosticsRecordId',
        'diagnostics_result': 'DiagnosticsResult',
        'ecs_info': 'EcsInfo',
        'endpoint_info': 'EndpointInfo',
        'instance_id': 'InstanceId',
        'public_address_info': 'PublicAddressInfo'
    }

    def __init__(self, diagnostics_items=None, diagnostics_record_id=None, diagnostics_result=None, ecs_info=None, endpoint_info=None, instance_id=None, public_address_info=None, _configuration=None):  # noqa: E501
        """DiagnosticsInfoForDescribeDiagnosticsInfosOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._diagnostics_items = None
        self._diagnostics_record_id = None
        self._diagnostics_result = None
        self._ecs_info = None
        self._endpoint_info = None
        self._instance_id = None
        self._public_address_info = None
        self.discriminator = None

        if diagnostics_items is not None:
            self.diagnostics_items = diagnostics_items
        if diagnostics_record_id is not None:
            self.diagnostics_record_id = diagnostics_record_id
        if diagnostics_result is not None:
            self.diagnostics_result = diagnostics_result
        if ecs_info is not None:
            self.ecs_info = ecs_info
        if endpoint_info is not None:
            self.endpoint_info = endpoint_info
        if instance_id is not None:
            self.instance_id = instance_id
        if public_address_info is not None:
            self.public_address_info = public_address_info

    @property
    def diagnostics_items(self):
        """Gets the diagnostics_items of this DiagnosticsInfoForDescribeDiagnosticsInfosOutput.  # noqa: E501


        :return: The diagnostics_items of this DiagnosticsInfoForDescribeDiagnosticsInfosOutput.  # noqa: E501
        :rtype: list[DiagnosticsItemForDescribeDiagnosticsInfosOutput]
        """
        return self._diagnostics_items

    @diagnostics_items.setter
    def diagnostics_items(self, diagnostics_items):
        """Sets the diagnostics_items of this DiagnosticsInfoForDescribeDiagnosticsInfosOutput.


        :param diagnostics_items: The diagnostics_items of this DiagnosticsInfoForDescribeDiagnosticsInfosOutput.  # noqa: E501
        :type: list[DiagnosticsItemForDescribeDiagnosticsInfosOutput]
        """

        self._diagnostics_items = diagnostics_items

    @property
    def diagnostics_record_id(self):
        """Gets the diagnostics_record_id of this DiagnosticsInfoForDescribeDiagnosticsInfosOutput.  # noqa: E501


        :return: The diagnostics_record_id of this DiagnosticsInfoForDescribeDiagnosticsInfosOutput.  # noqa: E501
        :rtype: str
        """
        return self._diagnostics_record_id

    @diagnostics_record_id.setter
    def diagnostics_record_id(self, diagnostics_record_id):
        """Sets the diagnostics_record_id of this DiagnosticsInfoForDescribeDiagnosticsInfosOutput.


        :param diagnostics_record_id: The diagnostics_record_id of this DiagnosticsInfoForDescribeDiagnosticsInfosOutput.  # noqa: E501
        :type: str
        """

        self._diagnostics_record_id = diagnostics_record_id

    @property
    def diagnostics_result(self):
        """Gets the diagnostics_result of this DiagnosticsInfoForDescribeDiagnosticsInfosOutput.  # noqa: E501


        :return: The diagnostics_result of this DiagnosticsInfoForDescribeDiagnosticsInfosOutput.  # noqa: E501
        :rtype: str
        """
        return self._diagnostics_result

    @diagnostics_result.setter
    def diagnostics_result(self, diagnostics_result):
        """Sets the diagnostics_result of this DiagnosticsInfoForDescribeDiagnosticsInfosOutput.


        :param diagnostics_result: The diagnostics_result of this DiagnosticsInfoForDescribeDiagnosticsInfosOutput.  # noqa: E501
        :type: str
        """

        self._diagnostics_result = diagnostics_result

    @property
    def ecs_info(self):
        """Gets the ecs_info of this DiagnosticsInfoForDescribeDiagnosticsInfosOutput.  # noqa: E501


        :return: The ecs_info of this DiagnosticsInfoForDescribeDiagnosticsInfosOutput.  # noqa: E501
        :rtype: EcsInfoForDescribeDiagnosticsInfosOutput
        """
        return self._ecs_info

    @ecs_info.setter
    def ecs_info(self, ecs_info):
        """Sets the ecs_info of this DiagnosticsInfoForDescribeDiagnosticsInfosOutput.


        :param ecs_info: The ecs_info of this DiagnosticsInfoForDescribeDiagnosticsInfosOutput.  # noqa: E501
        :type: EcsInfoForDescribeDiagnosticsInfosOutput
        """

        self._ecs_info = ecs_info

    @property
    def endpoint_info(self):
        """Gets the endpoint_info of this DiagnosticsInfoForDescribeDiagnosticsInfosOutput.  # noqa: E501


        :return: The endpoint_info of this DiagnosticsInfoForDescribeDiagnosticsInfosOutput.  # noqa: E501
        :rtype: EndpointInfoForDescribeDiagnosticsInfosOutput
        """
        return self._endpoint_info

    @endpoint_info.setter
    def endpoint_info(self, endpoint_info):
        """Sets the endpoint_info of this DiagnosticsInfoForDescribeDiagnosticsInfosOutput.


        :param endpoint_info: The endpoint_info of this DiagnosticsInfoForDescribeDiagnosticsInfosOutput.  # noqa: E501
        :type: EndpointInfoForDescribeDiagnosticsInfosOutput
        """

        self._endpoint_info = endpoint_info

    @property
    def instance_id(self):
        """Gets the instance_id of this DiagnosticsInfoForDescribeDiagnosticsInfosOutput.  # noqa: E501


        :return: The instance_id of this DiagnosticsInfoForDescribeDiagnosticsInfosOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this DiagnosticsInfoForDescribeDiagnosticsInfosOutput.


        :param instance_id: The instance_id of this DiagnosticsInfoForDescribeDiagnosticsInfosOutput.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def public_address_info(self):
        """Gets the public_address_info of this DiagnosticsInfoForDescribeDiagnosticsInfosOutput.  # noqa: E501


        :return: The public_address_info of this DiagnosticsInfoForDescribeDiagnosticsInfosOutput.  # noqa: E501
        :rtype: PublicAddressInfoForDescribeDiagnosticsInfosOutput
        """
        return self._public_address_info

    @public_address_info.setter
    def public_address_info(self, public_address_info):
        """Sets the public_address_info of this DiagnosticsInfoForDescribeDiagnosticsInfosOutput.


        :param public_address_info: The public_address_info of this DiagnosticsInfoForDescribeDiagnosticsInfosOutput.  # noqa: E501
        :type: PublicAddressInfoForDescribeDiagnosticsInfosOutput
        """

        self._public_address_info = public_address_info

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
        if issubclass(DiagnosticsInfoForDescribeDiagnosticsInfosOutput, dict):
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
        if not isinstance(other, DiagnosticsInfoForDescribeDiagnosticsInfosOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DiagnosticsInfoForDescribeDiagnosticsInfosOutput):
            return True

        return self.to_dict() != other.to_dict()
