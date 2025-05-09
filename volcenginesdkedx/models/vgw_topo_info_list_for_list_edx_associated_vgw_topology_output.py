# coding: utf-8

"""
    edx

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class VGWTopoInfoListForListEDXAssociatedVGWTopologyOutput(object):
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
        'cluster': 'ClusterForListEDXAssociatedVGWTopologyOutput',
        'instance_id': 'str',
        'instance_name': 'str',
        'type': 'str',
        'x_coordinate': 'int',
        'y_coordinate': 'int'
    }

    attribute_map = {
        'cluster': 'Cluster',
        'instance_id': 'InstanceId',
        'instance_name': 'InstanceName',
        'type': 'Type',
        'x_coordinate': 'XCoordinate',
        'y_coordinate': 'YCoordinate'
    }

    def __init__(self, cluster=None, instance_id=None, instance_name=None, type=None, x_coordinate=None, y_coordinate=None, _configuration=None):  # noqa: E501
        """VGWTopoInfoListForListEDXAssociatedVGWTopologyOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._cluster = None
        self._instance_id = None
        self._instance_name = None
        self._type = None
        self._x_coordinate = None
        self._y_coordinate = None
        self.discriminator = None

        if cluster is not None:
            self.cluster = cluster
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if type is not None:
            self.type = type
        if x_coordinate is not None:
            self.x_coordinate = x_coordinate
        if y_coordinate is not None:
            self.y_coordinate = y_coordinate

    @property
    def cluster(self):
        """Gets the cluster of this VGWTopoInfoListForListEDXAssociatedVGWTopologyOutput.  # noqa: E501


        :return: The cluster of this VGWTopoInfoListForListEDXAssociatedVGWTopologyOutput.  # noqa: E501
        :rtype: ClusterForListEDXAssociatedVGWTopologyOutput
        """
        return self._cluster

    @cluster.setter
    def cluster(self, cluster):
        """Sets the cluster of this VGWTopoInfoListForListEDXAssociatedVGWTopologyOutput.


        :param cluster: The cluster of this VGWTopoInfoListForListEDXAssociatedVGWTopologyOutput.  # noqa: E501
        :type: ClusterForListEDXAssociatedVGWTopologyOutput
        """

        self._cluster = cluster

    @property
    def instance_id(self):
        """Gets the instance_id of this VGWTopoInfoListForListEDXAssociatedVGWTopologyOutput.  # noqa: E501


        :return: The instance_id of this VGWTopoInfoListForListEDXAssociatedVGWTopologyOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this VGWTopoInfoListForListEDXAssociatedVGWTopologyOutput.


        :param instance_id: The instance_id of this VGWTopoInfoListForListEDXAssociatedVGWTopologyOutput.  # noqa: E501
        :type: str
        """

        self._instance_id = instance_id

    @property
    def instance_name(self):
        """Gets the instance_name of this VGWTopoInfoListForListEDXAssociatedVGWTopologyOutput.  # noqa: E501


        :return: The instance_name of this VGWTopoInfoListForListEDXAssociatedVGWTopologyOutput.  # noqa: E501
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        """Sets the instance_name of this VGWTopoInfoListForListEDXAssociatedVGWTopologyOutput.


        :param instance_name: The instance_name of this VGWTopoInfoListForListEDXAssociatedVGWTopologyOutput.  # noqa: E501
        :type: str
        """

        self._instance_name = instance_name

    @property
    def type(self):
        """Gets the type of this VGWTopoInfoListForListEDXAssociatedVGWTopologyOutput.  # noqa: E501


        :return: The type of this VGWTopoInfoListForListEDXAssociatedVGWTopologyOutput.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VGWTopoInfoListForListEDXAssociatedVGWTopologyOutput.


        :param type: The type of this VGWTopoInfoListForListEDXAssociatedVGWTopologyOutput.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def x_coordinate(self):
        """Gets the x_coordinate of this VGWTopoInfoListForListEDXAssociatedVGWTopologyOutput.  # noqa: E501


        :return: The x_coordinate of this VGWTopoInfoListForListEDXAssociatedVGWTopologyOutput.  # noqa: E501
        :rtype: int
        """
        return self._x_coordinate

    @x_coordinate.setter
    def x_coordinate(self, x_coordinate):
        """Sets the x_coordinate of this VGWTopoInfoListForListEDXAssociatedVGWTopologyOutput.


        :param x_coordinate: The x_coordinate of this VGWTopoInfoListForListEDXAssociatedVGWTopologyOutput.  # noqa: E501
        :type: int
        """

        self._x_coordinate = x_coordinate

    @property
    def y_coordinate(self):
        """Gets the y_coordinate of this VGWTopoInfoListForListEDXAssociatedVGWTopologyOutput.  # noqa: E501


        :return: The y_coordinate of this VGWTopoInfoListForListEDXAssociatedVGWTopologyOutput.  # noqa: E501
        :rtype: int
        """
        return self._y_coordinate

    @y_coordinate.setter
    def y_coordinate(self, y_coordinate):
        """Sets the y_coordinate of this VGWTopoInfoListForListEDXAssociatedVGWTopologyOutput.


        :param y_coordinate: The y_coordinate of this VGWTopoInfoListForListEDXAssociatedVGWTopologyOutput.  # noqa: E501
        :type: int
        """

        self._y_coordinate = y_coordinate

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
        if issubclass(VGWTopoInfoListForListEDXAssociatedVGWTopologyOutput, dict):
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
        if not isinstance(other, VGWTopoInfoListForListEDXAssociatedVGWTopologyOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VGWTopoInfoListForListEDXAssociatedVGWTopologyOutput):
            return True

        return self.to_dict() != other.to_dict()
