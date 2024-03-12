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


class TemplateInfoForListParameterTemplatesOutput(object):
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
        'create_time': 'str',
        'need_restart': 'bool',
        'parameter_num': 'int',
        'project_name': 'str',
        'template_category': 'str',
        'template_desc': 'str',
        'template_id': 'str',
        'template_name': 'str',
        'template_params': 'list[TemplateParamForListParameterTemplatesOutput]',
        'template_source': 'str',
        'template_type': 'str',
        'template_type_version': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'account_id': 'AccountId',
        'create_time': 'CreateTime',
        'need_restart': 'NeedRestart',
        'parameter_num': 'ParameterNum',
        'project_name': 'ProjectName',
        'template_category': 'TemplateCategory',
        'template_desc': 'TemplateDesc',
        'template_id': 'TemplateId',
        'template_name': 'TemplateName',
        'template_params': 'TemplateParams',
        'template_source': 'TemplateSource',
        'template_type': 'TemplateType',
        'template_type_version': 'TemplateTypeVersion',
        'update_time': 'UpdateTime'
    }

    def __init__(self, account_id=None, create_time=None, need_restart=None, parameter_num=None, project_name=None, template_category=None, template_desc=None, template_id=None, template_name=None, template_params=None, template_source=None, template_type=None, template_type_version=None, update_time=None, _configuration=None):  # noqa: E501
        """TemplateInfoForListParameterTemplatesOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_id = None
        self._create_time = None
        self._need_restart = None
        self._parameter_num = None
        self._project_name = None
        self._template_category = None
        self._template_desc = None
        self._template_id = None
        self._template_name = None
        self._template_params = None
        self._template_source = None
        self._template_type = None
        self._template_type_version = None
        self._update_time = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if create_time is not None:
            self.create_time = create_time
        if need_restart is not None:
            self.need_restart = need_restart
        if parameter_num is not None:
            self.parameter_num = parameter_num
        if project_name is not None:
            self.project_name = project_name
        if template_category is not None:
            self.template_category = template_category
        if template_desc is not None:
            self.template_desc = template_desc
        if template_id is not None:
            self.template_id = template_id
        if template_name is not None:
            self.template_name = template_name
        if template_params is not None:
            self.template_params = template_params
        if template_source is not None:
            self.template_source = template_source
        if template_type is not None:
            self.template_type = template_type
        if template_type_version is not None:
            self.template_type_version = template_type_version
        if update_time is not None:
            self.update_time = update_time

    @property
    def account_id(self):
        """Gets the account_id of this TemplateInfoForListParameterTemplatesOutput.  # noqa: E501


        :return: The account_id of this TemplateInfoForListParameterTemplatesOutput.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this TemplateInfoForListParameterTemplatesOutput.


        :param account_id: The account_id of this TemplateInfoForListParameterTemplatesOutput.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def create_time(self):
        """Gets the create_time of this TemplateInfoForListParameterTemplatesOutput.  # noqa: E501


        :return: The create_time of this TemplateInfoForListParameterTemplatesOutput.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this TemplateInfoForListParameterTemplatesOutput.


        :param create_time: The create_time of this TemplateInfoForListParameterTemplatesOutput.  # noqa: E501
        :type: str
        """

        self._create_time = create_time

    @property
    def need_restart(self):
        """Gets the need_restart of this TemplateInfoForListParameterTemplatesOutput.  # noqa: E501


        :return: The need_restart of this TemplateInfoForListParameterTemplatesOutput.  # noqa: E501
        :rtype: bool
        """
        return self._need_restart

    @need_restart.setter
    def need_restart(self, need_restart):
        """Sets the need_restart of this TemplateInfoForListParameterTemplatesOutput.


        :param need_restart: The need_restart of this TemplateInfoForListParameterTemplatesOutput.  # noqa: E501
        :type: bool
        """

        self._need_restart = need_restart

    @property
    def parameter_num(self):
        """Gets the parameter_num of this TemplateInfoForListParameterTemplatesOutput.  # noqa: E501


        :return: The parameter_num of this TemplateInfoForListParameterTemplatesOutput.  # noqa: E501
        :rtype: int
        """
        return self._parameter_num

    @parameter_num.setter
    def parameter_num(self, parameter_num):
        """Sets the parameter_num of this TemplateInfoForListParameterTemplatesOutput.


        :param parameter_num: The parameter_num of this TemplateInfoForListParameterTemplatesOutput.  # noqa: E501
        :type: int
        """

        self._parameter_num = parameter_num

    @property
    def project_name(self):
        """Gets the project_name of this TemplateInfoForListParameterTemplatesOutput.  # noqa: E501


        :return: The project_name of this TemplateInfoForListParameterTemplatesOutput.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this TemplateInfoForListParameterTemplatesOutput.


        :param project_name: The project_name of this TemplateInfoForListParameterTemplatesOutput.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def template_category(self):
        """Gets the template_category of this TemplateInfoForListParameterTemplatesOutput.  # noqa: E501


        :return: The template_category of this TemplateInfoForListParameterTemplatesOutput.  # noqa: E501
        :rtype: str
        """
        return self._template_category

    @template_category.setter
    def template_category(self, template_category):
        """Sets the template_category of this TemplateInfoForListParameterTemplatesOutput.


        :param template_category: The template_category of this TemplateInfoForListParameterTemplatesOutput.  # noqa: E501
        :type: str
        """

        self._template_category = template_category

    @property
    def template_desc(self):
        """Gets the template_desc of this TemplateInfoForListParameterTemplatesOutput.  # noqa: E501


        :return: The template_desc of this TemplateInfoForListParameterTemplatesOutput.  # noqa: E501
        :rtype: str
        """
        return self._template_desc

    @template_desc.setter
    def template_desc(self, template_desc):
        """Sets the template_desc of this TemplateInfoForListParameterTemplatesOutput.


        :param template_desc: The template_desc of this TemplateInfoForListParameterTemplatesOutput.  # noqa: E501
        :type: str
        """

        self._template_desc = template_desc

    @property
    def template_id(self):
        """Gets the template_id of this TemplateInfoForListParameterTemplatesOutput.  # noqa: E501


        :return: The template_id of this TemplateInfoForListParameterTemplatesOutput.  # noqa: E501
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        """Sets the template_id of this TemplateInfoForListParameterTemplatesOutput.


        :param template_id: The template_id of this TemplateInfoForListParameterTemplatesOutput.  # noqa: E501
        :type: str
        """

        self._template_id = template_id

    @property
    def template_name(self):
        """Gets the template_name of this TemplateInfoForListParameterTemplatesOutput.  # noqa: E501


        :return: The template_name of this TemplateInfoForListParameterTemplatesOutput.  # noqa: E501
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        """Sets the template_name of this TemplateInfoForListParameterTemplatesOutput.


        :param template_name: The template_name of this TemplateInfoForListParameterTemplatesOutput.  # noqa: E501
        :type: str
        """

        self._template_name = template_name

    @property
    def template_params(self):
        """Gets the template_params of this TemplateInfoForListParameterTemplatesOutput.  # noqa: E501


        :return: The template_params of this TemplateInfoForListParameterTemplatesOutput.  # noqa: E501
        :rtype: list[TemplateParamForListParameterTemplatesOutput]
        """
        return self._template_params

    @template_params.setter
    def template_params(self, template_params):
        """Sets the template_params of this TemplateInfoForListParameterTemplatesOutput.


        :param template_params: The template_params of this TemplateInfoForListParameterTemplatesOutput.  # noqa: E501
        :type: list[TemplateParamForListParameterTemplatesOutput]
        """

        self._template_params = template_params

    @property
    def template_source(self):
        """Gets the template_source of this TemplateInfoForListParameterTemplatesOutput.  # noqa: E501


        :return: The template_source of this TemplateInfoForListParameterTemplatesOutput.  # noqa: E501
        :rtype: str
        """
        return self._template_source

    @template_source.setter
    def template_source(self, template_source):
        """Sets the template_source of this TemplateInfoForListParameterTemplatesOutput.


        :param template_source: The template_source of this TemplateInfoForListParameterTemplatesOutput.  # noqa: E501
        :type: str
        """

        self._template_source = template_source

    @property
    def template_type(self):
        """Gets the template_type of this TemplateInfoForListParameterTemplatesOutput.  # noqa: E501


        :return: The template_type of this TemplateInfoForListParameterTemplatesOutput.  # noqa: E501
        :rtype: str
        """
        return self._template_type

    @template_type.setter
    def template_type(self, template_type):
        """Sets the template_type of this TemplateInfoForListParameterTemplatesOutput.


        :param template_type: The template_type of this TemplateInfoForListParameterTemplatesOutput.  # noqa: E501
        :type: str
        """

        self._template_type = template_type

    @property
    def template_type_version(self):
        """Gets the template_type_version of this TemplateInfoForListParameterTemplatesOutput.  # noqa: E501


        :return: The template_type_version of this TemplateInfoForListParameterTemplatesOutput.  # noqa: E501
        :rtype: str
        """
        return self._template_type_version

    @template_type_version.setter
    def template_type_version(self, template_type_version):
        """Sets the template_type_version of this TemplateInfoForListParameterTemplatesOutput.


        :param template_type_version: The template_type_version of this TemplateInfoForListParameterTemplatesOutput.  # noqa: E501
        :type: str
        """

        self._template_type_version = template_type_version

    @property
    def update_time(self):
        """Gets the update_time of this TemplateInfoForListParameterTemplatesOutput.  # noqa: E501


        :return: The update_time of this TemplateInfoForListParameterTemplatesOutput.  # noqa: E501
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this TemplateInfoForListParameterTemplatesOutput.


        :param update_time: The update_time of this TemplateInfoForListParameterTemplatesOutput.  # noqa: E501
        :type: str
        """

        self._update_time = update_time

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
        if issubclass(TemplateInfoForListParameterTemplatesOutput, dict):
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
        if not isinstance(other, TemplateInfoForListParameterTemplatesOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TemplateInfoForListParameterTemplatesOutput):
            return True

        return self.to_dict() != other.to_dict()
