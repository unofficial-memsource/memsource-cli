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


class BrowseRequestDto(object):
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
        'query_lang': 'str',
        'query': 'str',
        'status': 'str',
        'page_number': 'int',
        'page_size': 'int'
    }

    attribute_map = {
        'query_lang': 'queryLang',
        'query': 'query',
        'status': 'status',
        'page_number': 'pageNumber',
        'page_size': 'pageSize'
    }

    def __init__(self, query_lang=None, query=None, status=None, page_number=None, page_size=None):  # noqa: E501
        """BrowseRequestDto - a model defined in Swagger"""  # noqa: E501

        self._query_lang = None
        self._query = None
        self._status = None
        self._page_number = None
        self._page_size = None
        self.discriminator = None

        if query_lang is not None:
            self.query_lang = query_lang
        if query is not None:
            self.query = query
        if status is not None:
            self.status = status
        if page_number is not None:
            self.page_number = page_number
        if page_size is not None:
            self.page_size = page_size

    @property
    def query_lang(self):
        """Gets the query_lang of this BrowseRequestDto.  # noqa: E501


        :return: The query_lang of this BrowseRequestDto.  # noqa: E501
        :rtype: str
        """
        return self._query_lang

    @query_lang.setter
    def query_lang(self, query_lang):
        """Sets the query_lang of this BrowseRequestDto.


        :param query_lang: The query_lang of this BrowseRequestDto.  # noqa: E501
        :type: str
        """

        self._query_lang = query_lang

    @property
    def query(self):
        """Gets the query of this BrowseRequestDto.  # noqa: E501


        :return: The query of this BrowseRequestDto.  # noqa: E501
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this BrowseRequestDto.


        :param query: The query of this BrowseRequestDto.  # noqa: E501
        :type: str
        """

        self._query = query

    @property
    def status(self):
        """Gets the status of this BrowseRequestDto.  # noqa: E501


        :return: The status of this BrowseRequestDto.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this BrowseRequestDto.


        :param status: The status of this BrowseRequestDto.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def page_number(self):
        """Gets the page_number of this BrowseRequestDto.  # noqa: E501


        :return: The page_number of this BrowseRequestDto.  # noqa: E501
        :rtype: int
        """
        return self._page_number

    @page_number.setter
    def page_number(self, page_number):
        """Sets the page_number of this BrowseRequestDto.


        :param page_number: The page_number of this BrowseRequestDto.  # noqa: E501
        :type: int
        """

        self._page_number = page_number

    @property
    def page_size(self):
        """Gets the page_size of this BrowseRequestDto.  # noqa: E501


        :return: The page_size of this BrowseRequestDto.  # noqa: E501
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this BrowseRequestDto.


        :param page_size: The page_size of this BrowseRequestDto.  # noqa: E501
        :type: int
        """
        if page_size is not None and page_size > 50:  # noqa: E501
            raise ValueError("Invalid value for `page_size`, must be a value less than or equal to `50`")  # noqa: E501
        if page_size is not None and page_size < 1:  # noqa: E501
            raise ValueError("Invalid value for `page_size`, must be a value greater than or equal to `1`")  # noqa: E501

        self._page_size = page_size

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
        if issubclass(BrowseRequestDto, dict):
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
        if not isinstance(other, BrowseRequestDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
