from pymongo import MongoClient
from urllib.parse import quote_plus
from swagger_server.db.persons import PersonsClient
from swagger_server.db.deals import DealsClient
from swagger_server.db.transfers import TransfersClient
from swagger_server.db.accounts import AccountsClient
from swagger_server.db.debts import DebtsClient

client = MongoClient("127.0.0.1", 27017)
db = client.swagger_server

persons_client = PersonsClient(db.persons)
deals_client = DealsClient(db.deals)
transfers_client = TransfersClient(db.transfers)
accounts_client = AccountsClient(db.accounts)
debts_client = DebtsClient(db.debts)