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
from memsource_cli.models.net_rate_scheme_workflow_step_reference import NetRateSchemeWorkflowStepReference  # noqa: F401,E501
from memsource_cli.models.organization_reference import OrganizationReference  # noqa: F401,E501
from memsource_cli.models.user_reference import UserReference  # noqa: F401,E501


class NetRateScheme(object):
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
        'name': 'str',
        'organization': 'OrganizationReference',
        'date_created': 'datetime',
        'created_by': 'UserReference',
        'workflow_step_net_schemes': 'list[NetRateSchemeWorkflowStepReference]',
        'rates': 'DiscountSettingsDto'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'organization': 'organization',
        'date_created': 'dateCreated',
        'created_by': 'createdBy',
        'workflow_step_net_schemes': 'workflowStepNetSchemes',
        'rates': 'rates'
    }

    def __init__(self, id=None, name=None, organization=None, date_created=None, created_by=None, workflow_step_net_schemes=None, rates=None):  # noqa: E501
        """NetRateScheme - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._organization = None
        self._date_created = None
        self._created_by = None
        self._workflow_step_net_schemes = None
        self._rates = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if organization is not None:
            self.organization = organization
        if date_created is not None:
            self.date_created = date_created
        if created_by is not None:
            self.created_by = created_by
        if workflow_step_net_schemes is not None:
            self.workflow_step_net_schemes = workflow_step_net_schemes
        if rates is not None:
            self.rates = rates

    @property
    def id(self):
        """Gets the id of this NetRateScheme.  # noqa: E501


        :return: The id of this NetRateScheme.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NetRateScheme.


        :param id: The id of this NetRateScheme.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this NetRateScheme.  # noqa: E501


        :return: The name of this NetRateScheme.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NetRateScheme.


        :param name: The name of this NetRateScheme.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def organization(self):
        """Gets the organization of this NetRateScheme.  # noqa: E501


        :return: The organization of this NetRateScheme.  # noqa: E501
        :rtype: OrganizationReference
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this NetRateScheme.


        :param organization: The organization of this NetRateScheme.  # noqa: E501
        :type: OrganizationReference
        """

        self._organization = organization

    @property
    def date_created(self):
        """Gets the date_created of this NetRateScheme.  # noqa: E501


        :return: The date_created of this NetRateScheme.  # noqa: E501
        :rtype: datetime
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this NetRateScheme.


        :param date_created: The date_created of this NetRateScheme.  # noqa: E501
        :type: datetime
        """

        self._date_created = date_created

    @property
    def created_by(self):
        """Gets the created_by of this NetRateScheme.  # noqa: E501


        :return: The created_by of this NetRateScheme.  # noqa: E501
        :rtype: UserReference
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this NetRateScheme.


        :param created_by: The created_by of this NetRateScheme.  # noqa: E501
        :type: UserReference
        """

        self._created_by = created_by

    @property
    def workflow_step_net_schemes(self):
        """Gets the workflow_step_net_schemes of this NetRateScheme.  # noqa: E501


        :return: The workflow_step_net_schemes of this NetRateScheme.  # noqa: E501
        :rtype: list[NetRateSchemeWorkflowStepReference]
        """
        return self._workflow_step_net_schemes

    @workflow_step_net_schemes.setter
    def workflow_step_net_schemes(self, workflow_step_net_schemes):
        """Sets the workflow_step_net_schemes of this NetRateScheme.


        :param workflow_step_net_schemes: The workflow_step_net_schemes of this NetRateScheme.  # noqa: E501
        :type: list[NetRateSchemeWorkflowStepReference]
        """

        self._workflow_step_net_schemes = workflow_step_net_schemes

    @property
    def rates(self):
        """Gets the rates of this NetRateScheme.  # noqa: E501


        :return: The rates of this NetRateScheme.  # noqa: E501
        :rtype: DiscountSettingsDto
        """
        return self._rates

    @rates.setter
    def rates(self, rates):
        """Sets the rates of this NetRateScheme.


        :param rates: The rates of this NetRateScheme.  # noqa: E501
        :type: DiscountSettingsDto
        """

        self._rates = rates

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
        if issubclass(NetRateScheme, dict):
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
        if not isinstance(other, NetRateScheme):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
