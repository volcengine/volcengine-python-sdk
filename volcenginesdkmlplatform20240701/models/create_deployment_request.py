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


class CreateDeploymentRequest(object):
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
        'accept_service_traffic': 'bool',
        'apig_config': 'ApigConfigForCreateDeploymentInput',
        'clb_config': 'CLBConfigForCreateDeploymentInput',
        'deployment_name': 'str',
        'description': 'str',
        'dry_run': 'bool',
        'priority': 'int',
        'resource_queue_id': 'str',
        'roles': 'list[RoleForCreateDeploymentInput]',
        'service_id': 'str'
    }

    attribute_map = {
        'accept_service_traffic': 'AcceptServiceTraffic',
        'apig_config': 'ApigConfig',
        'clb_config': 'CLBConfig',
        'deployment_name': 'DeploymentName',
        'description': 'Description',
        'dry_run': 'DryRun',
        'priority': 'Priority',
        'resource_queue_id': 'ResourceQueueId',
        'roles': 'Roles',
        'service_id': 'ServiceId'
    }

    def __init__(self, accept_service_traffic=None, apig_config=None, clb_config=None, deployment_name=None, description=None, dry_run=None, priority=None, resource_queue_id=None, roles=None, service_id=None, _configuration=None):  # noqa: E501
        """CreateDeploymentRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._accept_service_traffic = None
        self._apig_config = None
        self._clb_config = None
        self._deployment_name = None
        self._description = None
        self._dry_run = None
        self._priority = None
        self._resource_queue_id = None
        self._roles = None
        self._service_id = None
        self.discriminator = None

        if accept_service_traffic is not None:
            self.accept_service_traffic = accept_service_traffic
        if apig_config is not None:
            self.apig_config = apig_config
        if clb_config is not None:
            self.clb_config = clb_config
        self.deployment_name = deployment_name
        if description is not None:
            self.description = description
        if dry_run is not None:
            self.dry_run = dry_run
        if priority is not None:
            self.priority = priority
        self.resource_queue_id = resource_queue_id
        if roles is not None:
            self.roles = roles
        self.service_id = service_id

    @property
    def accept_service_traffic(self):
        """Gets the accept_service_traffic of this CreateDeploymentRequest.  # noqa: E501


        :return: The accept_service_traffic of this CreateDeploymentRequest.  # noqa: E501
        :rtype: bool
        """
        return self._accept_service_traffic

    @accept_service_traffic.setter
    def accept_service_traffic(self, accept_service_traffic):
        """Sets the accept_service_traffic of this CreateDeploymentRequest.


        :param accept_service_traffic: The accept_service_traffic of this CreateDeploymentRequest.  # noqa: E501
        :type: bool
        """

        self._accept_service_traffic = accept_service_traffic

    @property
    def apig_config(self):
        """Gets the apig_config of this CreateDeploymentRequest.  # noqa: E501


        :return: The apig_config of this CreateDeploymentRequest.  # noqa: E501
        :rtype: ApigConfigForCreateDeploymentInput
        """
        return self._apig_config

    @apig_config.setter
    def apig_config(self, apig_config):
        """Sets the apig_config of this CreateDeploymentRequest.


        :param apig_config: The apig_config of this CreateDeploymentRequest.  # noqa: E501
        :type: ApigConfigForCreateDeploymentInput
        """

        self._apig_config = apig_config

    @property
    def clb_config(self):
        """Gets the clb_config of this CreateDeploymentRequest.  # noqa: E501


        :return: The clb_config of this CreateDeploymentRequest.  # noqa: E501
        :rtype: CLBConfigForCreateDeploymentInput
        """
        return self._clb_config

    @clb_config.setter
    def clb_config(self, clb_config):
        """Sets the clb_config of this CreateDeploymentRequest.


        :param clb_config: The clb_config of this CreateDeploymentRequest.  # noqa: E501
        :type: CLBConfigForCreateDeploymentInput
        """

        self._clb_config = clb_config

    @property
    def deployment_name(self):
        """Gets the deployment_name of this CreateDeploymentRequest.  # noqa: E501


        :return: The deployment_name of this CreateDeploymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._deployment_name

    @deployment_name.setter
    def deployment_name(self, deployment_name):
        """Sets the deployment_name of this CreateDeploymentRequest.


        :param deployment_name: The deployment_name of this CreateDeploymentRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and deployment_name is None:
            raise ValueError("Invalid value for `deployment_name`, must not be `None`")  # noqa: E501

        self._deployment_name = deployment_name

    @property
    def description(self):
        """Gets the description of this CreateDeploymentRequest.  # noqa: E501


        :return: The description of this CreateDeploymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateDeploymentRequest.


        :param description: The description of this CreateDeploymentRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def dry_run(self):
        """Gets the dry_run of this CreateDeploymentRequest.  # noqa: E501


        :return: The dry_run of this CreateDeploymentRequest.  # noqa: E501
        :rtype: bool
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        """Sets the dry_run of this CreateDeploymentRequest.


        :param dry_run: The dry_run of this CreateDeploymentRequest.  # noqa: E501
        :type: bool
        """

        self._dry_run = dry_run

    @property
    def priority(self):
        """Gets the priority of this CreateDeploymentRequest.  # noqa: E501


        :return: The priority of this CreateDeploymentRequest.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this CreateDeploymentRequest.


        :param priority: The priority of this CreateDeploymentRequest.  # noqa: E501
        :type: int
        """

        self._priority = priority

    @property
    def resource_queue_id(self):
        """Gets the resource_queue_id of this CreateDeploymentRequest.  # noqa: E501


        :return: The resource_queue_id of this CreateDeploymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._resource_queue_id

    @resource_queue_id.setter
    def resource_queue_id(self, resource_queue_id):
        """Sets the resource_queue_id of this CreateDeploymentRequest.


        :param resource_queue_id: The resource_queue_id of this CreateDeploymentRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and resource_queue_id is None:
            raise ValueError("Invalid value for `resource_queue_id`, must not be `None`")  # noqa: E501

        self._resource_queue_id = resource_queue_id

    @property
    def roles(self):
        """Gets the roles of this CreateDeploymentRequest.  # noqa: E501


        :return: The roles of this CreateDeploymentRequest.  # noqa: E501
        :rtype: list[RoleForCreateDeploymentInput]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this CreateDeploymentRequest.


        :param roles: The roles of this CreateDeploymentRequest.  # noqa: E501
        :type: list[RoleForCreateDeploymentInput]
        """

        self._roles = roles

    @property
    def service_id(self):
        """Gets the service_id of this CreateDeploymentRequest.  # noqa: E501


        :return: The service_id of this CreateDeploymentRequest.  # noqa: E501
        :rtype: str
        """
        return self._service_id

    @service_id.setter
    def service_id(self, service_id):
        """Sets the service_id of this CreateDeploymentRequest.


        :param service_id: The service_id of this CreateDeploymentRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and service_id is None:
            raise ValueError("Invalid value for `service_id`, must not be `None`")  # noqa: E501

        self._service_id = service_id

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
        if issubclass(CreateDeploymentRequest, dict):
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
        if not isinstance(other, CreateDeploymentRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreateDeploymentRequest):
            return True

        return self.to_dict() != other.to_dict()
