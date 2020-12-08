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


class Debt(object):
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
        'amount': 'float',
        'receiver': 'str',
        'sender': 'str'
    }

    attribute_map = {
        'account_id': 'accountId',
        'amount': 'amount',
        'receiver': 'receiver',
        'sender': 'sender'
    }

    def __init__(self, account_id=None, amount=None, receiver=None, sender=None):  # noqa: E501
        """Debt - a model defined in Swagger"""  # noqa: E501

        self._account_id = None
        self._amount = None
        self._receiver = None
        self._sender = None
        self.discriminator = None

        self.account_id = account_id
        self.amount = amount
        self.receiver = receiver
        self.sender = sender

    @property
    def account_id(self):
        """Gets the account_id of this Debt.  # noqa: E501


        :return: The account_id of this Debt.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this Debt.


        :param account_id: The account_id of this Debt.  # noqa: E501
        :type: str
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")  # noqa: E501

        self._account_id = account_id

    @property
    def amount(self):
        """Gets the amount of this Debt.  # noqa: E501


        :return: The amount of this Debt.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Debt.


        :param amount: The amount of this Debt.  # noqa: E501
        :type: float
        """
        if amount is None:
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def receiver(self):
        """Gets the receiver of this Debt.  # noqa: E501


        :return: The receiver of this Debt.  # noqa: E501
        :rtype: str
        """
        return self._receiver

    @receiver.setter
    def receiver(self, receiver):
        """Sets the receiver of this Debt.


        :param receiver: The receiver of this Debt.  # noqa: E501
        :type: str
        """
        if receiver is None:
            raise ValueError("Invalid value for `receiver`, must not be `None`")  # noqa: E501

        self._receiver = receiver

    @property
    def sender(self):
        """Gets the sender of this Debt.  # noqa: E501


        :return: The sender of this Debt.  # noqa: E501
        :rtype: str
        """
        return self._sender

    @sender.setter
    def sender(self, sender):
        """Sets the sender of this Debt.


        :param sender: The sender of this Debt.  # noqa: E501
        :type: str
        """
        if sender is None:
            raise ValueError("Invalid value for `sender`, must not be `None`")  # noqa: E501

        self._sender = sender

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
        if issubclass(Debt, dict):
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
        if not isinstance(other, Debt):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other