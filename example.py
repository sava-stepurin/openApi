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
