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


class PolicyForCreatePolicyOutput(object):
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
        'attachment_count': 'int',
        'category': 'str',
        'create_date': 'str',
        'description': 'str',
        'is_service_role_policy': 'int',
        'policy_document': 'str',
        'policy_name': 'str',
        'policy_trn': 'str',
        'policy_type': 'str',
        'update_date': 'str'
    }

    attribute_map = {
        'attachment_count': 'AttachmentCount',
        'category': 'Category',
        'create_date': 'CreateDate',
        'description': 'Description',
        'is_service_role_policy': 'IsServiceRolePolicy',
        'policy_document': 'PolicyDocument',
        'policy_name': 'PolicyName',
        'policy_trn': 'PolicyTrn',
        'policy_type': 'PolicyType',
        'update_date': 'UpdateDate'
    }

    def __init__(self, attachment_count=None, category=None, create_date=None, description=None, is_service_role_policy=None, policy_document=None, policy_name=None, policy_trn=None, policy_type=None, update_date=None, _configuration=None):  # noqa: E501
        """PolicyForCreatePolicyOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._attachment_count = None
        self._category = None
        self._create_date = None
        self._description = None
        self._is_service_role_policy = None
        self._policy_document = None
        self._policy_name = None
        self._policy_trn = None
        self._policy_type = None
        self._update_date = None
        self.discriminator = None

        if attachment_count is not None:
            self.attachment_count = attachment_count
        if category is not None:
            self.category = category
        if create_date is not None:
            self.create_date = create_date
        if description is not None:
            self.description = description
        if is_service_role_policy is not None:
            self.is_service_role_policy = is_service_role_policy
        if policy_document is not None:
            self.policy_document = policy_document
        if policy_name is not None:
            self.policy_name = policy_name
        if policy_trn is not None:
            self.policy_trn = policy_trn
        if policy_type is not None:
            self.policy_type = policy_type
        if update_date is not None:
            self.update_date = update_date

    @property
    def attachment_count(self):
        """Gets the attachment_count of this PolicyForCreatePolicyOutput.  # noqa: E501


        :return: The attachment_count of this PolicyForCreatePolicyOutput.  # noqa: E501
        :rtype: int
        """
        return self._attachment_count

    @attachment_count.setter
    def attachment_count(self, attachment_count):
        """Sets the attachment_count of this PolicyForCreatePolicyOutput.


        :param attachment_count: The attachment_count of this PolicyForCreatePolicyOutput.  # noqa: E501
        :type: int
        """

        self._attachment_count = attachment_count

    @property
    def category(self):
        """Gets the category of this PolicyForCreatePolicyOutput.  # noqa: E501


        :return: The category of this PolicyForCreatePolicyOutput.  # noqa: E501
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this PolicyForCreatePolicyOutput.


        :param category: The category of this PolicyForCreatePolicyOutput.  # noqa: E501
        :type: str
        """

        self._category = category

    @property
    def create_date(self):
        """Gets the create_date of this PolicyForCreatePolicyOutput.  # noqa: E501


        :return: The create_date of this PolicyForCreatePolicyOutput.  # noqa: E501
        :rtype: str
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this PolicyForCreatePolicyOutput.


        :param create_date: The create_date of this PolicyForCreatePolicyOutput.  # noqa: E501
        :type: str
        """

        self._create_date = create_date

    @property
    def description(self):
        """Gets the description of this PolicyForCreatePolicyOutput.  # noqa: E501


        :return: The description of this PolicyForCreatePolicyOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PolicyForCreatePolicyOutput.


        :param description: The description of this PolicyForCreatePolicyOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def is_service_role_policy(self):
        """Gets the is_service_role_policy of this PolicyForCreatePolicyOutput.  # noqa: E501


        :return: The is_service_role_policy of this PolicyForCreatePolicyOutput.  # noqa: E501
        :rtype: int
        """
        return self._is_service_role_policy

    @is_service_role_policy.setter
    def is_service_role_policy(self, is_service_role_policy):
        """Sets the is_service_role_policy of this PolicyForCreatePolicyOutput.


        :param is_service_role_policy: The is_service_role_policy of this PolicyForCreatePolicyOutput.  # noqa: E501
        :type: int
        """

        self._is_service_role_policy = is_service_role_policy

    @property
    def policy_document(self):
        """Gets the policy_document of this PolicyForCreatePolicyOutput.  # noqa: E501


        :return: The policy_document of this PolicyForCreatePolicyOutput.  # noqa: E501
        :rtype: str
        """
        return self._policy_document

    @policy_document.setter
    def policy_document(self, policy_document):
        """Sets the policy_document of this PolicyForCreatePolicyOutput.


        :param policy_document: The policy_document of this PolicyForCreatePolicyOutput.  # noqa: E501
        :type: str
        """

        self._policy_document = policy_document

    @property
    def policy_name(self):
        """Gets the policy_name of this PolicyForCreatePolicyOutput.  # noqa: E501


        :return: The policy_name of this PolicyForCreatePolicyOutput.  # noqa: E501
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        """Sets the policy_name of this PolicyForCreatePolicyOutput.


        :param policy_name: The policy_name of this PolicyForCreatePolicyOutput.  # noqa: E501
        :type: str
        """

        self._policy_name = policy_name

    @property
    def policy_trn(self):
        """Gets the policy_trn of this PolicyForCreatePolicyOutput.  # noqa: E501


        :return: The policy_trn of this PolicyForCreatePolicyOutput.  # noqa: E501
        :rtype: str
        """
        return self._policy_trn

    @policy_trn.setter
    def policy_trn(self, policy_trn):
        """Sets the policy_trn of this PolicyForCreatePolicyOutput.


        :param policy_trn: The policy_trn of this PolicyForCreatePolicyOutput.  # noqa: E501
        :type: str
        """

        self._policy_trn = policy_trn

    @property
    def policy_type(self):
        """Gets the policy_type of this PolicyForCreatePolicyOutput.  # noqa: E501


        :return: The policy_type of this PolicyForCreatePolicyOutput.  # noqa: E501
        :rtype: str
        """
        return self._policy_type

    @policy_type.setter
    def policy_type(self, policy_type):
        """Sets the policy_type of this PolicyForCreatePolicyOutput.


        :param policy_type: The policy_type of this PolicyForCreatePolicyOutput.  # noqa: E501
        :type: str
        """

        self._policy_type = policy_type

    @property
    def update_date(self):
        """Gets the update_date of this PolicyForCreatePolicyOutput.  # noqa: E501


        :return: The update_date of this PolicyForCreatePolicyOutput.  # noqa: E501
        :rtype: str
        """
        return self._update_date

    @update_date.setter
    def update_date(self, update_date):
        """Sets the update_date of this PolicyForCreatePolicyOutput.


        :param update_date: The update_date of this PolicyForCreatePolicyOutput.  # noqa: E501
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
        if issubclass(PolicyForCreatePolicyOutput, dict):
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
        if not isinstance(other, PolicyForCreatePolicyOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PolicyForCreatePolicyOutput):
            return True

        return self.to_dict() != other.to_dict()
