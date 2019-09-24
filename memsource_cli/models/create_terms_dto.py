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

from memsource_cli.models.term_create_by_job_dto import TermCreateByJobDto  # noqa: F401,E501


class CreateTermsDto(object):
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
        'source_term': 'TermCreateByJobDto',
        'target_term': 'TermCreateByJobDto'
    }

    attribute_map = {
        'source_term': 'sourceTerm',
        'target_term': 'targetTerm'
    }

    def __init__(self, source_term=None, target_term=None):  # noqa: E501
        """CreateTermsDto - a model defined in Swagger"""  # noqa: E501

        self._source_term = None
        self._target_term = None
        self.discriminator = None

        self.source_term = source_term
        self.target_term = target_term

    @property
    def source_term(self):
        """Gets the source_term of this CreateTermsDto.  # noqa: E501


        :return: The source_term of this CreateTermsDto.  # noqa: E501
        :rtype: TermCreateByJobDto
        """
        return self._source_term

    @source_term.setter
    def source_term(self, source_term):
        """Sets the source_term of this CreateTermsDto.


        :param source_term: The source_term of this CreateTermsDto.  # noqa: E501
        :type: TermCreateByJobDto
        """
        if source_term is None:
            raise ValueError("Invalid value for `source_term`, must not be `None`")  # noqa: E501

        self._source_term = source_term

    @property
    def target_term(self):
        """Gets the target_term of this CreateTermsDto.  # noqa: E501


        :return: The target_term of this CreateTermsDto.  # noqa: E501
        :rtype: TermCreateByJobDto
        """
        return self._target_term

    @target_term.setter
    def target_term(self, target_term):
        """Sets the target_term of this CreateTermsDto.


        :param target_term: The target_term of this CreateTermsDto.  # noqa: E501
        :type: TermCreateByJobDto
        """
        if target_term is None:
            raise ValueError("Invalid value for `target_term`, must not be `None`")  # noqa: E501

        self._target_term = target_term

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
        if issubclass(CreateTermsDto, dict):
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
        if not isinstance(other, CreateTermsDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
