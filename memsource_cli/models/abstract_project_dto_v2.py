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

from memsource_cli.models.domain_reference import DomainReference  # noqa: F401,E501
from memsource_cli.models.reference_file_reference import ReferenceFileReference  # noqa: F401,E501
from memsource_cli.models.sub_domain_reference import SubDomainReference  # noqa: F401,E501
from memsource_cli.models.user_reference import UserReference  # noqa: F401,E501


class AbstractProjectDtoV2(object):
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
        'uid': 'str',
        'internal_id': 'int',
        'id': 'str',
        'name': 'str',
        'date_created': 'datetime',
        'domain': 'DomainReference',
        'sub_domain': 'SubDomainReference',
        'owner': 'UserReference',
        'source_lang': 'str',
        'target_langs': 'list[str]',
        'references': 'list[ReferenceFileReference]',
        'user_role': 'str'
    }

    attribute_map = {
        'uid': 'uid',
        'internal_id': 'internalId',
        'id': 'id',
        'name': 'name',
        'date_created': 'dateCreated',
        'domain': 'domain',
        'sub_domain': 'subDomain',
        'owner': 'owner',
        'source_lang': 'sourceLang',
        'target_langs': 'targetLangs',
        'references': 'references',
        'user_role': 'userRole'
    }

    discriminator_value_class_map = {
        'Admin, Project Manager (v2)': 'AdminProjectManagerV2',
        'Linguist (v2)': 'LinguistV2'
    }

    def __init__(self, uid=None, internal_id=None, id=None, name=None, date_created=None, domain=None, sub_domain=None, owner=None, source_lang=None, target_langs=None, references=None, user_role=None):  # noqa: E501
        """AbstractProjectDtoV2 - a model defined in Swagger"""  # noqa: E501

        self._uid = None
        self._internal_id = None
        self._id = None
        self._name = None
        self._date_created = None
        self._domain = None
        self._sub_domain = None
        self._owner = None
        self._source_lang = None
        self._target_langs = None
        self._references = None
        self._user_role = None
        self.discriminator = 'userRole'

        if uid is not None:
            self.uid = uid
        if internal_id is not None:
            self.internal_id = internal_id
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if date_created is not None:
            self.date_created = date_created
        if domain is not None:
            self.domain = domain
        if sub_domain is not None:
            self.sub_domain = sub_domain
        if owner is not None:
            self.owner = owner
        if source_lang is not None:
            self.source_lang = source_lang
        if target_langs is not None:
            self.target_langs = target_langs
        if references is not None:
            self.references = references
        if user_role is not None:
            self.user_role = user_role

    @property
    def uid(self):
        """Gets the uid of this AbstractProjectDtoV2.  # noqa: E501


        :return: The uid of this AbstractProjectDtoV2.  # noqa: E501
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this AbstractProjectDtoV2.


        :param uid: The uid of this AbstractProjectDtoV2.  # noqa: E501
        :type: str
        """

        self._uid = uid

    @property
    def internal_id(self):
        """Gets the internal_id of this AbstractProjectDtoV2.  # noqa: E501


        :return: The internal_id of this AbstractProjectDtoV2.  # noqa: E501
        :rtype: int
        """
        return self._internal_id

    @internal_id.setter
    def internal_id(self, internal_id):
        """Sets the internal_id of this AbstractProjectDtoV2.


        :param internal_id: The internal_id of this AbstractProjectDtoV2.  # noqa: E501
        :type: int
        """

        self._internal_id = internal_id

    @property
    def id(self):
        """Gets the id of this AbstractProjectDtoV2.  # noqa: E501


        :return: The id of this AbstractProjectDtoV2.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AbstractProjectDtoV2.


        :param id: The id of this AbstractProjectDtoV2.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this AbstractProjectDtoV2.  # noqa: E501


        :return: The name of this AbstractProjectDtoV2.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AbstractProjectDtoV2.


        :param name: The name of this AbstractProjectDtoV2.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def date_created(self):
        """Gets the date_created of this AbstractProjectDtoV2.  # noqa: E501


        :return: The date_created of this AbstractProjectDtoV2.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this AbstractProjectDtoV2.


        :param date_created: The date_created of this AbstractProjectDtoV2.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def domain(self):
        """Gets the domain of this AbstractProjectDtoV2.  # noqa: E501


        :return: The domain of this AbstractProjectDtoV2.  # noqa: E501
        :rtype: DomainReference
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this AbstractProjectDtoV2.


        :param domain: The domain of this AbstractProjectDtoV2.  # noqa: E501
        :type: DomainReference
        """

        self._domain = domain

    @property
    def sub_domain(self):
        """Gets the sub_domain of this AbstractProjectDtoV2.  # noqa: E501


        :return: The sub_domain of this AbstractProjectDtoV2.  # noqa: E501
        :rtype: SubDomainReference
        """
        return self._sub_domain

    @sub_domain.setter
    def sub_domain(self, sub_domain):
        """Sets the sub_domain of this AbstractProjectDtoV2.


        :param sub_domain: The sub_domain of this AbstractProjectDtoV2.  # noqa: E501
        :type: SubDomainReference
        """

        self._sub_domain = sub_domain

    @property
    def owner(self):
        """Gets the owner of this AbstractProjectDtoV2.  # noqa: E501


        :return: The owner of this AbstractProjectDtoV2.  # noqa: E501
        :rtype: UserReference
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this AbstractProjectDtoV2.


        :param owner: The owner of this AbstractProjectDtoV2.  # noqa: E501
        :type: UserReference
        """

        self._owner = owner

    @property
    def source_lang(self):
        """Gets the source_lang of this AbstractProjectDtoV2.  # noqa: E501


        :return: The source_lang of this AbstractProjectDtoV2.  # noqa: E501
        :rtype: str
        """
        return self._source_lang

    @source_lang.setter
    def source_lang(self, source_lang):
        """Sets the source_lang of this AbstractProjectDtoV2.


        :param source_lang: The source_lang of this AbstractProjectDtoV2.  # noqa: E501
        :type: str
        """

        self._source_lang = source_lang

    @property
    def target_langs(self):
        """Gets the target_langs of this AbstractProjectDtoV2.  # noqa: E501


        :return: The target_langs of this AbstractProjectDtoV2.  # noqa: E501
        :rtype: list[str]
        """
        return self._target_langs

    @target_langs.setter
    def target_langs(self, target_langs):
        """Sets the target_langs of this AbstractProjectDtoV2.


        :param target_langs: The target_langs of this AbstractProjectDtoV2.  # noqa: E501
        :type: list[str]
        """

        self._target_langs = target_langs

    @property
    def references(self):
        """Gets the references of this AbstractProjectDtoV2.  # noqa: E501


        :return: The references of this AbstractProjectDtoV2.  # noqa: E501
        :rtype: list[ReferenceFileReference]
        """
        return self._references

    @references.setter
    def references(self, references):
        """Sets the references of this AbstractProjectDtoV2.


        :param references: The references of this AbstractProjectDtoV2.  # noqa: E501
        :type: list[ReferenceFileReference]
        """

        self._references = references

    @property
    def user_role(self):
        """Gets the user_role of this AbstractProjectDtoV2.  # noqa: E501

        Response differs based on user's role  # noqa: E501

        :return: The user_role of this AbstractProjectDtoV2.  # noqa: E501
        :rtype: str
        """
        return self._user_role

    @user_role.setter
    def user_role(self, user_role):
        """Sets the user_role of this AbstractProjectDtoV2.

        Response differs based on user's role  # noqa: E501

        :param user_role: The user_role of this AbstractProjectDtoV2.  # noqa: E501
        :type: str
        """

        self._user_role = user_role

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        if data[self.discriminator] is not None:
            discriminator_value = data[self.discriminator].lower()

        discriminator_value = data[self.discriminator]
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if issubclass(AbstractProjectDtoV2, dict):
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
        if not isinstance(other, AbstractProjectDtoV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
