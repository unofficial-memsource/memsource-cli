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

from memsource_cli.models.user_reference import UserReference  # noqa: F401,E501


class TermV2Dto(object):
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
        'id': 'str',
        'text': 'str',
        'lang': 'str',
        'rtl': 'bool',
        'modified_at': 'datetime',
        'created_at': 'datetime',
        'modified_by': 'UserReference',
        'created_by': 'UserReference',
        'case_sensitive': 'bool',
        'exact_match': 'bool',
        'forbidden': 'bool',
        'preferred': 'bool',
        'status': 'str',
        'concept_id': 'str',
        'usage': 'str',
        'note': 'str',
        'writable': 'bool',
        'short_translation': 'str',
        'term_type': 'str',
        'part_of_speech': 'str',
        'gender': 'str',
        'number': 'str'
    }

    attribute_map = {
        'id': 'id',
        'text': 'text',
        'lang': 'lang',
        'rtl': 'rtl',
        'modified_at': 'modifiedAt',
        'created_at': 'createdAt',
        'modified_by': 'modifiedBy',
        'created_by': 'createdBy',
        'case_sensitive': 'caseSensitive',
        'exact_match': 'exactMatch',
        'forbidden': 'forbidden',
        'preferred': 'preferred',
        'status': 'status',
        'concept_id': 'conceptId',
        'usage': 'usage',
        'note': 'note',
        'writable': 'writable',
        'short_translation': 'shortTranslation',
        'term_type': 'termType',
        'part_of_speech': 'partOfSpeech',
        'gender': 'gender',
        'number': 'number'
    }

    def __init__(self, id=None, text=None, lang=None, rtl=None, modified_at=None, created_at=None, modified_by=None, created_by=None, case_sensitive=None, exact_match=None, forbidden=None, preferred=None, status=None, concept_id=None, usage=None, note=None, writable=None, short_translation=None, term_type=None, part_of_speech=None, gender=None, number=None):  # noqa: E501
        """TermV2Dto - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._text = None
        self._lang = None
        self._rtl = None
        self._modified_at = None
        self._created_at = None
        self._modified_by = None
        self._created_by = None
        self._case_sensitive = None
        self._exact_match = None
        self._forbidden = None
        self._preferred = None
        self._status = None
        self._concept_id = None
        self._usage = None
        self._note = None
        self._writable = None
        self._short_translation = None
        self._term_type = None
        self._part_of_speech = None
        self._gender = None
        self._number = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if text is not None:
            self.text = text
        if lang is not None:
            self.lang = lang
        if rtl is not None:
            self.rtl = rtl
        if modified_at is not None:
            self.modified_at = modified_at
        if created_at is not None:
            self.created_at = created_at
        if modified_by is not None:
            self.modified_by = modified_by
        if created_by is not None:
            self.created_by = created_by
        if case_sensitive is not None:
            self.case_sensitive = case_sensitive
        if exact_match is not None:
            self.exact_match = exact_match
        if forbidden is not None:
            self.forbidden = forbidden
        if preferred is not None:
            self.preferred = preferred
        if status is not None:
            self.status = status
        if concept_id is not None:
            self.concept_id = concept_id
        if usage is not None:
            self.usage = usage
        if note is not None:
            self.note = note
        if writable is not None:
            self.writable = writable
        if short_translation is not None:
            self.short_translation = short_translation
        if term_type is not None:
            self.term_type = term_type
        if part_of_speech is not None:
            self.part_of_speech = part_of_speech
        if gender is not None:
            self.gender = gender
        if number is not None:
            self.number = number

    @property
    def id(self):
        """Gets the id of this TermV2Dto.  # noqa: E501


        :return: The id of this TermV2Dto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TermV2Dto.


        :param id: The id of this TermV2Dto.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def text(self):
        """Gets the text of this TermV2Dto.  # noqa: E501


        :return: The text of this TermV2Dto.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this TermV2Dto.


        :param text: The text of this TermV2Dto.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def lang(self):
        """Gets the lang of this TermV2Dto.  # noqa: E501


        :return: The lang of this TermV2Dto.  # noqa: E501
        :rtype: str
        """
        return self._lang

    @lang.setter
    def lang(self, lang):
        """Sets the lang of this TermV2Dto.


        :param lang: The lang of this TermV2Dto.  # noqa: E501
        :type: str
        """

        self._lang = lang

    @property
    def rtl(self):
        """Gets the rtl of this TermV2Dto.  # noqa: E501


        :return: The rtl of this TermV2Dto.  # noqa: E501
        :rtype: bool
        """
        return self._rtl

    @rtl.setter
    def rtl(self, rtl):
        """Sets the rtl of this TermV2Dto.


        :param rtl: The rtl of this TermV2Dto.  # noqa: E501
        :type: bool
        """

        self._rtl = rtl

    @property
    def modified_at(self):
        """Gets the modified_at of this TermV2Dto.  # noqa: E501


        :return: The modified_at of this TermV2Dto.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this TermV2Dto.


        :param modified_at: The modified_at of this TermV2Dto.  # noqa: E501
        :type: datetime
        """

        self._modified_at = modified_at

    @property
    def created_at(self):
        """Gets the created_at of this TermV2Dto.  # noqa: E501


        :return: The created_at of this TermV2Dto.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this TermV2Dto.


        :param created_at: The created_at of this TermV2Dto.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def modified_by(self):
        """Gets the modified_by of this TermV2Dto.  # noqa: E501


        :return: The modified_by of this TermV2Dto.  # noqa: E501
        :rtype: UserReference
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        """Sets the modified_by of this TermV2Dto.


        :param modified_by: The modified_by of this TermV2Dto.  # noqa: E501
        :type: UserReference
        """

        self._modified_by = modified_by

    @property
    def created_by(self):
        """Gets the created_by of this TermV2Dto.  # noqa: E501


        :return: The created_by of this TermV2Dto.  # noqa: E501
        :rtype: UserReference
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this TermV2Dto.


        :param created_by: The created_by of this TermV2Dto.  # noqa: E501
        :type: UserReference
        """

        self._created_by = created_by

    @property
    def case_sensitive(self):
        """Gets the case_sensitive of this TermV2Dto.  # noqa: E501


        :return: The case_sensitive of this TermV2Dto.  # noqa: E501
        :rtype: bool
        """
        return self._case_sensitive

    @case_sensitive.setter
    def case_sensitive(self, case_sensitive):
        """Sets the case_sensitive of this TermV2Dto.


        :param case_sensitive: The case_sensitive of this TermV2Dto.  # noqa: E501
        :type: bool
        """

        self._case_sensitive = case_sensitive

    @property
    def exact_match(self):
        """Gets the exact_match of this TermV2Dto.  # noqa: E501


        :return: The exact_match of this TermV2Dto.  # noqa: E501
        :rtype: bool
        """
        return self._exact_match

    @exact_match.setter
    def exact_match(self, exact_match):
        """Sets the exact_match of this TermV2Dto.


        :param exact_match: The exact_match of this TermV2Dto.  # noqa: E501
        :type: bool
        """

        self._exact_match = exact_match

    @property
    def forbidden(self):
        """Gets the forbidden of this TermV2Dto.  # noqa: E501


        :return: The forbidden of this TermV2Dto.  # noqa: E501
        :rtype: bool
        """
        return self._forbidden

    @forbidden.setter
    def forbidden(self, forbidden):
        """Sets the forbidden of this TermV2Dto.


        :param forbidden: The forbidden of this TermV2Dto.  # noqa: E501
        :type: bool
        """

        self._forbidden = forbidden

    @property
    def preferred(self):
        """Gets the preferred of this TermV2Dto.  # noqa: E501


        :return: The preferred of this TermV2Dto.  # noqa: E501
        :rtype: bool
        """
        return self._preferred

    @preferred.setter
    def preferred(self, preferred):
        """Sets the preferred of this TermV2Dto.


        :param preferred: The preferred of this TermV2Dto.  # noqa: E501
        :type: bool
        """

        self._preferred = preferred

    @property
    def status(self):
        """Gets the status of this TermV2Dto.  # noqa: E501


        :return: The status of this TermV2Dto.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TermV2Dto.


        :param status: The status of this TermV2Dto.  # noqa: E501
        :type: str
        """
        allowed_values = ["New", "Approved"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def concept_id(self):
        """Gets the concept_id of this TermV2Dto.  # noqa: E501


        :return: The concept_id of this TermV2Dto.  # noqa: E501
        :rtype: str
        """
        return self._concept_id

    @concept_id.setter
    def concept_id(self, concept_id):
        """Sets the concept_id of this TermV2Dto.


        :param concept_id: The concept_id of this TermV2Dto.  # noqa: E501
        :type: str
        """

        self._concept_id = concept_id

    @property
    def usage(self):
        """Gets the usage of this TermV2Dto.  # noqa: E501


        :return: The usage of this TermV2Dto.  # noqa: E501
        :rtype: str
        """
        return self._usage

    @usage.setter
    def usage(self, usage):
        """Sets the usage of this TermV2Dto.


        :param usage: The usage of this TermV2Dto.  # noqa: E501
        :type: str
        """

        self._usage = usage

    @property
    def note(self):
        """Gets the note of this TermV2Dto.  # noqa: E501


        :return: The note of this TermV2Dto.  # noqa: E501
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this TermV2Dto.


        :param note: The note of this TermV2Dto.  # noqa: E501
        :type: str
        """

        self._note = note

    @property
    def writable(self):
        """Gets the writable of this TermV2Dto.  # noqa: E501


        :return: The writable of this TermV2Dto.  # noqa: E501
        :rtype: bool
        """
        return self._writable

    @writable.setter
    def writable(self, writable):
        """Sets the writable of this TermV2Dto.


        :param writable: The writable of this TermV2Dto.  # noqa: E501
        :type: bool
        """

        self._writable = writable

    @property
    def short_translation(self):
        """Gets the short_translation of this TermV2Dto.  # noqa: E501


        :return: The short_translation of this TermV2Dto.  # noqa: E501
        :rtype: str
        """
        return self._short_translation

    @short_translation.setter
    def short_translation(self, short_translation):
        """Sets the short_translation of this TermV2Dto.


        :param short_translation: The short_translation of this TermV2Dto.  # noqa: E501
        :type: str
        """

        self._short_translation = short_translation

    @property
    def term_type(self):
        """Gets the term_type of this TermV2Dto.  # noqa: E501


        :return: The term_type of this TermV2Dto.  # noqa: E501
        :rtype: str
        """
        return self._term_type

    @term_type.setter
    def term_type(self, term_type):
        """Sets the term_type of this TermV2Dto.


        :param term_type: The term_type of this TermV2Dto.  # noqa: E501
        :type: str
        """

        self._term_type = term_type

    @property
    def part_of_speech(self):
        """Gets the part_of_speech of this TermV2Dto.  # noqa: E501


        :return: The part_of_speech of this TermV2Dto.  # noqa: E501
        :rtype: str
        """
        return self._part_of_speech

    @part_of_speech.setter
    def part_of_speech(self, part_of_speech):
        """Sets the part_of_speech of this TermV2Dto.


        :param part_of_speech: The part_of_speech of this TermV2Dto.  # noqa: E501
        :type: str
        """

        self._part_of_speech = part_of_speech

    @property
    def gender(self):
        """Gets the gender of this TermV2Dto.  # noqa: E501


        :return: The gender of this TermV2Dto.  # noqa: E501
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this TermV2Dto.


        :param gender: The gender of this TermV2Dto.  # noqa: E501
        :type: str
        """

        self._gender = gender

    @property
    def number(self):
        """Gets the number of this TermV2Dto.  # noqa: E501


        :return: The number of this TermV2Dto.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this TermV2Dto.


        :param number: The number of this TermV2Dto.  # noqa: E501
        :type: str
        """

        self._number = number

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
        if issubclass(TermV2Dto, dict):
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
        if not isinstance(other, TermV2Dto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
