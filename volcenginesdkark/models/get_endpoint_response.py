# coding: utf-8

"""
    ark

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class GetEndpointResponse(object):
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
        'batch_only': 'bool',
        'create_time': 'str',
        'description': 'str',
        'endpoint_model_type': 'str',
        'id': 'str',
        'model_reference': 'ModelReferenceForGetEndpointOutput',
        'model_unit_id': 'str',
        'moderation': 'ModerationForGetEndpointOutput',
        'name': 'str',
        'project_name': 'str',
        'rate_limit': 'RateLimitForGetEndpointOutput',
        'rolling_id': 'str',
        'scale_tier_id': 'str',
        'status': 'str',
        'status_reason': 'str',
        'support_rolling': 'bool',
        'support_scale_tier': 'bool',
        'tags': 'list[TagForGetEndpointOutput]',
        'update_time': 'str'
    }

    attribute_map = {
        'batch_only': 'BatchOnly',
        'create_time': 'CreateTime',
        'description': 'Description',
        'endpoint_model_type': 'EndpointModelType',
        'id': 'Id',
        'model_reference': 'ModelReference',
        'model_unit_id': 'ModelUnitId',
        'moderation': 'Moderation',
        'name': 'Name',
        'project_name': 'ProjectName',
        'rate_limit': 'RateLimit',
        'rolling_id': 'RollingId',
        'scale_tier_id': 'ScaleTierId',
        'status': 'Status',
        'status_reason': 'StatusReason',
        'support_rolling': 'SupportRolling',
        'support_scale_tier': 'SupportScaleTier',
        'tags': 'Tags',
        'update_time': 'UpdateTime'
    }

    def __init__(self, batch_only=None, create_time=None, description=None, endpoint_model_type=None, id=None, model_reference=None, model_unit_id=None, moderation=None, name=None, project_name=None, rate_limit=None, rolling_id=None, scale_tier_id=None, status=None, status_reason=None, support_rolling=None, support_scale_tier=None, tags=None, update_time=None, _configuration=None):  # noqa: E501
        """GetEndpointResponse - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._batch_only = None
        self._create_time = None
        self._description = None
        self._endpoint_model_type = None
        self._id = None
        self._model_reference = None
        self._model_unit_id = None
        self._moderation = None
        self._name = None
        self._project_name = None
        self._rate_limit = None
        self._rolling_id = None
        self._scale_tier_id = None
        self._status = None
        self._status_reason = None
        self._support_rolling = None
        self._support_scale_tier = None
        self._tags = None
        self._update_time = None
        self.discriminator = None

        if batch_only is not None:
            self.batch_only = batch_only
        if create_time is not None:
            self.create_time = create_time
        if description is not None:
            self.description = description
        if endpoint_model_type is not None:
            self.endpoint_model_type = endpoint_model_type
        if id is not None:
            self.id = id
        if model_reference is not None:
            self.model_reference = model_reference
        if model_unit_id is not None:
            self.model_unit_id = model_unit_id
        if moderation is not None:
            self.moderation = moderation
        if name is not None:
            self.name = name
        if project_name is not None:
            self.project_name = project_name
        if rate_limit is not None:
            self.rate_limit = rate_limit
        if rolling_id is not None:
            self.rolling_id = rolling_id
        if scale_tier_id is not None:
            self.scale_tier_id = scale_tier_id
        if status is not None:
            self.status = status
        if status_reason is not None:
            self.status_reason = status_reason
        if support_rolling is not None:
            self.support_rolling = support_rolling
        if support_scale_tier is not None:
            self.support_scale_tier = support_scale_tier
        if tags is not None:
            self.tags = tags
        if update_time is not None:
            self.update_time = update_time

    @property
    def batch_only(self):
        """Gets the batch_only of this GetEndpointResponse.  # noqa: E501


        :return: The batch_only of this GetEndpointResponse.  # noqa: E501
        :rtype: bool
        """
        return self._batch_only

    @batch_only.setter
    def batch_only(self, batch_only):
        """Sets the batch_only of this GetEndpointResponse.


        :param batch_only: The batch_only of this GetEndpointResponse.  # noqa: E501
        :type: bool
        """

        self._batch_only = batch_only

    @property
    def create_time(self):
        """Gets the create_time of this GetEndpointResponse.  # noqa: E501


        :return: The create_time of this GetEndpointResponse.  # noqa: E501
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this GetEndpointResponse.


        :param create_time: The create_time of this GetEndpointResponse.  # noqa: E501
        :type: str
        """

        self._create_time = create_time

    @property
    def description(self):
        """Gets the description of this GetEndpointResponse.  # noqa: E501


        :return: The description of this GetEndpointResponse.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this GetEndpointResponse.


        :param description: The description of this GetEndpointResponse.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def endpoint_model_type(self):
        """Gets the endpoint_model_type of this GetEndpointResponse.  # noqa: E501


        :return: The endpoint_model_type of this GetEndpointResponse.  # noqa: E501
        :rtype: str
        """
        return self._endpoint_model_type

    @endpoint_model_type.setter
    def endpoint_model_type(self, endpoint_model_type):
        """Sets the endpoint_model_type of this GetEndpointResponse.


        :param endpoint_model_type: The endpoint_model_type of this GetEndpointResponse.  # noqa: E501
        :type: str
        """

        self._endpoint_model_type = endpoint_model_type

    @property
    def id(self):
        """Gets the id of this GetEndpointResponse.  # noqa: E501


        :return: The id of this GetEndpointResponse.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetEndpointResponse.


        :param id: The id of this GetEndpointResponse.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def model_reference(self):
        """Gets the model_reference of this GetEndpointResponse.  # noqa: E501


        :return: The model_reference of this GetEndpointResponse.  # noqa: E501
        :rtype: ModelReferenceForGetEndpointOutput
        """
        return self._model_reference

    @model_reference.setter
    def model_reference(self, model_reference):
        """Sets the model_reference of this GetEndpointResponse.


        :param model_reference: The model_reference of this GetEndpointResponse.  # noqa: E501
        :type: ModelReferenceForGetEndpointOutput
        """

        self._model_reference = model_reference

    @property
    def model_unit_id(self):
        """Gets the model_unit_id of this GetEndpointResponse.  # noqa: E501


        :return: The model_unit_id of this GetEndpointResponse.  # noqa: E501
        :rtype: str
        """
        return self._model_unit_id

    @model_unit_id.setter
    def model_unit_id(self, model_unit_id):
        """Sets the model_unit_id of this GetEndpointResponse.


        :param model_unit_id: The model_unit_id of this GetEndpointResponse.  # noqa: E501
        :type: str
        """

        self._model_unit_id = model_unit_id

    @property
    def moderation(self):
        """Gets the moderation of this GetEndpointResponse.  # noqa: E501


        :return: The moderation of this GetEndpointResponse.  # noqa: E501
        :rtype: ModerationForGetEndpointOutput
        """
        return self._moderation

    @moderation.setter
    def moderation(self, moderation):
        """Sets the moderation of this GetEndpointResponse.


        :param moderation: The moderation of this GetEndpointResponse.  # noqa: E501
        :type: ModerationForGetEndpointOutput
        """

        self._moderation = moderation

    @property
    def name(self):
        """Gets the name of this GetEndpointResponse.  # noqa: E501


        :return: The name of this GetEndpointResponse.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this GetEndpointResponse.


        :param name: The name of this GetEndpointResponse.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def project_name(self):
        """Gets the project_name of this GetEndpointResponse.  # noqa: E501


        :return: The project_name of this GetEndpointResponse.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this GetEndpointResponse.


        :param project_name: The project_name of this GetEndpointResponse.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def rate_limit(self):
        """Gets the rate_limit of this GetEndpointResponse.  # noqa: E501


        :return: The rate_limit of this GetEndpointResponse.  # noqa: E501
        :rtype: RateLimitForGetEndpointOutput
        """
        return self._rate_limit

    @rate_limit.setter
    def rate_limit(self, rate_limit):
        """Sets the rate_limit of this GetEndpointResponse.


        :param rate_limit: The rate_limit of this GetEndpointResponse.  # noqa: E501
        :type: RateLimitForGetEndpointOutput
        """

        self._rate_limit = rate_limit

    @property
    def rolling_id(self):
        """Gets the rolling_id of this GetEndpointResponse.  # noqa: E501


        :return: The rolling_id of this GetEndpointResponse.  # noqa: E501
        :rtype: str
        """
        return self._rolling_id

    @rolling_id.setter
    def rolling_id(self, rolling_id):
        """Sets the rolling_id of this GetEndpointResponse.


        :param rolling_id: The rolling_id of this GetEndpointResponse.  # noqa: E501
        :type: str
        """

        self._rolling_id = rolling_id

    @property
    def scale_tier_id(self):
        """Gets the scale_tier_id of this GetEndpointResponse.  # noqa: E501


        :return: The scale_tier_id of this GetEndpointResponse.  # noqa: E501
        :rtype: str
        """
        return self._scale_tier_id

    @scale_tier_id.setter
    def scale_tier_id(self, scale_tier_id):
        """Sets the scale_tier_id of this GetEndpointResponse.


        :param scale_tier_id: The scale_tier_id of this GetEndpointResponse.  # noqa: E501
        :type: str
        """

        self._scale_tier_id = scale_tier_id

    @property
    def status(self):
        """Gets the status of this GetEndpointResponse.  # noqa: E501


        :return: The status of this GetEndpointResponse.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GetEndpointResponse.


        :param status: The status of this GetEndpointResponse.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def status_reason(self):
        """Gets the status_reason of this GetEndpointResponse.  # noqa: E501


        :return: The status_reason of this GetEndpointResponse.  # noqa: E501
        :rtype: str
        """
        return self._status_reason

    @status_reason.setter
    def status_reason(self, status_reason):
        """Sets the status_reason of this GetEndpointResponse.


        :param status_reason: The status_reason of this GetEndpointResponse.  # noqa: E501
        :type: str
        """

        self._status_reason = status_reason

    @property
    def support_rolling(self):
        """Gets the support_rolling of this GetEndpointResponse.  # noqa: E501


        :return: The support_rolling of this GetEndpointResponse.  # noqa: E501
        :rtype: bool
        """
        return self._support_rolling

    @support_rolling.setter
    def support_rolling(self, support_rolling):
        """Sets the support_rolling of this GetEndpointResponse.


        :param support_rolling: The support_rolling of this GetEndpointResponse.  # noqa: E501
        :type: bool
        """

        self._support_rolling = support_rolling

    @property
    def support_scale_tier(self):
        """Gets the support_scale_tier of this GetEndpointResponse.  # noqa: E501


        :return: The support_scale_tier of this GetEndpointResponse.  # noqa: E501
        :rtype: bool
        """
        return self._support_scale_tier

    @support_scale_tier.setter
    def support_scale_tier(self, support_scale_tier):
        """Sets the support_scale_tier of this GetEndpointResponse.


        :param support_scale_tier: The support_scale_tier of this GetEndpointResponse.  # noqa: E501
        :type: bool
        """

        self._support_scale_tier = support_scale_tier

    @property
    def tags(self):
        """Gets the tags of this GetEndpointResponse.  # noqa: E501


        :return: The tags of this GetEndpointResponse.  # noqa: E501
        :rtype: list[TagForGetEndpointOutput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this GetEndpointResponse.


        :param tags: The tags of this GetEndpointResponse.  # noqa: E501
        :type: list[TagForGetEndpointOutput]
        """

        self._tags = tags

    @property
    def update_time(self):
        """Gets the update_time of this GetEndpointResponse.  # noqa: E501


        :return: The update_time of this GetEndpointResponse.  # noqa: E501
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this GetEndpointResponse.


        :param update_time: The update_time of this GetEndpointResponse.  # noqa: E501
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
        if issubclass(GetEndpointResponse, dict):
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
        if not isinstance(other, GetEndpointResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GetEndpointResponse):
            return True

        return self.to_dict() != other.to_dict()
