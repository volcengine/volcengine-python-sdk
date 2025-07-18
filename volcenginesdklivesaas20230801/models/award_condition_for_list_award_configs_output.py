# coding: utf-8

"""
    livesaas20230801

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: common-version
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from volcenginesdkcore.configuration import Configuration


class AwardConditionForListAwardConfigsOutput(object):
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
        'check_in': 'str',
        'questionnaire': 'str',
        'quiz': 'str',
        'right_quiz': 'str',
        'vote': 'str'
    }

    attribute_map = {
        'check_in': 'CheckIn',
        'questionnaire': 'Questionnaire',
        'quiz': 'Quiz',
        'right_quiz': 'RightQuiz',
        'vote': 'Vote'
    }

    def __init__(self, check_in=None, questionnaire=None, quiz=None, right_quiz=None, vote=None, _configuration=None):  # noqa: E501
        """AwardConditionForListAwardConfigsOutput - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._check_in = None
        self._questionnaire = None
        self._quiz = None
        self._right_quiz = None
        self._vote = None
        self.discriminator = None

        if check_in is not None:
            self.check_in = check_in
        if questionnaire is not None:
            self.questionnaire = questionnaire
        if quiz is not None:
            self.quiz = quiz
        if right_quiz is not None:
            self.right_quiz = right_quiz
        if vote is not None:
            self.vote = vote

    @property
    def check_in(self):
        """Gets the check_in of this AwardConditionForListAwardConfigsOutput.  # noqa: E501


        :return: The check_in of this AwardConditionForListAwardConfigsOutput.  # noqa: E501
        :rtype: str
        """
        return self._check_in

    @check_in.setter
    def check_in(self, check_in):
        """Sets the check_in of this AwardConditionForListAwardConfigsOutput.


        :param check_in: The check_in of this AwardConditionForListAwardConfigsOutput.  # noqa: E501
        :type: str
        """

        self._check_in = check_in

    @property
    def questionnaire(self):
        """Gets the questionnaire of this AwardConditionForListAwardConfigsOutput.  # noqa: E501


        :return: The questionnaire of this AwardConditionForListAwardConfigsOutput.  # noqa: E501
        :rtype: str
        """
        return self._questionnaire

    @questionnaire.setter
    def questionnaire(self, questionnaire):
        """Sets the questionnaire of this AwardConditionForListAwardConfigsOutput.


        :param questionnaire: The questionnaire of this AwardConditionForListAwardConfigsOutput.  # noqa: E501
        :type: str
        """

        self._questionnaire = questionnaire

    @property
    def quiz(self):
        """Gets the quiz of this AwardConditionForListAwardConfigsOutput.  # noqa: E501


        :return: The quiz of this AwardConditionForListAwardConfigsOutput.  # noqa: E501
        :rtype: str
        """
        return self._quiz

    @quiz.setter
    def quiz(self, quiz):
        """Sets the quiz of this AwardConditionForListAwardConfigsOutput.


        :param quiz: The quiz of this AwardConditionForListAwardConfigsOutput.  # noqa: E501
        :type: str
        """

        self._quiz = quiz

    @property
    def right_quiz(self):
        """Gets the right_quiz of this AwardConditionForListAwardConfigsOutput.  # noqa: E501


        :return: The right_quiz of this AwardConditionForListAwardConfigsOutput.  # noqa: E501
        :rtype: str
        """
        return self._right_quiz

    @right_quiz.setter
    def right_quiz(self, right_quiz):
        """Sets the right_quiz of this AwardConditionForListAwardConfigsOutput.


        :param right_quiz: The right_quiz of this AwardConditionForListAwardConfigsOutput.  # noqa: E501
        :type: str
        """

        self._right_quiz = right_quiz

    @property
    def vote(self):
        """Gets the vote of this AwardConditionForListAwardConfigsOutput.  # noqa: E501


        :return: The vote of this AwardConditionForListAwardConfigsOutput.  # noqa: E501
        :rtype: str
        """
        return self._vote

    @vote.setter
    def vote(self, vote):
        """Sets the vote of this AwardConditionForListAwardConfigsOutput.


        :param vote: The vote of this AwardConditionForListAwardConfigsOutput.  # noqa: E501
        :type: str
        """

        self._vote = vote

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
        if issubclass(AwardConditionForListAwardConfigsOutput, dict):
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
        if not isinstance(other, AwardConditionForListAwardConfigsOutput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AwardConditionForListAwardConfigsOutput):
            return True

        return self.to_dict() != other.to_dict()
