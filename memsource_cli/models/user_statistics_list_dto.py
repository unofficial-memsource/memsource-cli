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

from memsource_cli.models.user_statistics_dto import UserStatisticsDto  # noqa: F401,E501


class UserStatisticsListDto(object):
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
        'user_statistics': 'list[UserStatisticsDto]'
    }

    attribute_map = {
        'user_statistics': 'userStatistics'
    }

    def __init__(self, user_statistics=None):  # noqa: E501
        """UserStatisticsListDto - a model defined in Swagger"""  # noqa: E501

        self._user_statistics = None
        self.discriminator = None

        self.user_statistics = user_statistics

    @property
    def user_statistics(self):
        """Gets the user_statistics of this UserStatisticsListDto.  # noqa: E501


        :return: The user_statistics of this UserStatisticsListDto.  # noqa: E501
        :rtype: list[UserStatisticsDto]
        """
        return self._user_statistics

    @user_statistics.setter
    def user_statistics(self, user_statistics):
        """Sets the user_statistics of this UserStatisticsListDto.


        :param user_statistics: The user_statistics of this UserStatisticsListDto.  # noqa: E501
        :type: list[UserStatisticsDto]
        """
        if user_statistics is None:
            raise ValueError("Invalid value for `user_statistics`, must not be `None`")  # noqa: E501

        self._user_statistics = user_statistics

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
        if issubclass(UserStatisticsListDto, dict):
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
        if not isinstance(other, UserStatisticsListDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
