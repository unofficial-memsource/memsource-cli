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

from memsource_cli.models.machine_translate_settings_reference import MachineTranslateSettingsReference  # noqa: F401,E501


class MTSettingsPerLanguageReference(object):
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
        'target_lang': 'str',
        'machine_translate_settings': 'MachineTranslateSettingsReference'
    }

    attribute_map = {
        'target_lang': 'targetLang',
        'machine_translate_settings': 'machineTranslateSettings'
    }

    def __init__(self, target_lang=None, machine_translate_settings=None):  # noqa: E501
        """MTSettingsPerLanguageReference - a model defined in Swagger"""  # noqa: E501

        self._target_lang = None
        self._machine_translate_settings = None
        self.discriminator = None

        if target_lang is not None:
            self.target_lang = target_lang
        if machine_translate_settings is not None:
            self.machine_translate_settings = machine_translate_settings

    @property
    def target_lang(self):
        """Gets the target_lang of this MTSettingsPerLanguageReference.  # noqa: E501

        mtSettings is set for whole project if targetLang == null  # noqa: E501

        :return: The target_lang of this MTSettingsPerLanguageReference.  # noqa: E501
        :rtype: str
        """
        return self._target_lang

    @target_lang.setter
    def target_lang(self, target_lang):
        """Sets the target_lang of this MTSettingsPerLanguageReference.

        mtSettings is set for whole project if targetLang == null  # noqa: E501

        :param target_lang: The target_lang of this MTSettingsPerLanguageReference.  # noqa: E501
        :type: str
        """

        self._target_lang = target_lang

    @property
    def machine_translate_settings(self):
        """Gets the machine_translate_settings of this MTSettingsPerLanguageReference.  # noqa: E501


        :return: The machine_translate_settings of this MTSettingsPerLanguageReference.  # noqa: E501
        :rtype: MachineTranslateSettingsReference
        """
        return self._machine_translate_settings

    @machine_translate_settings.setter
    def machine_translate_settings(self, machine_translate_settings):
        """Sets the machine_translate_settings of this MTSettingsPerLanguageReference.


        :param machine_translate_settings: The machine_translate_settings of this MTSettingsPerLanguageReference.  # noqa: E501
        :type: MachineTranslateSettingsReference
        """

        self._machine_translate_settings = machine_translate_settings

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
        if issubclass(MTSettingsPerLanguageReference, dict):
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
        if not isinstance(other, MTSettingsPerLanguageReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
