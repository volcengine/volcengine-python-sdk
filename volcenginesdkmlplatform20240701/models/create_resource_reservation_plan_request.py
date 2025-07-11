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


class CreateResourceReservationPlanRequest(object):
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
        'compute_resource': 'ComputeResourceForCreateResourceReservationPlanInput',
        'description': 'str',
        'dry_run': 'bool',
        'name': 'str',
        'reservation_config': 'ReservationConfigForCreateResourceReservationPlanInput',
        'storage_config': 'StorageConfigForCreateResourceReservationPlanInput',
        'workload_network_config': 'WorkloadNetworkConfigForCreateResourceReservationPlanInput'
    }

    attribute_map = {
        'compute_resource': 'ComputeResource',
        'description': 'Description',
        'dry_run': 'DryRun',
        'name': 'Name',
        'reservation_config': 'ReservationConfig',
        'storage_config': 'StorageConfig',
        'workload_network_config': 'WorkloadNetworkConfig'
    }

    def __init__(self, compute_resource=None, description=None, dry_run=None, name=None, reservation_config=None, storage_config=None, workload_network_config=None, _configuration=None):  # noqa: E501
        """CreateResourceReservationPlanRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._compute_resource = None
        self._description = None
        self._dry_run = None
        self._name = None
        self._reservation_config = None
        self._storage_config = None
        self._workload_network_config = None
        self.discriminator = None

        if compute_resource is not None:
            self.compute_resource = compute_resource
        if description is not None:
            self.description = description
        if dry_run is not None:
            self.dry_run = dry_run
        self.name = name
        if reservation_config is not None:
            self.reservation_config = reservation_config
        if storage_config is not None:
            self.storage_config = storage_config
        if workload_network_config is not None:
            self.workload_network_config = workload_network_config

    @property
    def compute_resource(self):
        """Gets the compute_resource of this CreateResourceReservationPlanRequest.  # noqa: E501


        :return: The compute_resource of this CreateResourceReservationPlanRequest.  # noqa: E501
        :rtype: ComputeResourceForCreateResourceReservationPlanInput
        """
        return self._compute_resource

    @compute_resource.setter
    def compute_resource(self, compute_resource):
        """Sets the compute_resource of this CreateResourceReservationPlanRequest.


        :param compute_resource: The compute_resource of this CreateResourceReservationPlanRequest.  # noqa: E501
        :type: ComputeResourceForCreateResourceReservationPlanInput
        """

        self._compute_resource = compute_resource

    @property
    def description(self):
        """Gets the description of this CreateResourceReservationPlanRequest.  # noqa: E501


        :return: The description of this CreateResourceReservationPlanRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateResourceReservationPlanRequest.


        :param description: The description of this CreateResourceReservationPlanRequest.  # noqa: E501
        :type: str
        """
        if (self._configuration.client_side_validation and
                description is not None and len(description) > 500):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `500`")  # noqa: E501
        if (self._configuration.client_side_validation and
                description is not None and len(description) < 1):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `1`")  # noqa: E501

        self._description = description

    @property
    def dry_run(self):
        """Gets the dry_run of this CreateResourceReservationPlanRequest.  # noqa: E501


        :return: The dry_run of this CreateResourceReservationPlanRequest.  # noqa: E501
        :rtype: bool
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        """Sets the dry_run of this CreateResourceReservationPlanRequest.


        :param dry_run: The dry_run of this CreateResourceReservationPlanRequest.  # noqa: E501
        :type: bool
        """

        self._dry_run = dry_run

    @property
    def name(self):
        """Gets the name of this CreateResourceReservationPlanRequest.  # noqa: E501


        :return: The name of this CreateResourceReservationPlanRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateResourceReservationPlanRequest.


        :param name: The name of this CreateResourceReservationPlanRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name is not None and len(name) > 200):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `200`")  # noqa: E501
        if (self._configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def reservation_config(self):
        """Gets the reservation_config of this CreateResourceReservationPlanRequest.  # noqa: E501


        :return: The reservation_config of this CreateResourceReservationPlanRequest.  # noqa: E501
        :rtype: ReservationConfigForCreateResourceReservationPlanInput
        """
        return self._reservation_config

    @reservation_config.setter
    def reservation_config(self, reservation_config):
        """Sets the reservation_config of this CreateResourceReservationPlanRequest.


        :param reservation_config: The reservation_config of this CreateResourceReservationPlanRequest.  # noqa: E501
        :type: ReservationConfigForCreateResourceReservationPlanInput
        """

        self._reservation_config = reservation_config

    @property
    def storage_config(self):
        """Gets the storage_config of this CreateResourceReservationPlanRequest.  # noqa: E501


        :return: The storage_config of this CreateResourceReservationPlanRequest.  # noqa: E501
        :rtype: StorageConfigForCreateResourceReservationPlanInput
        """
        return self._storage_config

    @storage_config.setter
    def storage_config(self, storage_config):
        """Sets the storage_config of this CreateResourceReservationPlanRequest.


        :param storage_config: The storage_config of this CreateResourceReservationPlanRequest.  # noqa: E501
        :type: StorageConfigForCreateResourceReservationPlanInput
        """

        self._storage_config = storage_config

    @property
    def workload_network_config(self):
        """Gets the workload_network_config of this CreateResourceReservationPlanRequest.  # noqa: E501


        :return: The workload_network_config of this CreateResourceReservationPlanRequest.  # noqa: E501
        :rtype: WorkloadNetworkConfigForCreateResourceReservationPlanInput
        """
        return self._workload_network_config

    @workload_network_config.setter
    def workload_network_config(self, workload_network_config):
        """Sets the workload_network_config of this CreateResourceReservationPlanRequest.


        :param workload_network_config: The workload_network_config of this CreateResourceReservationPlanRequest.  # noqa: E501
        :type: WorkloadNetworkConfigForCreateResourceReservationPlanInput
        """

        self._workload_network_config = workload_network_config

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
        if issubclass(CreateResourceReservationPlanRequest, dict):
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
        if not isinstance(other, CreateResourceReservationPlanRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateResourceReservationPlanRequest):
            return True

        return self.to_dict() != other.to_dict()
