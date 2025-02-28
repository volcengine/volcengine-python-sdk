# coding: utf-8

"""
    flink20250101

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class AppForStartApplicationInstanceInput(object):
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
        'account_id': 'str',
        'args': 'str',
        'conf': 'str',
        'dependency': 'DependencyForStartApplicationInstanceInput',
        'deploy_request': 'DeployRequestForStartApplicationInstanceInput',
        'engine_version': 'str',
        'jar': 'str',
        'job_name': 'str',
        'job_type': 'str',
        'main_class': 'str',
        'project_id': 'str',
        'sql_text': 'str',
        'unique_key': 'str',
        'user_id': 'str'
    }

    attribute_map = {
        'account_id': 'AccountId',
        'args': 'Args',
        'conf': 'Conf',
        'dependency': 'Dependency',
        'deploy_request': 'DeployRequest',
        'engine_version': 'EngineVersion',
        'jar': 'Jar',
        'job_name': 'JobName',
        'job_type': 'JobType',
        'main_class': 'MainClass',
        'project_id': 'ProjectId',
        'sql_text': 'SqlText',
        'unique_key': 'UniqueKey',
        'user_id': 'UserId'
    }

    def __init__(self, account_id=None, args=None, conf=None, dependency=None, deploy_request=None, engine_version=None, jar=None, job_name=None, job_type=None, main_class=None, project_id=None, sql_text=None, unique_key=None, user_id=None, _configuration=None):  # noqa: E501
        """AppForStartApplicationInstanceInput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_id = None
        self._args = None
        self._conf = None
        self._dependency = None
        self._deploy_request = None
        self._engine_version = None
        self._jar = None
        self._job_name = None
        self._job_type = None
        self._main_class = None
        self._project_id = None
        self._sql_text = None
        self._unique_key = None
        self._user_id = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if args is not None:
            self.args = args
        if conf is not None:
            self.conf = conf
        if dependency is not None:
            self.dependency = dependency
        if deploy_request is not None:
            self.deploy_request = deploy_request
        if engine_version is not None:
            self.engine_version = engine_version
        if jar is not None:
            self.jar = jar
        if job_name is not None:
            self.job_name = job_name
        if job_type is not None:
            self.job_type = job_type
        if main_class is not None:
            self.main_class = main_class
        if project_id is not None:
            self.project_id = project_id
        if sql_text is not None:
            self.sql_text = sql_text
        if unique_key is not None:
            self.unique_key = unique_key
        if user_id is not None:
            self.user_id = user_id

    @property
    def account_id(self):
        """Gets the account_id of this AppForStartApplicationInstanceInput.  # noqa: E501


        :return: The account_id of this AppForStartApplicationInstanceInput.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this AppForStartApplicationInstanceInput.


        :param account_id: The account_id of this AppForStartApplicationInstanceInput.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def args(self):
        """Gets the args of this AppForStartApplicationInstanceInput.  # noqa: E501


        :return: The args of this AppForStartApplicationInstanceInput.  # noqa: E501
        :rtype: str
        """
        return self._args

    @args.setter
    def args(self, args):
        """Sets the args of this AppForStartApplicationInstanceInput.


        :param args: The args of this AppForStartApplicationInstanceInput.  # noqa: E501
        :type: str
        """

        self._args = args

    @property
    def conf(self):
        """Gets the conf of this AppForStartApplicationInstanceInput.  # noqa: E501


        :return: The conf of this AppForStartApplicationInstanceInput.  # noqa: E501
        :rtype: str
        """
        return self._conf

    @conf.setter
    def conf(self, conf):
        """Sets the conf of this AppForStartApplicationInstanceInput.


        :param conf: The conf of this AppForStartApplicationInstanceInput.  # noqa: E501
        :type: str
        """

        self._conf = conf

    @property
    def dependency(self):
        """Gets the dependency of this AppForStartApplicationInstanceInput.  # noqa: E501


        :return: The dependency of this AppForStartApplicationInstanceInput.  # noqa: E501
        :rtype: DependencyForStartApplicationInstanceInput
        """
        return self._dependency

    @dependency.setter
    def dependency(self, dependency):
        """Sets the dependency of this AppForStartApplicationInstanceInput.


        :param dependency: The dependency of this AppForStartApplicationInstanceInput.  # noqa: E501
        :type: DependencyForStartApplicationInstanceInput
        """

        self._dependency = dependency

    @property
    def deploy_request(self):
        """Gets the deploy_request of this AppForStartApplicationInstanceInput.  # noqa: E501


        :return: The deploy_request of this AppForStartApplicationInstanceInput.  # noqa: E501
        :rtype: DeployRequestForStartApplicationInstanceInput
        """
        return self._deploy_request

    @deploy_request.setter
    def deploy_request(self, deploy_request):
        """Sets the deploy_request of this AppForStartApplicationInstanceInput.


        :param deploy_request: The deploy_request of this AppForStartApplicationInstanceInput.  # noqa: E501
        :type: DeployRequestForStartApplicationInstanceInput
        """

        self._deploy_request = deploy_request

    @property
    def engine_version(self):
        """Gets the engine_version of this AppForStartApplicationInstanceInput.  # noqa: E501


        :return: The engine_version of this AppForStartApplicationInstanceInput.  # noqa: E501
        :rtype: str
        """
        return self._engine_version

    @engine_version.setter
    def engine_version(self, engine_version):
        """Sets the engine_version of this AppForStartApplicationInstanceInput.


        :param engine_version: The engine_version of this AppForStartApplicationInstanceInput.  # noqa: E501
        :type: str
        """
        allowed_values = ["FLINK_VERSION_1_11", "FLINK_VERSION_1_16"]  # noqa: E501
        if (self._configuration.client_side_validation and
                engine_version not in allowed_values):
            raise ValueError(
                "Invalid value for `engine_version` ({0}), must be one of {1}"  # noqa: E501
                .format(engine_version, allowed_values)
            )

        self._engine_version = engine_version

    @property
    def jar(self):
        """Gets the jar of this AppForStartApplicationInstanceInput.  # noqa: E501


        :return: The jar of this AppForStartApplicationInstanceInput.  # noqa: E501
        :rtype: str
        """
        return self._jar

    @jar.setter
    def jar(self, jar):
        """Sets the jar of this AppForStartApplicationInstanceInput.


        :param jar: The jar of this AppForStartApplicationInstanceInput.  # noqa: E501
        :type: str
        """

        self._jar = jar

    @property
    def job_name(self):
        """Gets the job_name of this AppForStartApplicationInstanceInput.  # noqa: E501


        :return: The job_name of this AppForStartApplicationInstanceInput.  # noqa: E501
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        """Sets the job_name of this AppForStartApplicationInstanceInput.


        :param job_name: The job_name of this AppForStartApplicationInstanceInput.  # noqa: E501
        :type: str
        """

        self._job_name = job_name

    @property
    def job_type(self):
        """Gets the job_type of this AppForStartApplicationInstanceInput.  # noqa: E501


        :return: The job_type of this AppForStartApplicationInstanceInput.  # noqa: E501
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        """Sets the job_type of this AppForStartApplicationInstanceInput.


        :param job_type: The job_type of this AppForStartApplicationInstanceInput.  # noqa: E501
        :type: str
        """
        allowed_values = ["FLINK_STREAMING_JAR", "FLINK_STREAMING_SQL", "FLINK_BATCH_SQL", "FLINK_BATCH_JAR"]  # noqa: E501
        if (self._configuration.client_side_validation and
                job_type not in allowed_values):
            raise ValueError(
                "Invalid value for `job_type` ({0}), must be one of {1}"  # noqa: E501
                .format(job_type, allowed_values)
            )

        self._job_type = job_type

    @property
    def main_class(self):
        """Gets the main_class of this AppForStartApplicationInstanceInput.  # noqa: E501


        :return: The main_class of this AppForStartApplicationInstanceInput.  # noqa: E501
        :rtype: str
        """
        return self._main_class

    @main_class.setter
    def main_class(self, main_class):
        """Sets the main_class of this AppForStartApplicationInstanceInput.


        :param main_class: The main_class of this AppForStartApplicationInstanceInput.  # noqa: E501
        :type: str
        """

        self._main_class = main_class

    @property
    def project_id(self):
        """Gets the project_id of this AppForStartApplicationInstanceInput.  # noqa: E501


        :return: The project_id of this AppForStartApplicationInstanceInput.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this AppForStartApplicationInstanceInput.


        :param project_id: The project_id of this AppForStartApplicationInstanceInput.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def sql_text(self):
        """Gets the sql_text of this AppForStartApplicationInstanceInput.  # noqa: E501


        :return: The sql_text of this AppForStartApplicationInstanceInput.  # noqa: E501
        :rtype: str
        """
        return self._sql_text

    @sql_text.setter
    def sql_text(self, sql_text):
        """Sets the sql_text of this AppForStartApplicationInstanceInput.


        :param sql_text: The sql_text of this AppForStartApplicationInstanceInput.  # noqa: E501
        :type: str
        """

        self._sql_text = sql_text

    @property
    def unique_key(self):
        """Gets the unique_key of this AppForStartApplicationInstanceInput.  # noqa: E501


        :return: The unique_key of this AppForStartApplicationInstanceInput.  # noqa: E501
        :rtype: str
        """
        return self._unique_key

    @unique_key.setter
    def unique_key(self, unique_key):
        """Sets the unique_key of this AppForStartApplicationInstanceInput.


        :param unique_key: The unique_key of this AppForStartApplicationInstanceInput.  # noqa: E501
        :type: str
        """

        self._unique_key = unique_key

    @property
    def user_id(self):
        """Gets the user_id of this AppForStartApplicationInstanceInput.  # noqa: E501


        :return: The user_id of this AppForStartApplicationInstanceInput.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this AppForStartApplicationInstanceInput.


        :param user_id: The user_id of this AppForStartApplicationInstanceInput.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

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
        if issubclass(AppForStartApplicationInstanceInput, dict):
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
        if not isinstance(other, AppForStartApplicationInstanceInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AppForStartApplicationInstanceInput):
            return True

        return self.to_dict() != other.to_dict()
