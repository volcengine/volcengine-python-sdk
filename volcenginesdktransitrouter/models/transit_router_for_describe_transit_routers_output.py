# coding: utf-8

"""
    transitrouter

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class TransitRouterForDescribeTransitRoutersOutput(object):
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
        'asn': 'int',
        'business_status': 'str',
        'creation_time': 'str',
        'deleted_time': 'str',
        'description': 'str',
        'grant_status': 'str',
        'overdue_time': 'str',
        'project_name': 'str',
        'status': 'str',
        'tags': 'list[TagForDescribeTransitRoutersOutput]',
        'transit_router_id': 'str',
        'transit_router_name': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'account_id': 'AccountId',
        'asn': 'Asn',
        'business_status': 'BusinessStatus',
        'creation_time': 'CreationTime',
        'deleted_time': 'DeletedTime',
        'description': 'Description',
        'grant_status': 'GrantStatus',
        'overdue_time': 'OverdueTime',
        'project_name': 'ProjectName',
        'status': 'Status',
        'tags': 'Tags',
        'transit_router_id': 'TransitRouterId',
        'transit_router_name': 'TransitRouterName',
        'update_time': 'UpdateTime'
    }

    def __init__(self, account_id=None, asn=None, business_status=None, creation_time=None, deleted_time=None, description=None, grant_status=None, overdue_time=None, project_name=None, status=None, tags=None, transit_router_id=None, transit_router_name=None, update_time=None, _configuration=None):  # noqa: E501
        """TransitRouterForDescribeTransitRoutersOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_id = None
        self._asn = None
        self._business_status = None
        self._creation_time = None
        self._deleted_time = None
        self._description = None
        self._grant_status = None
        self._overdue_time = None
        self._project_name = None
        self._status = None
        self._tags = None
        self._transit_router_id = None
        self._transit_router_name = None
        self._update_time = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if asn is not None:
            self.asn = asn
        if business_status is not None:
            self.business_status = business_status
        if creation_time is not None:
            self.creation_time = creation_time
        if deleted_time is not None:
            self.deleted_time = deleted_time
        if description is not None:
            self.description = description
        if grant_status is not None:
            self.grant_status = grant_status
        if overdue_time is not None:
            self.overdue_time = overdue_time
        if project_name is not None:
            self.project_name = project_name
        if status is not None:
            self.status = status
        if tags is not None:
            self.tags = tags
        if transit_router_id is not None:
            self.transit_router_id = transit_router_id
        if transit_router_name is not None:
            self.transit_router_name = transit_router_name
        if update_time is not None:
            self.update_time = update_time

    @property
    def account_id(self):
        """Gets the account_id of this TransitRouterForDescribeTransitRoutersOutput.  # noqa: E501


        :return: The account_id of this TransitRouterForDescribeTransitRoutersOutput.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this TransitRouterForDescribeTransitRoutersOutput.


        :param account_id: The account_id of this TransitRouterForDescribeTransitRoutersOutput.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def asn(self):
        """Gets the asn of this TransitRouterForDescribeTransitRoutersOutput.  # noqa: E501


        :return: The asn of this TransitRouterForDescribeTransitRoutersOutput.  # noqa: E501
        :rtype: int
        """
        return self._asn

    @asn.setter
    def asn(self, asn):
        """Sets the asn of this TransitRouterForDescribeTransitRoutersOutput.


        :param asn: The asn of this TransitRouterForDescribeTransitRoutersOutput.  # noqa: E501
        :type: int
        """

        self._asn = asn

    @property
    def business_status(self):
        """Gets the business_status of this TransitRouterForDescribeTransitRoutersOutput.  # noqa: E501


        :return: The business_status of this TransitRouterForDescribeTransitRoutersOutput.  # noqa: E501
        :rtype: str
        """
        return self._business_status

    @business_status.setter
    def business_status(self, business_status):
        """Sets the business_status of this TransitRouterForDescribeTransitRoutersOutput.


        :param business_status: The business_status of this TransitRouterForDescribeTransitRoutersOutput.  # noqa: E501
        :type: str
        """

        self._business_status = business_status

    @property
    def creation_time(self):
        """Gets the creation_time of this TransitRouterForDescribeTransitRoutersOutput.  # noqa: E501


        :return: The creation_time of this TransitRouterForDescribeTransitRoutersOutput.  # noqa: E501
        :rtype: str
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """Sets the creation_time of this TransitRouterForDescribeTransitRoutersOutput.


        :param creation_time: The creation_time of this TransitRouterForDescribeTransitRoutersOutput.  # noqa: E501
        :type: str
        """

        self._creation_time = creation_time

    @property
    def deleted_time(self):
        """Gets the deleted_time of this TransitRouterForDescribeTransitRoutersOutput.  # noqa: E501


        :return: The deleted_time of this TransitRouterForDescribeTransitRoutersOutput.  # noqa: E501
        :rtype: str
        """
        return self._deleted_time

    @deleted_time.setter
    def deleted_time(self, deleted_time):
        """Sets the deleted_time of this TransitRouterForDescribeTransitRoutersOutput.


        :param deleted_time: The deleted_time of this TransitRouterForDescribeTransitRoutersOutput.  # noqa: E501
        :type: str
        """

        self._deleted_time = deleted_time

    @property
    def description(self):
        """Gets the description of this TransitRouterForDescribeTransitRoutersOutput.  # noqa: E501


        :return: The description of this TransitRouterForDescribeTransitRoutersOutput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TransitRouterForDescribeTransitRoutersOutput.


        :param description: The description of this TransitRouterForDescribeTransitRoutersOutput.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def grant_status(self):
        """Gets the grant_status of this TransitRouterForDescribeTransitRoutersOutput.  # noqa: E501


        :return: The grant_status of this TransitRouterForDescribeTransitRoutersOutput.  # noqa: E501
        :rtype: str
        """
        return self._grant_status

    @grant_status.setter
    def grant_status(self, grant_status):
        """Sets the grant_status of this TransitRouterForDescribeTransitRoutersOutput.


        :param grant_status: The grant_status of this TransitRouterForDescribeTransitRoutersOutput.  # noqa: E501
        :type: str
        """

        self._grant_status = grant_status

    @property
    def overdue_time(self):
        """Gets the overdue_time of this TransitRouterForDescribeTransitRoutersOutput.  # noqa: E501


        :return: The overdue_time of this TransitRouterForDescribeTransitRoutersOutput.  # noqa: E501
        :rtype: str
        """
        return self._overdue_time

    @overdue_time.setter
    def overdue_time(self, overdue_time):
        """Sets the overdue_time of this TransitRouterForDescribeTransitRoutersOutput.


        :param overdue_time: The overdue_time of this TransitRouterForDescribeTransitRoutersOutput.  # noqa: E501
        :type: str
        """

        self._overdue_time = overdue_time

    @property
    def project_name(self):
        """Gets the project_name of this TransitRouterForDescribeTransitRoutersOutput.  # noqa: E501


        :return: The project_name of this TransitRouterForDescribeTransitRoutersOutput.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this TransitRouterForDescribeTransitRoutersOutput.


        :param project_name: The project_name of this TransitRouterForDescribeTransitRoutersOutput.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def status(self):
        """Gets the status of this TransitRouterForDescribeTransitRoutersOutput.  # noqa: E501


        :return: The status of this TransitRouterForDescribeTransitRoutersOutput.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TransitRouterForDescribeTransitRoutersOutput.


        :param status: The status of this TransitRouterForDescribeTransitRoutersOutput.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def tags(self):
        """Gets the tags of this TransitRouterForDescribeTransitRoutersOutput.  # noqa: E501


        :return: The tags of this TransitRouterForDescribeTransitRoutersOutput.  # noqa: E501
        :rtype: list[TagForDescribeTransitRoutersOutput]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this TransitRouterForDescribeTransitRoutersOutput.


        :param tags: The tags of this TransitRouterForDescribeTransitRoutersOutput.  # noqa: E501
        :type: list[TagForDescribeTransitRoutersOutput]
        """

        self._tags = tags

    @property
    def transit_router_id(self):
        """Gets the transit_router_id of this TransitRouterForDescribeTransitRoutersOutput.  # noqa: E501


        :return: The transit_router_id of this TransitRouterForDescribeTransitRoutersOutput.  # noqa: E501
        :rtype: str
        """
        return self._transit_router_id

    @transit_router_id.setter
    def transit_router_id(self, transit_router_id):
        """Sets the transit_router_id of this TransitRouterForDescribeTransitRoutersOutput.


        :param transit_router_id: The transit_router_id of this TransitRouterForDescribeTransitRoutersOutput.  # noqa: E501
        :type: str
        """

        self._transit_router_id = transit_router_id

    @property
    def transit_router_name(self):
        """Gets the transit_router_name of this TransitRouterForDescribeTransitRoutersOutput.  # noqa: E501


        :return: The transit_router_name of this TransitRouterForDescribeTransitRoutersOutput.  # noqa: E501
        :rtype: str
        """
        return self._transit_router_name

    @transit_router_name.setter
    def transit_router_name(self, transit_router_name):
        """Sets the transit_router_name of this TransitRouterForDescribeTransitRoutersOutput.


        :param transit_router_name: The transit_router_name of this TransitRouterForDescribeTransitRoutersOutput.  # noqa: E501
        :type: str
        """

        self._transit_router_name = transit_router_name

    @property
    def update_time(self):
        """Gets the update_time of this TransitRouterForDescribeTransitRoutersOutput.  # noqa: E501


        :return: The update_time of this TransitRouterForDescribeTransitRoutersOutput.  # noqa: E501
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this TransitRouterForDescribeTransitRoutersOutput.


        :param update_time: The update_time of this TransitRouterForDescribeTransitRoutersOutput.  # noqa: E501
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
        if issubclass(TransitRouterForDescribeTransitRoutersOutput, dict):
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
        if not isinstance(other, TransitRouterForDescribeTransitRoutersOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransitRouterForDescribeTransitRoutersOutput):
            return True

        return self.to_dict() != other.to_dict()
