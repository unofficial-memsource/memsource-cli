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

from memsource_cli.models.id_reference import IdReference  # noqa: F401,E501


class TransMemoryCreateDto(object):
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
        'name': 'str',
        'source_lang': 'str',
        'target_langs': 'list[str]',
        'client': 'IdReference',
        'business_unit': 'IdReference',
        'domain': 'IdReference',
        'sub_domain': 'IdReference',
        'note': 'str'
    }

    attribute_map = {
        'name': 'name',
        'source_lang': 'sourceLang',
        'target_langs': 'targetLangs',
        'client': 'client',
        'business_unit': 'businessUnit',
        'domain': 'domain',
        'sub_domain': 'subDomain',
        'note': 'note'
    }

    def __init__(self, name=None, source_lang=None, target_langs=None, client=None, business_unit=None, domain=None, sub_domain=None, note=None):  # noqa: E501
        """TransMemoryCreateDto - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._source_lang = None
        self._target_langs = None
        self._client = None
        self._business_unit = None
        self._domain = None
        self._sub_domain = None
        self._note = None
        self.discriminator = None

        self.name = name
        self.source_lang = source_lang
        self.target_langs = target_langs
        if client is not None:
            self.client = client
        if business_unit is not None:
            self.business_unit = business_unit
        if domain is not None:
            self.domain = domain
        if sub_domain is not None:
            self.sub_domain = sub_domain
        if note is not None:
            self.note = note

    @property
    def name(self):
        """Gets the name of this TransMemoryCreateDto.  # noqa: E501


        :return: The name of this TransMemoryCreateDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TransMemoryCreateDto.


        :param name: The name of this TransMemoryCreateDto.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 0:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `0`")  # noqa: E501

        self._name = name

    @property
    def source_lang(self):
        """Gets the source_lang of this TransMemoryCreateDto.  # noqa: E501


        :return: The source_lang of this TransMemoryCreateDto.  # noqa: E501
        :rtype: str
        """
        return self._source_lang

    @source_lang.setter
    def source_lang(self, source_lang):
        """Sets the source_lang of this TransMemoryCreateDto.


        :param source_lang: The source_lang of this TransMemoryCreateDto.  # noqa: E501
        :type: str
        """
        if source_lang is None:
            raise ValueError("Invalid value for `source_lang`, must not be `None`")  # noqa: E501

        self._source_lang = source_lang

    @property
    def target_langs(self):
        """Gets the target_langs of this TransMemoryCreateDto.  # noqa: E501


        :return: The target_langs of this TransMemoryCreateDto.  # noqa: E501
        :rtype: list[str]
        """
        return self._target_langs

    @target_langs.setter
    def target_langs(self, target_langs):
        """Sets the target_langs of this TransMemoryCreateDto.


        :param target_langs: The target_langs of this TransMemoryCreateDto.  # noqa: E501
        :type: list[str]
        """
        if target_langs is None:
            raise ValueError("Invalid value for `target_langs`, must not be `None`")  # noqa: E501

        self._target_langs = target_langs

    @property
    def client(self):
        """Gets the client of this TransMemoryCreateDto.  # noqa: E501


        :return: The client of this TransMemoryCreateDto.  # noqa: E501
        :rtype: IdReference
        """
        return self._client

    @client.setter
    def client(self, client):
        """Sets the client of this TransMemoryCreateDto.


        :param client: The client of this TransMemoryCreateDto.  # noqa: E501
        :type: IdReference
        """

        self._client = client

    @property
    def business_unit(self):
        """Gets the business_unit of this TransMemoryCreateDto.  # noqa: E501


        :return: The business_unit of this TransMemoryCreateDto.  # noqa: E501
        :rtype: IdReference
        """
        return self._business_unit

    @business_unit.setter
    def business_unit(self, business_unit):
        """Sets the business_unit of this TransMemoryCreateDto.


        :param business_unit: The business_unit of this TransMemoryCreateDto.  # noqa: E501
        :type: IdReference
        """

        self._business_unit = business_unit

    @property
    def domain(self):
        """Gets the domain of this TransMemoryCreateDto.  # noqa: E501


        :return: The domain of this TransMemoryCreateDto.  # noqa: E501
        :rtype: IdReference
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this TransMemoryCreateDto.


        :param domain: The domain of this TransMemoryCreateDto.  # noqa: E501
        :type: IdReference
        """

        self._domain = domain

    @property
    def sub_domain(self):
        """Gets the sub_domain of this TransMemoryCreateDto.  # noqa: E501


        :return: The sub_domain of this TransMemoryCreateDto.  # noqa: E501
        :rtype: IdReference
        """
        return self._sub_domain

    @sub_domain.setter
    def sub_domain(self, sub_domain):
        """Sets the sub_domain of this TransMemoryCreateDto.


        :param sub_domain: The sub_domain of this TransMemoryCreateDto.  # noqa: E501
        :type: IdReference
        """

        self._sub_domain = sub_domain

    @property
    def note(self):
        """Gets the note of this TransMemoryCreateDto.  # noqa: E501


        :return: The note of this TransMemoryCreateDto.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this TransMemoryCreateDto.


        :param note: The note of this TransMemoryCreateDto.  # noqa: E501
        :type: str
        """
        if note is not None and len(note) > 4096:
            raise ValueError("Invalid value for `note`, length must be less than or equal to `4096`")  # noqa: E501
        if note is not None and len(note) < 0:
            raise ValueError("Invalid value for `note`, length must be greater than or equal to `0`")  # noqa: E501

        self._note = note

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
        if issubclass(TransMemoryCreateDto, dict):
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
        if not isinstance(other, TransMemoryCreateDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
