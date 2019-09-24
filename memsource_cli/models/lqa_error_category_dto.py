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

# from memsource_cli.models.lqa_error_category_dto import LqaErrorCategoryDto  # noqa: F401,E501


class LqaErrorCategoryDto(object):
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
        'error_category_id': 'int',
        'name': 'str',
        'enabled': 'bool',
        'error_categories': 'list[LqaErrorCategoryDto]'
    }

    attribute_map = {
        'error_category_id': 'errorCategoryId',
        'name': 'name',
        'enabled': 'enabled',
        'error_categories': 'errorCategories'
    }

    def __init__(self, error_category_id=None, name=None, enabled=None, error_categories=None):  # noqa: E501
        """LqaErrorCategoryDto - a model defined in Swagger"""  # noqa: E501

        self._error_category_id = None
        self._name = None
        self._enabled = None
        self._error_categories = None
        self.discriminator = None

        if error_category_id is not None:
            self.error_category_id = error_category_id
        if name is not None:
            self.name = name
        if enabled is not None:
            self.enabled = enabled
        if error_categories is not None:
            self.error_categories = error_categories

    @property
    def error_category_id(self):
        """Gets the error_category_id of this LqaErrorCategoryDto.  # noqa: E501


        :return: The error_category_id of this LqaErrorCategoryDto.  # noqa: E501
        :rtype: int
        """
        return self._error_category_id

    @error_category_id.setter
    def error_category_id(self, error_category_id):
        """Sets the error_category_id of this LqaErrorCategoryDto.


        :param error_category_id: The error_category_id of this LqaErrorCategoryDto.  # noqa: E501
        :type: int
        """

        self._error_category_id = error_category_id

    @property
    def name(self):
        """Gets the name of this LqaErrorCategoryDto.  # noqa: E501


        :return: The name of this LqaErrorCategoryDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LqaErrorCategoryDto.


        :param name: The name of this LqaErrorCategoryDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def enabled(self):
        """Gets the enabled of this LqaErrorCategoryDto.  # noqa: E501


        :return: The enabled of this LqaErrorCategoryDto.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this LqaErrorCategoryDto.


        :param enabled: The enabled of this LqaErrorCategoryDto.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def error_categories(self):
        """Gets the error_categories of this LqaErrorCategoryDto.  # noqa: E501


        :return: The error_categories of this LqaErrorCategoryDto.  # noqa: E501
        :rtype: list[LqaErrorCategoryDto]
        """
        return self._error_categories

    @error_categories.setter
    def error_categories(self, error_categories):
        """Sets the error_categories of this LqaErrorCategoryDto.


        :param error_categories: The error_categories of this LqaErrorCategoryDto.  # noqa: E501
        :type: list[LqaErrorCategoryDto]
        """

        self._error_categories = error_categories

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
        if issubclass(LqaErrorCategoryDto, dict):
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
        if not isinstance(other, LqaErrorCategoryDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
