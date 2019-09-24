# coding: utf-8

"""
    Memsource REST API

    Welcome to Memsource's API documentation. To view our legacy APIs please [visit our documentation](https://wiki.memsource.com/wiki/Memsource_API) and for more information about our new APIs, [visit our blog](https://www.memsource.com/blog/2017/10/24/introducing-rest-apis-qa-with-the-memsource-api-team/).    If you have any questions, please contact [Memsource Support](<mailto:support@memsource.com>).  # noqa: E501

    OpenAPI spec version: Latest
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class TranslationPriceSetCreateDto(object):
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
        'source_languages': 'list[str]',
        'target_languages': 'list[str]'
    }

    attribute_map = {
        'source_languages': 'sourceLanguages',
        'target_languages': 'targetLanguages'
    }

    def __init__(self, source_languages=None, target_languages=None):  # noqa: E501
        """TranslationPriceSetCreateDto - a model defined in Swagger"""  # noqa: E501

        self._source_languages = None
        self._target_languages = None
        self.discriminator = None

        self.source_languages = source_languages
        self.target_languages = target_languages

    @property
    def source_languages(self):
        """Gets the source_languages of this TranslationPriceSetCreateDto.  # noqa: E501


        :return: The source_languages of this TranslationPriceSetCreateDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._source_languages

    @source_languages.setter
    def source_languages(self, source_languages):
        """Sets the source_languages of this TranslationPriceSetCreateDto.


        :param source_languages: The source_languages of this TranslationPriceSetCreateDto.  # noqa: E501
        :type: list[str]
        """
        if source_languages is None:
            raise ValueError("Invalid value for `source_languages`, must not be `None`")  # noqa: E501

        self._source_languages = source_languages

    @property
    def target_languages(self):
        """Gets the target_languages of this TranslationPriceSetCreateDto.  # noqa: E501


        :return: The target_languages of this TranslationPriceSetCreateDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._target_languages

    @target_languages.setter
    def target_languages(self, target_languages):
        """Sets the target_languages of this TranslationPriceSetCreateDto.


        :param target_languages: The target_languages of this TranslationPriceSetCreateDto.  # noqa: E501
        :type: list[str]
        """
        if target_languages is None:
            raise ValueError("Invalid value for `target_languages`, must not be `None`")  # noqa: E501

        self._target_languages = target_languages

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
        if issubclass(TranslationPriceSetCreateDto, dict):
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
        if not isinstance(other, TranslationPriceSetCreateDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
