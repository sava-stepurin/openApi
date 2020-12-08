# swagger_client.ApiApi

All URIs are relative to *http://127.0.0.1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_account**](ApiApi.md#add_account) | **POST** /api/addAccount | Add a new account to the store
[**add_deal**](ApiApi.md#add_deal) | **POST** /api/addDeal | Add a new deal to the store
[**add_person**](ApiApi.md#add_person) | **POST** /api/addPerson | Add a new person to the store
[**add_transfer**](ApiApi.md#add_transfer) | **POST** /api/addTransfer | Add a new transfer to the store
[**get_accounts**](ApiApi.md#get_accounts) | **GET** /api/getAccounts | Finds Accounts by accountId
[**get_deals**](ApiApi.md#get_deals) | **GET** /api/getDeals | Finds deals by accountId
[**get_debts**](ApiApi.md#get_debts) | **GET** /api/getDebts | Finds debts by accountId
[**get_persons**](ApiApi.md#get_persons) | **GET** /api/getPersons | Finds Persons by accountId
[**get_transfers**](ApiApi.md#get_transfers) | **GET** /api/getTransfers | Finds Transfers by accountId


# **add_account**
> add_account(body)

Add a new account to the store



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiApi()
body = swagger_client.Account() # Account | Account object that needs to be added to the store

try:
    # Add a new account to the store
    api_instance.add_account(body)
except ApiException as e:
    print("Exception when calling ApiApi->add_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Account**](Account.md)| Account object that needs to be added to the store | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_deal**
> add_deal(body)

Add a new deal to the store



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiApi()
body = swagger_client.Deal() # Deal | Deal object that needs to be added to the store

try:
    # Add a new deal to the store
    api_instance.add_deal(body)
except ApiException as e:
    print("Exception when calling ApiApi->add_deal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Deal**](Deal.md)| Deal object that needs to be added to the store | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_person**
> add_person(body)

Add a new person to the store



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiApi()
body = swagger_client.Person() # Person | Person object that needs to be added to the store

try:
    # Add a new person to the store
    api_instance.add_person(body)
except ApiException as e:
    print("Exception when calling ApiApi->add_person: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Person**](Person.md)| Person object that needs to be added to the store | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_transfer**
> add_transfer(body)

Add a new transfer to the store



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiApi()
body = swagger_client.Transfer() # Transfer | Transfer object that needs to be added to the store

try:
    # Add a new transfer to the store
    api_instance.add_transfer(body)
except ApiException as e:
    print("Exception when calling ApiApi->add_transfer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Transfer**](Transfer.md)| Transfer object that needs to be added to the store | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accounts**
> list[Account] get_accounts(account_id)

Finds Accounts by accountId

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiApi()
account_id = 'account_id_example' # str | Account id

try:
    # Finds Accounts by accountId
    api_response = api_instance.get_accounts(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->get_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account id | 

### Return type

[**list[Account]**](Account.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_deals**
> list[Deal] get_deals(account_id)

Finds deals by accountId

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiApi()
account_id = 'account_id_example' # str | Account id

try:
    # Finds deals by accountId
    api_response = api_instance.get_deals(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->get_deals: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account id | 

### Return type

[**list[Deal]**](Deal.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_debts**
> list[Debt] get_debts(account_id)

Finds debts by accountId

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiApi()
account_id = 'account_id_example' # str | Account id

try:
    # Finds debts by accountId
    api_response = api_instance.get_debts(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->get_debts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account id | 

### Return type

[**list[Debt]**](Debt.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_persons**
> list[Person] get_persons(account_id)

Finds Persons by accountId

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiApi()
account_id = 'account_id_example' # str | Account id

try:
    # Finds Persons by accountId
    api_response = api_instance.get_persons(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->get_persons: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account id | 

### Return type

[**list[Person]**](Person.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_transfers**
> list[Transfer] get_transfers(account_id)

Finds Transfers by accountId

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ApiApi()
account_id = 'account_id_example' # str | Account id

try:
    # Finds Transfers by accountId
    api_response = api_instance.get_transfers(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->get_transfers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**| Account id | 

### Return type

[**list[Transfer]**](Transfer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

