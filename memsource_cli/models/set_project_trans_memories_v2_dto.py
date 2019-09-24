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
from memsource_cli.models.set_project_trans_memory_dto import SetProjectTransMemoryDto  # noqa: F401,E501


class SetProjectTransMemoriesV2Dto(object):
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
        'trans_memories': 'list[SetProjectTransMemoryDto]',
        'target_lang': 'str',
        'workflow_step': 'IdReference'
    }

    attribute_map = {
        'trans_memories': 'transMemories',
        'target_lang': 'targetLang',
        'workflow_step': 'workflowStep'
    }

    def __init__(self, trans_memories=None, target_lang=None, workflow_step=None):  # noqa: E501
        """SetProjectTransMemoriesV2Dto - a model defined in Swagger"""  # noqa: E501

        self._trans_memories = None
        self._target_lang = None
        self._workflow_step = None
        self.discriminator = None

        if trans_memories is not None:
            self.trans_memories = trans_memories
        if target_lang is not None:
            self.target_lang = target_lang
        if workflow_step is not None:
            self.workflow_step = workflow_step

    @property
    def trans_memories(self):
        """Gets the trans_memories of this SetProjectTransMemoriesV2Dto.  # noqa: E501


        :return: The trans_memories of this SetProjectTransMemoriesV2Dto.  # noqa: E501
        :rtype: list[SetProjectTransMemoryDto]
        """
        return self._trans_memories

    @trans_memories.setter
    def trans_memories(self, trans_memories):
        """Sets the trans_memories of this SetProjectTransMemoriesV2Dto.


        :param trans_memories: The trans_memories of this SetProjectTransMemoriesV2Dto.  # noqa: E501
        :type: list[SetProjectTransMemoryDto]
        """

        self._trans_memories = trans_memories

    @property
    def target_lang(self):
        """Gets the target_lang of this SetProjectTransMemoriesV2Dto.  # noqa: E501

        Set translation memory only for the specific project target language  # noqa: E501

        :return: The target_lang of this SetProjectTransMemoriesV2Dto.  # noqa: E501
        :rtype: str
        """
        return self._target_lang

    @target_lang.setter
    def target_lang(self, target_lang):
        """Sets the target_lang of this SetProjectTransMemoriesV2Dto.

        Set translation memory only for the specific project target language  # noqa: E501

        :param target_lang: The target_lang of this SetProjectTransMemoriesV2Dto.  # noqa: E501
        :type: str
        """

        self._target_lang = target_lang

    @property
    def workflow_step(self):
        """Gets the workflow_step of this SetProjectTransMemoriesV2Dto.  # noqa: E501

        Set translation memory only for the specific workflow step  # noqa: E501

        :return: The workflow_step of this SetProjectTransMemoriesV2Dto.  # noqa: E501
        :rtype: IdReference
        """
        return self._workflow_step

    @workflow_step.setter
    def workflow_step(self, workflow_step):
        """Sets the workflow_step of this SetProjectTransMemoriesV2Dto.

        Set translation memory only for the specific workflow step  # noqa: E501

        :param workflow_step: The workflow_step of this SetProjectTransMemoriesV2Dto.  # noqa: E501
        :type: IdReference
        """

        self._workflow_step = workflow_step

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
        if issubclass(SetProjectTransMemoriesV2Dto, dict):
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
        if not isinstance(other, SetProjectTransMemoriesV2Dto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
