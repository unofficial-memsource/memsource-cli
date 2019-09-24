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


class ErrorDetailDto(object):
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
        'code': 'str',
        'args': 'dict(str, object)',
        'message': 'str'
    }

    attribute_map = {
        'code': 'code',
        'args': 'args',
        'message': 'message'
    }

    def __init__(self, code=None, args=None, message=None):  # noqa: E501
        """ErrorDetailDto - a model defined in Swagger"""  # noqa: E501

        self._code = None
        self._args = None
        self._message = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if args is not None:
            self.args = args
        if message is not None:
            self.message = message

    @property
    def code(self):
        """Gets the code of this ErrorDetailDto.  # noqa: E501

        Code, e.g. NOT_FOUND.  # noqa: E501

        :return: The code of this ErrorDetailDto.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ErrorDetailDto.

        Code, e.g. NOT_FOUND.  # noqa: E501

        :param code: The code of this ErrorDetailDto.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def args(self):
        """Gets the args of this ErrorDetailDto.  # noqa: E501

        Related arguments, e.g. number => \"hello world\"  # noqa: E501

        :return: The args of this ErrorDetailDto.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._args

    @args.setter
    def args(self, args):
        """Sets the args of this ErrorDetailDto.

        Related arguments, e.g. number => \"hello world\"  # noqa: E501

        :param args: The args of this ErrorDetailDto.  # noqa: E501
        :type: dict(str, object)
        """

        self._args = args

    @property
    def message(self):
        """Gets the message of this ErrorDetailDto.  # noqa: E501

        Optional human-readable message.  # noqa: E501

        :return: The message of this ErrorDetailDto.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ErrorDetailDto.

        Optional human-readable message.  # noqa: E501

        :param message: The message of this ErrorDetailDto.  # noqa: E501
        :type: str
        """

        self._message = message

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
        if issubclass(ErrorDetailDto, dict):
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
        if not isinstance(other, ErrorDetailDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
