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


class ListQuestionnaireAnswerDataAPIV2Response(object):
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
        'page_item_count': 'int',
        'page_no': 'int',
        'questionnaires': 'list[QuestionnaireForListQuestionnaireAnswerDataAPIV2Output]',
        'questions': 'list[QuestionForListQuestionnaireAnswerDataAPIV2Output]',
        'total_item_count': 'int'
    }

    attribute_map = {
        'page_item_count': 'PageItemCount',
        'page_no': 'PageNo',
        'questionnaires': 'Questionnaires',
        'questions': 'Questions',
        'total_item_count': 'TotalItemCount'
    }

    def __init__(self, page_item_count=None, page_no=None, questionnaires=None, questions=None, total_item_count=None, _configuration=None):  # noqa: E501
        """ListQuestionnaireAnswerDataAPIV2Response - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._page_item_count = None
        self._page_no = None
        self._questionnaires = None
        self._questions = None
        self._total_item_count = None
        self.discriminator = None

        if page_item_count is not None:
            self.page_item_count = page_item_count
        if page_no is not None:
            self.page_no = page_no
        if questionnaires is not None:
            self.questionnaires = questionnaires
        if questions is not None:
            self.questions = questions
        if total_item_count is not None:
            self.total_item_count = total_item_count

    @property
    def page_item_count(self):
        """Gets the page_item_count of this ListQuestionnaireAnswerDataAPIV2Response.  # noqa: E501


        :return: The page_item_count of this ListQuestionnaireAnswerDataAPIV2Response.  # noqa: E501
        :rtype: int
        """
        return self._page_item_count

    @page_item_count.setter
    def page_item_count(self, page_item_count):
        """Sets the page_item_count of this ListQuestionnaireAnswerDataAPIV2Response.


        :param page_item_count: The page_item_count of this ListQuestionnaireAnswerDataAPIV2Response.  # noqa: E501
        :type: int
        """

        self._page_item_count = page_item_count

    @property
    def page_no(self):
        """Gets the page_no of this ListQuestionnaireAnswerDataAPIV2Response.  # noqa: E501


        :return: The page_no of this ListQuestionnaireAnswerDataAPIV2Response.  # noqa: E501
        :rtype: int
        """
        return self._page_no

    @page_no.setter
    def page_no(self, page_no):
        """Sets the page_no of this ListQuestionnaireAnswerDataAPIV2Response.


        :param page_no: The page_no of this ListQuestionnaireAnswerDataAPIV2Response.  # noqa: E501
        :type: int
        """

        self._page_no = page_no

    @property
    def questionnaires(self):
        """Gets the questionnaires of this ListQuestionnaireAnswerDataAPIV2Response.  # noqa: E501


        :return: The questionnaires of this ListQuestionnaireAnswerDataAPIV2Response.  # noqa: E501
        :rtype: list[QuestionnaireForListQuestionnaireAnswerDataAPIV2Output]
        """
        return self._questionnaires

    @questionnaires.setter
    def questionnaires(self, questionnaires):
        """Sets the questionnaires of this ListQuestionnaireAnswerDataAPIV2Response.


        :param questionnaires: The questionnaires of this ListQuestionnaireAnswerDataAPIV2Response.  # noqa: E501
        :type: list[QuestionnaireForListQuestionnaireAnswerDataAPIV2Output]
        """

        self._questionnaires = questionnaires

    @property
    def questions(self):
        """Gets the questions of this ListQuestionnaireAnswerDataAPIV2Response.  # noqa: E501


        :return: The questions of this ListQuestionnaireAnswerDataAPIV2Response.  # noqa: E501
        :rtype: list[QuestionForListQuestionnaireAnswerDataAPIV2Output]
        """
        return self._questions

    @questions.setter
    def questions(self, questions):
        """Sets the questions of this ListQuestionnaireAnswerDataAPIV2Response.


        :param questions: The questions of this ListQuestionnaireAnswerDataAPIV2Response.  # noqa: E501
        :type: list[QuestionForListQuestionnaireAnswerDataAPIV2Output]
        """

        self._questions = questions

    @property
    def total_item_count(self):
        """Gets the total_item_count of this ListQuestionnaireAnswerDataAPIV2Response.  # noqa: E501


        :return: The total_item_count of this ListQuestionnaireAnswerDataAPIV2Response.  # noqa: E501
        :rtype: int
        """
        return self._total_item_count

    @total_item_count.setter
    def total_item_count(self, total_item_count):
        """Sets the total_item_count of this ListQuestionnaireAnswerDataAPIV2Response.


        :param total_item_count: The total_item_count of this ListQuestionnaireAnswerDataAPIV2Response.  # noqa: E501
        :type: int
        """

        self._total_item_count = total_item_count

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
        if issubclass(ListQuestionnaireAnswerDataAPIV2Response, dict):
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
        if not isinstance(other, ListQuestionnaireAnswerDataAPIV2Response):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ListQuestionnaireAnswerDataAPIV2Response):
            return True

        return self.to_dict() != other.to_dict()
