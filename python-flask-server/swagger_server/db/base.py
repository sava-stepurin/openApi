from bson.objectid import ObjectId
from swagger_server.utils import object_id_to_str


class CollManager:
    def __init__(self, client):
        self.client = client

    def get_by_id(self, doc_id):
        entry = self.client.find_one({"_id": ObjectId(doc_id)})
        if entry is None:
            return None
        object_id_to_str(entry)
        return list([entry])

    def get_by_acc_id(self, acc_id):
        return list(map(lambda x: object_id_to_str(x),
                        list(self.client.find({"accountId": acc_id}))))

    def add(self, body):
        print(body, body.to_dict(), type(body), type(body.to_dict()))
        return {"id": str(self.client.insert_one(body.to_dict()).inserted_id)}

    def delete_by_id(self, doc_id):
        self.client.delete_one({"_id": ObjectId(doc_id)})

from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiApi(swagger_client.ApiClient())
body = swagger_client.Account(name="taste")
try:
    # Add a new account to the store
    api_instance.add_account(body)
except ApiException as e:
    print("Exception when calling ApiApi->add_account: %s\n" % e)