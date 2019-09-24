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

from memsource_cli.models.counts_dto import CountsDto  # noqa: F401,E501
from memsource_cli.models.match_counts101_dto import MatchCounts101Dto  # noqa: F401,E501
from memsource_cli.models.match_counts_dto import MatchCountsDto  # noqa: F401,E501
from memsource_cli.models.match_counts_nt_dto import MatchCountsNTDto  # noqa: F401,E501


class DataDto(object):
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
        'available': 'bool',
        'all': 'CountsDto',
        'repetitions': 'CountsDto',
        'trans_memory_matches': 'MatchCounts101Dto',
        'machine_translation_matches': 'MatchCountsDto',
        'non_translatables_matches': 'MatchCountsNTDto'
    }

    attribute_map = {
        'available': 'available',
        'all': 'all',
        'repetitions': 'repetitions',
        'trans_memory_matches': 'transMemoryMatches',
        'machine_translation_matches': 'machineTranslationMatches',
        'non_translatables_matches': 'nonTranslatablesMatches'
    }

    def __init__(self, available=None, all=None, repetitions=None, trans_memory_matches=None, machine_translation_matches=None, non_translatables_matches=None):  # noqa: E501
        """DataDto - a model defined in Swagger"""  # noqa: E501

        self._available = None
        self._all = None
        self._repetitions = None
        self._trans_memory_matches = None
        self._machine_translation_matches = None
        self._non_translatables_matches = None
        self.discriminator = None

        if available is not None:
            self.available = available
        if all is not None:
            self.all = all
        if repetitions is not None:
            self.repetitions = repetitions
        if trans_memory_matches is not None:
            self.trans_memory_matches = trans_memory_matches
        if machine_translation_matches is not None:
            self.machine_translation_matches = machine_translation_matches
        if non_translatables_matches is not None:
            self.non_translatables_matches = non_translatables_matches

    @property
    def available(self):
        """Gets the available of this DataDto.  # noqa: E501


        :return: The available of this DataDto.  # noqa: E501
        :rtype: bool
        """
        return self._available

    @available.setter
    def available(self, available):
        """Sets the available of this DataDto.


        :param available: The available of this DataDto.  # noqa: E501
        :type: bool
        """

        self._available = available

    @property
    def all(self):
        """Gets the all of this DataDto.  # noqa: E501


        :return: The all of this DataDto.  # noqa: E501
        :rtype: CountsDto
        """
        return self._all

    @all.setter
    def all(self, all):
        """Sets the all of this DataDto.


        :param all: The all of this DataDto.  # noqa: E501
        :type: CountsDto
        """

        self._all = all

    @property
    def repetitions(self):
        """Gets the repetitions of this DataDto.  # noqa: E501


        :return: The repetitions of this DataDto.  # noqa: E501
        :rtype: CountsDto
        """
        return self._repetitions

    @repetitions.setter
    def repetitions(self, repetitions):
        """Sets the repetitions of this DataDto.


        :param repetitions: The repetitions of this DataDto.  # noqa: E501
        :type: CountsDto
        """

        self._repetitions = repetitions

    @property
    def trans_memory_matches(self):
        """Gets the trans_memory_matches of this DataDto.  # noqa: E501


        :return: The trans_memory_matches of this DataDto.  # noqa: E501
        :rtype: MatchCounts101Dto
        """
        return self._trans_memory_matches

    @trans_memory_matches.setter
    def trans_memory_matches(self, trans_memory_matches):
        """Sets the trans_memory_matches of this DataDto.


        :param trans_memory_matches: The trans_memory_matches of this DataDto.  # noqa: E501
        :type: MatchCounts101Dto
        """

        self._trans_memory_matches = trans_memory_matches

    @property
    def machine_translation_matches(self):
        """Gets the machine_translation_matches of this DataDto.  # noqa: E501


        :return: The machine_translation_matches of this DataDto.  # noqa: E501
        :rtype: MatchCountsDto
        """
        return self._machine_translation_matches

    @machine_translation_matches.setter
    def machine_translation_matches(self, machine_translation_matches):
        """Sets the machine_translation_matches of this DataDto.


        :param machine_translation_matches: The machine_translation_matches of this DataDto.  # noqa: E501
        :type: MatchCountsDto
        """

        self._machine_translation_matches = machine_translation_matches

    @property
    def non_translatables_matches(self):
        """Gets the non_translatables_matches of this DataDto.  # noqa: E501


        :return: The non_translatables_matches of this DataDto.  # noqa: E501
        :rtype: MatchCountsNTDto
        """
        return self._non_translatables_matches

    @non_translatables_matches.setter
    def non_translatables_matches(self, non_translatables_matches):
        """Sets the non_translatables_matches of this DataDto.


        :param non_translatables_matches: The non_translatables_matches of this DataDto.  # noqa: E501
        :type: MatchCountsNTDto
        """

        self._non_translatables_matches = non_translatables_matches

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
        if issubclass(DataDto, dict):
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
        if not isinstance(other, DataDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
