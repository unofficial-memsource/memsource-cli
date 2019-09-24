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

from memsource_cli.models.discount_settings_dto import DiscountSettingsDto  # noqa: F401,E501
from memsource_cli.models.net_rate_scheme_workflow_step_create import NetRateSchemeWorkflowStepCreate  # noqa: F401,E501


class DiscountSchemeCreateDto(object):
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
        'rates': 'DiscountSettingsDto',
        'workflow_step_net_schemes': 'list[NetRateSchemeWorkflowStepCreate]'
    }

    attribute_map = {
        'name': 'name',
        'rates': 'rates',
        'workflow_step_net_schemes': 'workflowStepNetSchemes'
    }

    def __init__(self, name=None, rates=None, workflow_step_net_schemes=None):  # noqa: E501
        """DiscountSchemeCreateDto - a model defined in Swagger"""  # noqa: E501

        self._name = None
        self._rates = None
        self._workflow_step_net_schemes = None
        self.discriminator = None

        self.name = name
        if rates is not None:
            self.rates = rates
        if workflow_step_net_schemes is not None:
            self.workflow_step_net_schemes = workflow_step_net_schemes

    @property
    def name(self):
        """Gets the name of this DiscountSchemeCreateDto.  # noqa: E501


        :return: The name of this DiscountSchemeCreateDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DiscountSchemeCreateDto.


        :param name: The name of this DiscountSchemeCreateDto.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) > 255:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `255`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def rates(self):
        """Gets the rates of this DiscountSchemeCreateDto.  # noqa: E501


        :return: The rates of this DiscountSchemeCreateDto.  # noqa: E501
        :rtype: DiscountSettingsDto
        """
        return self._rates

    @rates.setter
    def rates(self, rates):
        """Sets the rates of this DiscountSchemeCreateDto.


        :param rates: The rates of this DiscountSchemeCreateDto.  # noqa: E501
        :type: DiscountSettingsDto
        """

        self._rates = rates

    @property
    def workflow_step_net_schemes(self):
        """Gets the workflow_step_net_schemes of this DiscountSchemeCreateDto.  # noqa: E501


        :return: The workflow_step_net_schemes of this DiscountSchemeCreateDto.  # noqa: E501
        :rtype: list[NetRateSchemeWorkflowStepCreate]
        """
        return self._workflow_step_net_schemes

    @workflow_step_net_schemes.setter
    def workflow_step_net_schemes(self, workflow_step_net_schemes):
        """Sets the workflow_step_net_schemes of this DiscountSchemeCreateDto.


        :param workflow_step_net_schemes: The workflow_step_net_schemes of this DiscountSchemeCreateDto.  # noqa: E501
        :type: list[NetRateSchemeWorkflowStepCreate]
        """

        self._workflow_step_net_schemes = workflow_step_net_schemes

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
        if issubclass(DiscountSchemeCreateDto, dict):
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
        if not isinstance(other, DiscountSchemeCreateDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
