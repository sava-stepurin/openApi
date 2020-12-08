import connexion
import six

from swagger_server.models.account import Account  # noqa: E501
from swagger_server.models.deal import Deal  # noqa: E501
from swagger_server.models.debt import Debt  # noqa: E501
from swagger_server.models.person import Person  # noqa: E501
from swagger_server.models.transfer import Transfer  # noqa: E501
from swagger_server import util
from flask import jsonify
from swagger_server.db.client import *


def add_account(body):  # noqa: E501
    """Add a new account to the store

     # noqa: E501

    :param body: Account object that needs to be added to the store
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Account.from_dict(connexion.request.get_json())  # noqa: E501
    return jsonify(accounts_client.add(body))


def add_deal(body):  # noqa: E501
    """Add a new deal to the store

     # noqa: E501

    :param body: Deal object that needs to be added to the store
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Deal.from_dict(connexion.request.get_json())  # noqa: E501
    return jsonify(deals_client.add(body))


def add_person(body):  # noqa: E501
    """Add a new person to the store

     # noqa: E501

    :param body: Person object that needs to be added to the store
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Person.from_dict(connexion.request.get_json())  # noqa: E501
    return jsonify(persons_client.add(body))


def add_transfer(body):  # noqa: E501
    """Add a new transfer to the store

     # noqa: E501

    :param body: Transfer object that needs to be added to the store
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Transfer.from_dict(connexion.request.get_json())  # noqa: E501
    return jsonify(transfers_client.add(body))


def get_accounts(accountId):  # noqa: E501
    """Finds Account by accountId

     # noqa: E501

    :param accountId: Account id
    :type accountId: str

    :rtype: List[Account]
    """
    return jsonify(accounts_client.get_by_acc_id(accountId))


def get_deals(accountId):  # noqa: E501
    """Finds deals by accountId

     # noqa: E501

    :param accountId: Account id
    :type accountId: str

    :rtype: List[Deal]
    """
    return jsonify(transfers_client.get_by_acc_id(accountId))


def get_debts(accountId):  # noqa: E501
    """Finds debts by accountId

     # noqa: E501

    :param accountId: Account id
    :type accountId: str

    :rtype: List[Debt]
    """
    return jsonify(debts_client.get_by_acc_id(accountId))


def get_persons(accountId):  # noqa: E501
    """Finds Persons by accountId

     # noqa: E501

    :param accountId: Account id
    :type accountId: str

    :rtype: List[Person]
    """
    res = persons_client.get_by_acc_id(accountId)
    persons_debts_enrichment(res, accountId)
    return jsonify(res)


def persons_debts_enrichment(persons_list, account_id):
    optimized_debts = debts_client.get_optimized_debts(account_id)
    for debt in optimized_debts:
        debtor_name = persons_client.get_by_id(debt["receiver"])["name"]
        lender_name = persons_client.get_by_id(debt["sender"])["name"]

        for person in persons_list:
            if "debtors" not in person.keys():
                person["debtors"] = []
            if "lenders" not in person.keys():
                person["lenders"] = []

            if person["id"] == debt["sender"]:
                person["debtors"].append({"name": debtor_name,
                                          "amount": debt["amount"]})
            if person["id"] == debt["receiver"]:
                person["lenders"].append({"name": lender_name,
                                          "amount": debt["amount"]})


def get_transfers(accountId):  # noqa: E501
    """Finds Transfers by accountId

     # noqa: E501

    :param accountId: Account id
    :type accountId: str

    :rtype: List[Transfer]
    """
    return jsonify(transfers_client.get_by_acc_id(accountId))
