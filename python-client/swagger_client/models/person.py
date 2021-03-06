# coding: utf-8

"""
    Buycycle

    DevOps homework  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Person(object):
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
        'account_id': 'str',
        'debtors': 'list[PersonDebtors]',
        'lenders': 'list[PersonDebtors]',
        'name': 'str'
    }

    attribute_map = {
        'account_id': 'accountId',
        'debtors': 'debtors',
        'lenders': 'lenders',
        'name': 'name'
    }

    def __init__(self, account_id=None, debtors=None, lenders=None, name=None):  # noqa: E501
        """Person - a model defined in Swagger"""  # noqa: E501

        self._account_id = None
        self._debtors = None
        self._lenders = None
        self._name = None
        self.discriminator = None

        self.account_id = account_id
        if debtors is not None:
            self.debtors = debtors
        if lenders is not None:
            self.lenders = lenders
        self.name = name

    @property
    def account_id(self):
        """Gets the account_id of this Person.  # noqa: E501


        :return: The account_id of this Person.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this Person.


        :param account_id: The account_id of this Person.  # noqa: E501
        :type: str
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def debtors(self):
        """Gets the debtors of this Person.  # noqa: E501


        :return: The debtors of this Person.  # noqa: E501
        :rtype: list[PersonDebtors]
        """
        return self._debtors

    @debtors.setter
    def debtors(self, debtors):
        """Sets the debtors of this Person.


        :param debtors: The debtors of this Person.  # noqa: E501
        :type: list[PersonDebtors]
        """

        self._debtors = debtors

    @property
    def lenders(self):
        """Gets the lenders of this Person.  # noqa: E501


        :return: The lenders of this Person.  # noqa: E501
        :rtype: list[PersonDebtors]
        """
        return self._lenders

    @lenders.setter
    def lenders(self, lenders):
        """Sets the lenders of this Person.


        :param lenders: The lenders of this Person.  # noqa: E501
        :type: list[PersonDebtors]
        """

        self._lenders = lenders

    @property
    def name(self):
        """Gets the name of this Person.  # noqa: E501


        :return: The name of this Person.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Person.


        :param name: The name of this Person.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

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
        if issubclass(Person, dict):
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
        if not isinstance(other, Person):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
