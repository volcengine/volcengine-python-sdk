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


class ListResourceReservationRecordsRequest(object):
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
        'page_number': 'int',
        'page_size': 'int',
        'reservation_plan_id': 'str',
        'sort_by': 'str',
        'sort_order': 'str',
        'states': 'list[str]'
    }

    attribute_map = {
        'page_number': 'PageNumber',
        'page_size': 'PageSize',
        'reservation_plan_id': 'ReservationPlanId',
        'sort_by': 'SortBy',
        'sort_order': 'SortOrder',
        'states': 'States'
    }

    def __init__(self, page_number=None, page_size=None, reservation_plan_id=None, sort_by=None, sort_order=None, states=None, _configuration=None):  # noqa: E501
        """ListResourceReservationRecordsRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._page_number = None
        self._page_size = None
        self._reservation_plan_id = None
        self._sort_by = None
        self._sort_order = None
        self._states = None
        self.discriminator = None

        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size
        self.reservation_plan_id = reservation_plan_id
        if sort_by is not None:
            self.sort_by = sort_by
        if sort_order is not None:
            self.sort_order = sort_order
        if states is not None:
            self.states = states

    @property
    def page_number(self):
        """Gets the page_number of this ListResourceReservationRecordsRequest.  # noqa: E501


        :return: The page_number of this ListResourceReservationRecordsRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this ListResourceReservationRecordsRequest.


        :param page_number: The page_number of this ListResourceReservationRecordsRequest.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this ListResourceReservationRecordsRequest.  # noqa: E501


        :return: The page_size of this ListResourceReservationRecordsRequest.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ListResourceReservationRecordsRequest.


        :param page_size: The page_size of this ListResourceReservationRecordsRequest.  # noqa: E501
        :type: int
        """
        if (self._configuration.client_side_validation and
                page_size is not None and page_size > 100):  # noqa: E501
            raise ValueError("Invalid value for `page_size`, must be a value less than or equal to `100`")  # noqa: E501
        if (self._configuration.client_side_validation and
                page_size is not None and page_size < 10):  # noqa: E501
            raise ValueError("Invalid value for `page_size`, must be a value greater than or equal to `10`")  # noqa: E501

        self._page_size = page_size

    @property
    def reservation_plan_id(self):
        """Gets the reservation_plan_id of this ListResourceReservationRecordsRequest.  # noqa: E501


        :return: The reservation_plan_id of this ListResourceReservationRecordsRequest.  # noqa: E501
        :rtype: str
        """
        return self._reservation_plan_id

    @reservation_plan_id.setter
    def reservation_plan_id(self, reservation_plan_id):
        """Sets the reservation_plan_id of this ListResourceReservationRecordsRequest.


        :param reservation_plan_id: The reservation_plan_id of this ListResourceReservationRecordsRequest.  # noqa: E501
        :type: str
        """
        if self._configuration.client_side_validation and reservation_plan_id is None:
            raise ValueError("Invalid value for `reservation_plan_id`, must not be `None`")  # noqa: E501

        self._reservation_plan_id = reservation_plan_id

    @property
    def sort_by(self):
        """Gets the sort_by of this ListResourceReservationRecordsRequest.  # noqa: E501


        :return: The sort_by of this ListResourceReservationRecordsRequest.  # noqa: E501
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        """Sets the sort_by of this ListResourceReservationRecordsRequest.


        :param sort_by: The sort_by of this ListResourceReservationRecordsRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["CreateTime"]  # noqa: E501
        if (self._configuration.client_side_validation and
                sort_by not in allowed_values):
            raise ValueError(
                "Invalid value for `sort_by` ({0}), must be one of {1}"  # noqa: E501
                .format(sort_by, allowed_values)
            )

        self._sort_by = sort_by

    @property
    def sort_order(self):
        """Gets the sort_order of this ListResourceReservationRecordsRequest.  # noqa: E501


        :return: The sort_order of this ListResourceReservationRecordsRequest.  # noqa: E501
        :rtype: str
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this ListResourceReservationRecordsRequest.


        :param sort_order: The sort_order of this ListResourceReservationRecordsRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["Ascend", "Descend"]  # noqa: E501
        if (self._configuration.client_side_validation and
                sort_order not in allowed_values):
            raise ValueError(
                "Invalid value for `sort_order` ({0}), must be one of {1}"  # noqa: E501
                .format(sort_order, allowed_values)
            )

        self._sort_order = sort_order

    @property
    def states(self):
        """Gets the states of this ListResourceReservationRecordsRequest.  # noqa: E501


        :return: The states of this ListResourceReservationRecordsRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._states

    @states.setter
    def states(self, states):
        """Sets the states of this ListResourceReservationRecordsRequest.


        :param states: The states of this ListResourceReservationRecordsRequest.  # noqa: E501
        :type: list[str]
        """

        self._states = states

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
        if issubclass(ListResourceReservationRecordsRequest, dict):
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
        if not isinstance(other, ListResourceReservationRecordsRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListResourceReservationRecordsRequest):
            return True

        return self.to_dict() != other.to_dict()
