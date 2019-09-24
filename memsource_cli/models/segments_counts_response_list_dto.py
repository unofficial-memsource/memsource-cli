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

from memsource_cli.models.segments_counts_response_dto import SegmentsCountsResponseDto  # noqa: F401,E501


class SegmentsCountsResponseListDto(object):
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
        'segments_counts_results': 'list[SegmentsCountsResponseDto]'
    }

    attribute_map = {
        'segments_counts_results': 'segmentsCountsResults'
    }

    def __init__(self, segments_counts_results=None):  # noqa: E501
        """SegmentsCountsResponseListDto - a model defined in Swagger"""  # noqa: E501

        self._segments_counts_results = None
        self.discriminator = None

        if segments_counts_results is not None:
            self.segments_counts_results = segments_counts_results

    @property
    def segments_counts_results(self):
        """Gets the segments_counts_results of this SegmentsCountsResponseListDto.  # noqa: E501


        :return: The segments_counts_results of this SegmentsCountsResponseListDto.  # noqa: E501
        :rtype: list[SegmentsCountsResponseDto]
        """
        return self._segments_counts_results

    @segments_counts_results.setter
    def segments_counts_results(self, segments_counts_results):
        """Sets the segments_counts_results of this SegmentsCountsResponseListDto.


        :param segments_counts_results: The segments_counts_results of this SegmentsCountsResponseListDto.  # noqa: E501
        :type: list[SegmentsCountsResponseDto]
        """

        self._segments_counts_results = segments_counts_results

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
        if issubclass(SegmentsCountsResponseListDto, dict):
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
        if not isinstance(other, SegmentsCountsResponseListDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
