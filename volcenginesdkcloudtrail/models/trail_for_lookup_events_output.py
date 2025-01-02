# coding: utf-8

"""
    cloud_trail

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class TrailForLookupEventsOutput(object):
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
        'access_key_id': 'str',
        'error_code': 'str',
        'event_detail': 'str',
        'event_id': 'str',
        'event_name': 'str',
        'event_name_display': 'str',
        'event_source': 'str',
        'event_source_display': 'str',
        'event_time': 'str',
        'region': 'str',
        'related_resources': 'list[RelatedResourceForLookupEventsOutput]',
        'request_id': 'str',
        'source_ip_address': 'str',
        'user_name': 'str'
    }

    attribute_map = {
        'access_key_id': 'AccessKeyID',
        'error_code': 'ErrorCode',
        'event_detail': 'EventDetail',
        'event_id': 'EventID',
        'event_name': 'EventName',
        'event_name_display': 'EventNameDisplay',
        'event_source': 'EventSource',
        'event_source_display': 'EventSourceDisplay',
        'event_time': 'EventTime',
        'region': 'Region',
        'related_resources': 'RelatedResources',
        'request_id': 'RequestID',
        'source_ip_address': 'SourceIPAddress',
        'user_name': 'UserName'
    }

    def __init__(self, access_key_id=None, error_code=None, event_detail=None, event_id=None, event_name=None, event_name_display=None, event_source=None, event_source_display=None, event_time=None, region=None, related_resources=None, request_id=None, source_ip_address=None, user_name=None, _configuration=None):  # noqa: E501
        """TrailForLookupEventsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._access_key_id = None
        self._error_code = None
        self._event_detail = None
        self._event_id = None
        self._event_name = None
        self._event_name_display = None
        self._event_source = None
        self._event_source_display = None
        self._event_time = None
        self._region = None
        self._related_resources = None
        self._request_id = None
        self._source_ip_address = None
        self._user_name = None
        self.discriminator = None

        if access_key_id is not None:
            self.access_key_id = access_key_id
        if error_code is not None:
            self.error_code = error_code
        if event_detail is not None:
            self.event_detail = event_detail
        if event_id is not None:
            self.event_id = event_id
        if event_name is not None:
            self.event_name = event_name
        if event_name_display is not None:
            self.event_name_display = event_name_display
        if event_source is not None:
            self.event_source = event_source
        if event_source_display is not None:
            self.event_source_display = event_source_display
        if event_time is not None:
            self.event_time = event_time
        if region is not None:
            self.region = region
        if related_resources is not None:
            self.related_resources = related_resources
        if request_id is not None:
            self.request_id = request_id
        if source_ip_address is not None:
            self.source_ip_address = source_ip_address
        if user_name is not None:
            self.user_name = user_name

    @property
    def access_key_id(self):
        """Gets the access_key_id of this TrailForLookupEventsOutput.  # noqa: E501


        :return: The access_key_id of this TrailForLookupEventsOutput.  # noqa: E501
        :rtype: str
        """
        return self._access_key_id

    @access_key_id.setter
    def access_key_id(self, access_key_id):
        """Sets the access_key_id of this TrailForLookupEventsOutput.


        :param access_key_id: The access_key_id of this TrailForLookupEventsOutput.  # noqa: E501
        :type: str
        """

        self._access_key_id = access_key_id

    @property
    def error_code(self):
        """Gets the error_code of this TrailForLookupEventsOutput.  # noqa: E501


        :return: The error_code of this TrailForLookupEventsOutput.  # noqa: E501
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this TrailForLookupEventsOutput.


        :param error_code: The error_code of this TrailForLookupEventsOutput.  # noqa: E501
        :type: str
        """

        self._error_code = error_code

    @property
    def event_detail(self):
        """Gets the event_detail of this TrailForLookupEventsOutput.  # noqa: E501


        :return: The event_detail of this TrailForLookupEventsOutput.  # noqa: E501
        :rtype: str
        """
        return self._event_detail

    @event_detail.setter
    def event_detail(self, event_detail):
        """Sets the event_detail of this TrailForLookupEventsOutput.


        :param event_detail: The event_detail of this TrailForLookupEventsOutput.  # noqa: E501
        :type: str
        """

        self._event_detail = event_detail

    @property
    def event_id(self):
        """Gets the event_id of this TrailForLookupEventsOutput.  # noqa: E501


        :return: The event_id of this TrailForLookupEventsOutput.  # noqa: E501
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this TrailForLookupEventsOutput.


        :param event_id: The event_id of this TrailForLookupEventsOutput.  # noqa: E501
        :type: str
        """

        self._event_id = event_id

    @property
    def event_name(self):
        """Gets the event_name of this TrailForLookupEventsOutput.  # noqa: E501


        :return: The event_name of this TrailForLookupEventsOutput.  # noqa: E501
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """Sets the event_name of this TrailForLookupEventsOutput.


        :param event_name: The event_name of this TrailForLookupEventsOutput.  # noqa: E501
        :type: str
        """

        self._event_name = event_name

    @property
    def event_name_display(self):
        """Gets the event_name_display of this TrailForLookupEventsOutput.  # noqa: E501


        :return: The event_name_display of this TrailForLookupEventsOutput.  # noqa: E501
        :rtype: str
        """
        return self._event_name_display

    @event_name_display.setter
    def event_name_display(self, event_name_display):
        """Sets the event_name_display of this TrailForLookupEventsOutput.


        :param event_name_display: The event_name_display of this TrailForLookupEventsOutput.  # noqa: E501
        :type: str
        """

        self._event_name_display = event_name_display

    @property
    def event_source(self):
        """Gets the event_source of this TrailForLookupEventsOutput.  # noqa: E501


        :return: The event_source of this TrailForLookupEventsOutput.  # noqa: E501
        :rtype: str
        """
        return self._event_source

    @event_source.setter
    def event_source(self, event_source):
        """Sets the event_source of this TrailForLookupEventsOutput.


        :param event_source: The event_source of this TrailForLookupEventsOutput.  # noqa: E501
        :type: str
        """

        self._event_source = event_source

    @property
    def event_source_display(self):
        """Gets the event_source_display of this TrailForLookupEventsOutput.  # noqa: E501


        :return: The event_source_display of this TrailForLookupEventsOutput.  # noqa: E501
        :rtype: str
        """
        return self._event_source_display

    @event_source_display.setter
    def event_source_display(self, event_source_display):
        """Sets the event_source_display of this TrailForLookupEventsOutput.


        :param event_source_display: The event_source_display of this TrailForLookupEventsOutput.  # noqa: E501
        :type: str
        """

        self._event_source_display = event_source_display

    @property
    def event_time(self):
        """Gets the event_time of this TrailForLookupEventsOutput.  # noqa: E501


        :return: The event_time of this TrailForLookupEventsOutput.  # noqa: E501
        :rtype: str
        """
        return self._event_time

    @event_time.setter
    def event_time(self, event_time):
        """Sets the event_time of this TrailForLookupEventsOutput.


        :param event_time: The event_time of this TrailForLookupEventsOutput.  # noqa: E501
        :type: str
        """

        self._event_time = event_time

    @property
    def region(self):
        """Gets the region of this TrailForLookupEventsOutput.  # noqa: E501


        :return: The region of this TrailForLookupEventsOutput.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this TrailForLookupEventsOutput.


        :param region: The region of this TrailForLookupEventsOutput.  # noqa: E501
        :type: str
        """

        self._region = region

    @property
    def related_resources(self):
        """Gets the related_resources of this TrailForLookupEventsOutput.  # noqa: E501


        :return: The related_resources of this TrailForLookupEventsOutput.  # noqa: E501
        :rtype: list[RelatedResourceForLookupEventsOutput]
        """
        return self._related_resources

    @related_resources.setter
    def related_resources(self, related_resources):
        """Sets the related_resources of this TrailForLookupEventsOutput.


        :param related_resources: The related_resources of this TrailForLookupEventsOutput.  # noqa: E501
        :type: list[RelatedResourceForLookupEventsOutput]
        """

        self._related_resources = related_resources

    @property
    def request_id(self):
        """Gets the request_id of this TrailForLookupEventsOutput.  # noqa: E501


        :return: The request_id of this TrailForLookupEventsOutput.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this TrailForLookupEventsOutput.


        :param request_id: The request_id of this TrailForLookupEventsOutput.  # noqa: E501
        :type: str
        """

        self._request_id = request_id

    @property
    def source_ip_address(self):
        """Gets the source_ip_address of this TrailForLookupEventsOutput.  # noqa: E501


        :return: The source_ip_address of this TrailForLookupEventsOutput.  # noqa: E501
        :rtype: str
        """
        return self._source_ip_address

    @source_ip_address.setter
    def source_ip_address(self, source_ip_address):
        """Sets the source_ip_address of this TrailForLookupEventsOutput.


        :param source_ip_address: The source_ip_address of this TrailForLookupEventsOutput.  # noqa: E501
        :type: str
        """

        self._source_ip_address = source_ip_address

    @property
    def user_name(self):
        """Gets the user_name of this TrailForLookupEventsOutput.  # noqa: E501


        :return: The user_name of this TrailForLookupEventsOutput.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this TrailForLookupEventsOutput.


        :param user_name: The user_name of this TrailForLookupEventsOutput.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

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
        if issubclass(TrailForLookupEventsOutput, dict):
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
        if not isinstance(other, TrailForLookupEventsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TrailForLookupEventsOutput):
            return True

        return self.to_dict() != other.to_dict()