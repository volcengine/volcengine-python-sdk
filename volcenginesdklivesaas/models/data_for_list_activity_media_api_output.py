# coding: utf-8

"""
    livesaas

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class DataForListActivityMediaAPIOutput(object):
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
        'activity_video': 'list[ActivityVideoForListActivityMediaAPIOutput]',
        'cover_image': 'str',
        'create_time': 'int',
        'creator': 'str',
        'failure_time': 'int',
        'folder_id': 'int',
        'folder_name': 'str',
        'id': 'str',
        'interaction_script_id': 'int',
        'media_library_video_type': 'int',
        'media_name': 'str',
        'media_size': 'int',
        'media_video_duration': 'int',
        'review_status': 'int',
        'source_type': 'int',
        'update_time': 'int',
        'vid': 'str',
        'video_height': 'int',
        'video_width': 'int'
    }

    attribute_map = {
        'activity_video': 'ActivityVideo',
        'cover_image': 'CoverImage',
        'create_time': 'CreateTime',
        'creator': 'Creator',
        'failure_time': 'FailureTime',
        'folder_id': 'FolderId',
        'folder_name': 'FolderName',
        'id': 'Id',
        'interaction_script_id': 'InteractionScriptId',
        'media_library_video_type': 'MediaLibraryVideoType',
        'media_name': 'MediaName',
        'media_size': 'MediaSize',
        'media_video_duration': 'MediaVideoDuration',
        'review_status': 'ReviewStatus',
        'source_type': 'SourceType',
        'update_time': 'UpdateTime',
        'vid': 'Vid',
        'video_height': 'VideoHeight',
        'video_width': 'VideoWidth'
    }

    def __init__(self, activity_video=None, cover_image=None, create_time=None, creator=None, failure_time=None, folder_id=None, folder_name=None, id=None, interaction_script_id=None, media_library_video_type=None, media_name=None, media_size=None, media_video_duration=None, review_status=None, source_type=None, update_time=None, vid=None, video_height=None, video_width=None, _configuration=None):  # noqa: E501
        """DataForListActivityMediaAPIOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._activity_video = None
        self._cover_image = None
        self._create_time = None
        self._creator = None
        self._failure_time = None
        self._folder_id = None
        self._folder_name = None
        self._id = None
        self._interaction_script_id = None
        self._media_library_video_type = None
        self._media_name = None
        self._media_size = None
        self._media_video_duration = None
        self._review_status = None
        self._source_type = None
        self._update_time = None
        self._vid = None
        self._video_height = None
        self._video_width = None
        self.discriminator = None

        if activity_video is not None:
            self.activity_video = activity_video
        if cover_image is not None:
            self.cover_image = cover_image
        if create_time is not None:
            self.create_time = create_time
        if creator is not None:
            self.creator = creator
        if failure_time is not None:
            self.failure_time = failure_time
        if folder_id is not None:
            self.folder_id = folder_id
        if folder_name is not None:
            self.folder_name = folder_name
        if id is not None:
            self.id = id
        if interaction_script_id is not None:
            self.interaction_script_id = interaction_script_id
        if media_library_video_type is not None:
            self.media_library_video_type = media_library_video_type
        if media_name is not None:
            self.media_name = media_name
        if media_size is not None:
            self.media_size = media_size
        if media_video_duration is not None:
            self.media_video_duration = media_video_duration
        if review_status is not None:
            self.review_status = review_status
        if source_type is not None:
            self.source_type = source_type
        if update_time is not None:
            self.update_time = update_time
        if vid is not None:
            self.vid = vid
        if video_height is not None:
            self.video_height = video_height
        if video_width is not None:
            self.video_width = video_width

    @property
    def activity_video(self):
        """Gets the activity_video of this DataForListActivityMediaAPIOutput.  # noqa: E501


        :return: The activity_video of this DataForListActivityMediaAPIOutput.  # noqa: E501
        :rtype: list[ActivityVideoForListActivityMediaAPIOutput]
        """
        return self._activity_video

    @activity_video.setter
    def activity_video(self, activity_video):
        """Sets the activity_video of this DataForListActivityMediaAPIOutput.


        :param activity_video: The activity_video of this DataForListActivityMediaAPIOutput.  # noqa: E501
        :type: list[ActivityVideoForListActivityMediaAPIOutput]
        """

        self._activity_video = activity_video

    @property
    def cover_image(self):
        """Gets the cover_image of this DataForListActivityMediaAPIOutput.  # noqa: E501


        :return: The cover_image of this DataForListActivityMediaAPIOutput.  # noqa: E501
        :rtype: str
        """
        return self._cover_image

    @cover_image.setter
    def cover_image(self, cover_image):
        """Sets the cover_image of this DataForListActivityMediaAPIOutput.


        :param cover_image: The cover_image of this DataForListActivityMediaAPIOutput.  # noqa: E501
        :type: str
        """

        self._cover_image = cover_image

    @property
    def create_time(self):
        """Gets the create_time of this DataForListActivityMediaAPIOutput.  # noqa: E501


        :return: The create_time of this DataForListActivityMediaAPIOutput.  # noqa: E501
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this DataForListActivityMediaAPIOutput.


        :param create_time: The create_time of this DataForListActivityMediaAPIOutput.  # noqa: E501
        :type: int
        """

        self._create_time = create_time

    @property
    def creator(self):
        """Gets the creator of this DataForListActivityMediaAPIOutput.  # noqa: E501


        :return: The creator of this DataForListActivityMediaAPIOutput.  # noqa: E501
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this DataForListActivityMediaAPIOutput.


        :param creator: The creator of this DataForListActivityMediaAPIOutput.  # noqa: E501
        :type: str
        """

        self._creator = creator

    @property
    def failure_time(self):
        """Gets the failure_time of this DataForListActivityMediaAPIOutput.  # noqa: E501


        :return: The failure_time of this DataForListActivityMediaAPIOutput.  # noqa: E501
        :rtype: int
        """
        return self._failure_time

    @failure_time.setter
    def failure_time(self, failure_time):
        """Sets the failure_time of this DataForListActivityMediaAPIOutput.


        :param failure_time: The failure_time of this DataForListActivityMediaAPIOutput.  # noqa: E501
        :type: int
        """

        self._failure_time = failure_time

    @property
    def folder_id(self):
        """Gets the folder_id of this DataForListActivityMediaAPIOutput.  # noqa: E501


        :return: The folder_id of this DataForListActivityMediaAPIOutput.  # noqa: E501
        :rtype: int
        """
        return self._folder_id

    @folder_id.setter
    def folder_id(self, folder_id):
        """Sets the folder_id of this DataForListActivityMediaAPIOutput.


        :param folder_id: The folder_id of this DataForListActivityMediaAPIOutput.  # noqa: E501
        :type: int
        """

        self._folder_id = folder_id

    @property
    def folder_name(self):
        """Gets the folder_name of this DataForListActivityMediaAPIOutput.  # noqa: E501


        :return: The folder_name of this DataForListActivityMediaAPIOutput.  # noqa: E501
        :rtype: str
        """
        return self._folder_name

    @folder_name.setter
    def folder_name(self, folder_name):
        """Sets the folder_name of this DataForListActivityMediaAPIOutput.


        :param folder_name: The folder_name of this DataForListActivityMediaAPIOutput.  # noqa: E501
        :type: str
        """

        self._folder_name = folder_name

    @property
    def id(self):
        """Gets the id of this DataForListActivityMediaAPIOutput.  # noqa: E501


        :return: The id of this DataForListActivityMediaAPIOutput.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DataForListActivityMediaAPIOutput.


        :param id: The id of this DataForListActivityMediaAPIOutput.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def interaction_script_id(self):
        """Gets the interaction_script_id of this DataForListActivityMediaAPIOutput.  # noqa: E501


        :return: The interaction_script_id of this DataForListActivityMediaAPIOutput.  # noqa: E501
        :rtype: int
        """
        return self._interaction_script_id

    @interaction_script_id.setter
    def interaction_script_id(self, interaction_script_id):
        """Sets the interaction_script_id of this DataForListActivityMediaAPIOutput.


        :param interaction_script_id: The interaction_script_id of this DataForListActivityMediaAPIOutput.  # noqa: E501
        :type: int
        """

        self._interaction_script_id = interaction_script_id

    @property
    def media_library_video_type(self):
        """Gets the media_library_video_type of this DataForListActivityMediaAPIOutput.  # noqa: E501


        :return: The media_library_video_type of this DataForListActivityMediaAPIOutput.  # noqa: E501
        :rtype: int
        """
        return self._media_library_video_type

    @media_library_video_type.setter
    def media_library_video_type(self, media_library_video_type):
        """Sets the media_library_video_type of this DataForListActivityMediaAPIOutput.


        :param media_library_video_type: The media_library_video_type of this DataForListActivityMediaAPIOutput.  # noqa: E501
        :type: int
        """

        self._media_library_video_type = media_library_video_type

    @property
    def media_name(self):
        """Gets the media_name of this DataForListActivityMediaAPIOutput.  # noqa: E501


        :return: The media_name of this DataForListActivityMediaAPIOutput.  # noqa: E501
        :rtype: str
        """
        return self._media_name

    @media_name.setter
    def media_name(self, media_name):
        """Sets the media_name of this DataForListActivityMediaAPIOutput.


        :param media_name: The media_name of this DataForListActivityMediaAPIOutput.  # noqa: E501
        :type: str
        """

        self._media_name = media_name

    @property
    def media_size(self):
        """Gets the media_size of this DataForListActivityMediaAPIOutput.  # noqa: E501


        :return: The media_size of this DataForListActivityMediaAPIOutput.  # noqa: E501
        :rtype: int
        """
        return self._media_size

    @media_size.setter
    def media_size(self, media_size):
        """Sets the media_size of this DataForListActivityMediaAPIOutput.


        :param media_size: The media_size of this DataForListActivityMediaAPIOutput.  # noqa: E501
        :type: int
        """

        self._media_size = media_size

    @property
    def media_video_duration(self):
        """Gets the media_video_duration of this DataForListActivityMediaAPIOutput.  # noqa: E501


        :return: The media_video_duration of this DataForListActivityMediaAPIOutput.  # noqa: E501
        :rtype: int
        """
        return self._media_video_duration

    @media_video_duration.setter
    def media_video_duration(self, media_video_duration):
        """Sets the media_video_duration of this DataForListActivityMediaAPIOutput.


        :param media_video_duration: The media_video_duration of this DataForListActivityMediaAPIOutput.  # noqa: E501
        :type: int
        """

        self._media_video_duration = media_video_duration

    @property
    def review_status(self):
        """Gets the review_status of this DataForListActivityMediaAPIOutput.  # noqa: E501


        :return: The review_status of this DataForListActivityMediaAPIOutput.  # noqa: E501
        :rtype: int
        """
        return self._review_status

    @review_status.setter
    def review_status(self, review_status):
        """Sets the review_status of this DataForListActivityMediaAPIOutput.


        :param review_status: The review_status of this DataForListActivityMediaAPIOutput.  # noqa: E501
        :type: int
        """

        self._review_status = review_status

    @property
    def source_type(self):
        """Gets the source_type of this DataForListActivityMediaAPIOutput.  # noqa: E501


        :return: The source_type of this DataForListActivityMediaAPIOutput.  # noqa: E501
        :rtype: int
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this DataForListActivityMediaAPIOutput.


        :param source_type: The source_type of this DataForListActivityMediaAPIOutput.  # noqa: E501
        :type: int
        """

        self._source_type = source_type

    @property
    def update_time(self):
        """Gets the update_time of this DataForListActivityMediaAPIOutput.  # noqa: E501


        :return: The update_time of this DataForListActivityMediaAPIOutput.  # noqa: E501
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this DataForListActivityMediaAPIOutput.


        :param update_time: The update_time of this DataForListActivityMediaAPIOutput.  # noqa: E501
        :type: int
        """

        self._update_time = update_time

    @property
    def vid(self):
        """Gets the vid of this DataForListActivityMediaAPIOutput.  # noqa: E501


        :return: The vid of this DataForListActivityMediaAPIOutput.  # noqa: E501
        :rtype: str
        """
        return self._vid

    @vid.setter
    def vid(self, vid):
        """Sets the vid of this DataForListActivityMediaAPIOutput.


        :param vid: The vid of this DataForListActivityMediaAPIOutput.  # noqa: E501
        :type: str
        """

        self._vid = vid

    @property
    def video_height(self):
        """Gets the video_height of this DataForListActivityMediaAPIOutput.  # noqa: E501


        :return: The video_height of this DataForListActivityMediaAPIOutput.  # noqa: E501
        :rtype: int
        """
        return self._video_height

    @video_height.setter
    def video_height(self, video_height):
        """Sets the video_height of this DataForListActivityMediaAPIOutput.


        :param video_height: The video_height of this DataForListActivityMediaAPIOutput.  # noqa: E501
        :type: int
        """

        self._video_height = video_height

    @property
    def video_width(self):
        """Gets the video_width of this DataForListActivityMediaAPIOutput.  # noqa: E501


        :return: The video_width of this DataForListActivityMediaAPIOutput.  # noqa: E501
        :rtype: int
        """
        return self._video_width

    @video_width.setter
    def video_width(self, video_width):
        """Sets the video_width of this DataForListActivityMediaAPIOutput.


        :param video_width: The video_width of this DataForListActivityMediaAPIOutput.  # noqa: E501
        :type: int
        """

        self._video_width = video_width

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
        if issubclass(DataForListActivityMediaAPIOutput, dict):
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
        if not isinstance(other, DataForListActivityMediaAPIOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DataForListActivityMediaAPIOutput):
            return True

        return self.to_dict() != other.to_dict()
