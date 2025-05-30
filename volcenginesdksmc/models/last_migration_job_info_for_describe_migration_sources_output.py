# coding: utf-8

"""
    smc

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class LastMigrationJobInfoForDescribeMigrationSourcesOutput(object):
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
        'destination_type': 'str',
        'migration_job_id': 'str',
        'migration_job_name': 'str',
        'migration_job_state': 'str',
        'project_name': 'str'
    }

    attribute_map = {
        'destination_type': 'DestinationType',
        'migration_job_id': 'MigrationJobId',
        'migration_job_name': 'MigrationJobName',
        'migration_job_state': 'MigrationJobState',
        'project_name': 'ProjectName'
    }

    def __init__(self, destination_type=None, migration_job_id=None, migration_job_name=None, migration_job_state=None, project_name=None, _configuration=None):  # noqa: E501
        """LastMigrationJobInfoForDescribeMigrationSourcesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._destination_type = None
        self._migration_job_id = None
        self._migration_job_name = None
        self._migration_job_state = None
        self._project_name = None
        self.discriminator = None

        if destination_type is not None:
            self.destination_type = destination_type
        if migration_job_id is not None:
            self.migration_job_id = migration_job_id
        if migration_job_name is not None:
            self.migration_job_name = migration_job_name
        if migration_job_state is not None:
            self.migration_job_state = migration_job_state
        if project_name is not None:
            self.project_name = project_name

    @property
    def destination_type(self):
        """Gets the destination_type of this LastMigrationJobInfoForDescribeMigrationSourcesOutput.  # noqa: E501


        :return: The destination_type of this LastMigrationJobInfoForDescribeMigrationSourcesOutput.  # noqa: E501
        :rtype: str
        """
        return self._destination_type

    @destination_type.setter
    def destination_type(self, destination_type):
        """Sets the destination_type of this LastMigrationJobInfoForDescribeMigrationSourcesOutput.


        :param destination_type: The destination_type of this LastMigrationJobInfoForDescribeMigrationSourcesOutput.  # noqa: E501
        :type: str
        """

        self._destination_type = destination_type

    @property
    def migration_job_id(self):
        """Gets the migration_job_id of this LastMigrationJobInfoForDescribeMigrationSourcesOutput.  # noqa: E501


        :return: The migration_job_id of this LastMigrationJobInfoForDescribeMigrationSourcesOutput.  # noqa: E501
        :rtype: str
        """
        return self._migration_job_id

    @migration_job_id.setter
    def migration_job_id(self, migration_job_id):
        """Sets the migration_job_id of this LastMigrationJobInfoForDescribeMigrationSourcesOutput.


        :param migration_job_id: The migration_job_id of this LastMigrationJobInfoForDescribeMigrationSourcesOutput.  # noqa: E501
        :type: str
        """

        self._migration_job_id = migration_job_id

    @property
    def migration_job_name(self):
        """Gets the migration_job_name of this LastMigrationJobInfoForDescribeMigrationSourcesOutput.  # noqa: E501


        :return: The migration_job_name of this LastMigrationJobInfoForDescribeMigrationSourcesOutput.  # noqa: E501
        :rtype: str
        """
        return self._migration_job_name

    @migration_job_name.setter
    def migration_job_name(self, migration_job_name):
        """Sets the migration_job_name of this LastMigrationJobInfoForDescribeMigrationSourcesOutput.


        :param migration_job_name: The migration_job_name of this LastMigrationJobInfoForDescribeMigrationSourcesOutput.  # noqa: E501
        :type: str
        """

        self._migration_job_name = migration_job_name

    @property
    def migration_job_state(self):
        """Gets the migration_job_state of this LastMigrationJobInfoForDescribeMigrationSourcesOutput.  # noqa: E501


        :return: The migration_job_state of this LastMigrationJobInfoForDescribeMigrationSourcesOutput.  # noqa: E501
        :rtype: str
        """
        return self._migration_job_state

    @migration_job_state.setter
    def migration_job_state(self, migration_job_state):
        """Sets the migration_job_state of this LastMigrationJobInfoForDescribeMigrationSourcesOutput.


        :param migration_job_state: The migration_job_state of this LastMigrationJobInfoForDescribeMigrationSourcesOutput.  # noqa: E501
        :type: str
        """

        self._migration_job_state = migration_job_state

    @property
    def project_name(self):
        """Gets the project_name of this LastMigrationJobInfoForDescribeMigrationSourcesOutput.  # noqa: E501


        :return: The project_name of this LastMigrationJobInfoForDescribeMigrationSourcesOutput.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this LastMigrationJobInfoForDescribeMigrationSourcesOutput.


        :param project_name: The project_name of this LastMigrationJobInfoForDescribeMigrationSourcesOutput.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

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
        if issubclass(LastMigrationJobInfoForDescribeMigrationSourcesOutput, dict):
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
        if not isinstance(other, LastMigrationJobInfoForDescribeMigrationSourcesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, LastMigrationJobInfoForDescribeMigrationSourcesOutput):
            return True

        return self.to_dict() != other.to_dict()
