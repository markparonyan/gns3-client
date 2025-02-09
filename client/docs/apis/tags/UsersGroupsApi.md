<a name="__pageTop"></a>
# openapi_client.apis.tags.users_groups_api.UsersGroupsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_member_to_group_v3_access_groups_user_group_id_members_user_id_put**](#add_member_to_group_v3_access_groups_user_group_id_members_user_id_put) | **put** /v3/access/groups/{user_group_id}/members/{user_id} | Add Member To Group
[**create_user_group_v3_access_groups_post**](#create_user_group_v3_access_groups_post) | **post** /v3/access/groups | Create User Group
[**delete_user_group_v3_access_groups_user_group_id_delete**](#delete_user_group_v3_access_groups_user_group_id_delete) | **delete** /v3/access/groups/{user_group_id} | Delete User Group
[**get_user_group_members_v3_access_groups_user_group_id_members_get**](#get_user_group_members_v3_access_groups_user_group_id_members_get) | **get** /v3/access/groups/{user_group_id}/members | Get User Group Members
[**get_user_group_v3_access_groups_user_group_id_get**](#get_user_group_v3_access_groups_user_group_id_get) | **get** /v3/access/groups/{user_group_id} | Get User Group
[**get_user_groups_v3_access_groups_get**](#get_user_groups_v3_access_groups_get) | **get** /v3/access/groups | Get User Groups
[**remove_member_from_group_v3_access_groups_user_group_id_members_user_id_delete**](#remove_member_from_group_v3_access_groups_user_group_id_members_user_id_delete) | **delete** /v3/access/groups/{user_group_id}/members/{user_id} | Remove Member From Group
[**update_user_group_v3_access_groups_user_group_id_put**](#update_user_group_v3_access_groups_user_group_id_put) | **put** /v3/access/groups/{user_group_id} | Update User Group

# **add_member_to_group_v3_access_groups_user_group_id_members_user_id_put**
<a name="add_member_to_group_v3_access_groups_user_group_id_members_user_id_put"></a>
> add_member_to_group_v3_access_groups_user_group_id_members_user_id_put(user_group_iduser_id)

Add Member To Group

Add member to a user group.  Required privilege: Group.Modify

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import openapi_client
from openapi_client.apis.tags import users_groups_api
from openapi_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2PasswordBearer
configuration = openapi_client.Configuration(
    host = "http://localhost",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_groups_api.UsersGroupsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'user_group_id': None,
        'user_id': None,
    }
    try:
        # Add Member To Group
        api_response = api_instance.add_member_to_group_v3_access_groups_user_group_id_members_user_id_put(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling UsersGroupsApi->add_member_to_group_v3_access_groups_user_group_id_members_user_id_put: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
user_group_id | UserGroupIdSchema | | 
user_id | UserIdSchema | | 

# UserGroupIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | value must be a uuid

# UserIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#add_member_to_group_v3_access_groups_user_group_id_members_user_id_put.ApiResponseFor204) | Successful Response
422 | [ApiResponseFor422](#add_member_to_group_v3_access_groups_user_group_id_members_user_id_put.ApiResponseFor422) | Validation Error

#### add_member_to_group_v3_access_groups_user_group_id_members_user_id_put.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### add_member_to_group_v3_access_groups_user_group_id_members_user_id_put.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

[OAuth2PasswordBearer](../../../README.md#OAuth2PasswordBearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_user_group_v3_access_groups_post**
<a name="create_user_group_v3_access_groups_post"></a>
> UserGroup create_user_group_v3_access_groups_post(user_group_create)

Create User Group

Create a new user group.  Required privilege: Group.Allocate

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import openapi_client
from openapi_client.apis.tags import users_groups_api
from openapi_client.model.user_group_create import UserGroupCreate
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.user_group import UserGroup
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2PasswordBearer
configuration = openapi_client.Configuration(
    host = "http://localhost",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_groups_api.UsersGroupsApi(api_client)

    # example passing only required values which don't have defaults set
    body = UserGroupCreate(None)
    try:
        # Create User Group
        api_response = api_instance.create_user_group_v3_access_groups_post(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UsersGroupsApi->create_user_group_v3_access_groups_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UserGroupCreate**](../../models/UserGroupCreate.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_user_group_v3_access_groups_post.ApiResponseFor201) | Successful Response
422 | [ApiResponseFor422](#create_user_group_v3_access_groups_post.ApiResponseFor422) | Validation Error

#### create_user_group_v3_access_groups_post.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UserGroup**](../../models/UserGroup.md) |  | 


#### create_user_group_v3_access_groups_post.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

[OAuth2PasswordBearer](../../../README.md#OAuth2PasswordBearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_user_group_v3_access_groups_user_group_id_delete**
<a name="delete_user_group_v3_access_groups_user_group_id_delete"></a>
> delete_user_group_v3_access_groups_user_group_id_delete(user_group_id)

Delete User Group

Delete a user group.  Required privilege: Group.Allocate

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import openapi_client
from openapi_client.apis.tags import users_groups_api
from openapi_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2PasswordBearer
configuration = openapi_client.Configuration(
    host = "http://localhost",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_groups_api.UsersGroupsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'user_group_id': None,
    }
    try:
        # Delete User Group
        api_response = api_instance.delete_user_group_v3_access_groups_user_group_id_delete(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling UsersGroupsApi->delete_user_group_v3_access_groups_user_group_id_delete: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
user_group_id | UserGroupIdSchema | | 

# UserGroupIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_user_group_v3_access_groups_user_group_id_delete.ApiResponseFor204) | Successful Response
422 | [ApiResponseFor422](#delete_user_group_v3_access_groups_user_group_id_delete.ApiResponseFor422) | Validation Error

#### delete_user_group_v3_access_groups_user_group_id_delete.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_user_group_v3_access_groups_user_group_id_delete.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

[OAuth2PasswordBearer](../../../README.md#OAuth2PasswordBearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_user_group_members_v3_access_groups_user_group_id_members_get**
<a name="get_user_group_members_v3_access_groups_user_group_id_members_get"></a>
> bool, date, datetime, dict, float, int, list, str, none_type get_user_group_members_v3_access_groups_user_group_id_members_get(user_group_id)

Get User Group Members

Get all user group members.  Required privilege: Group.Audit

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import openapi_client
from openapi_client.apis.tags import users_groups_api
from openapi_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2PasswordBearer
configuration = openapi_client.Configuration(
    host = "http://localhost",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_groups_api.UsersGroupsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'user_group_id': None,
    }
    try:
        # Get User Group Members
        api_response = api_instance.get_user_group_members_v3_access_groups_user_group_id_members_get(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UsersGroupsApi->get_user_group_members_v3_access_groups_user_group_id_members_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
user_group_id | UserGroupIdSchema | | 

# UserGroupIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_user_group_members_v3_access_groups_user_group_id_members_get.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#get_user_group_members_v3_access_groups_user_group_id_members_get.ApiResponseFor422) | Validation Error

#### get_user_group_members_v3_access_groups_user_group_id_members_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

#### get_user_group_members_v3_access_groups_user_group_id_members_get.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

[OAuth2PasswordBearer](../../../README.md#OAuth2PasswordBearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_user_group_v3_access_groups_user_group_id_get**
<a name="get_user_group_v3_access_groups_user_group_id_get"></a>
> UserGroup get_user_group_v3_access_groups_user_group_id_get(user_group_id)

Get User Group

Get a user group.  Required privilege: Group.Audit

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import openapi_client
from openapi_client.apis.tags import users_groups_api
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.user_group import UserGroup
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2PasswordBearer
configuration = openapi_client.Configuration(
    host = "http://localhost",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_groups_api.UsersGroupsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'user_group_id': None,
    }
    try:
        # Get User Group
        api_response = api_instance.get_user_group_v3_access_groups_user_group_id_get(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UsersGroupsApi->get_user_group_v3_access_groups_user_group_id_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
user_group_id | UserGroupIdSchema | | 

# UserGroupIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_user_group_v3_access_groups_user_group_id_get.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#get_user_group_v3_access_groups_user_group_id_get.ApiResponseFor422) | Validation Error

#### get_user_group_v3_access_groups_user_group_id_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UserGroup**](../../models/UserGroup.md) |  | 


#### get_user_group_v3_access_groups_user_group_id_get.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

[OAuth2PasswordBearer](../../../README.md#OAuth2PasswordBearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_user_groups_v3_access_groups_get**
<a name="get_user_groups_v3_access_groups_get"></a>
> bool, date, datetime, dict, float, int, list, str, none_type get_user_groups_v3_access_groups_get()

Get User Groups

Get all user groups.  Required privilege: Group.Audit

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import openapi_client
from openapi_client.apis.tags import users_groups_api
from openapi_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2PasswordBearer
configuration = openapi_client.Configuration(
    host = "http://localhost",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_groups_api.UsersGroupsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get User Groups
        api_response = api_instance.get_user_groups_v3_access_groups_get()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UsersGroupsApi->get_user_groups_v3_access_groups_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_user_groups_v3_access_groups_get.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#get_user_groups_v3_access_groups_get.ApiResponseFor422) | Validation Error

#### get_user_groups_v3_access_groups_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

#### get_user_groups_v3_access_groups_get.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

[OAuth2PasswordBearer](../../../README.md#OAuth2PasswordBearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **remove_member_from_group_v3_access_groups_user_group_id_members_user_id_delete**
<a name="remove_member_from_group_v3_access_groups_user_group_id_members_user_id_delete"></a>
> remove_member_from_group_v3_access_groups_user_group_id_members_user_id_delete(user_group_iduser_id)

Remove Member From Group

Remove member from a user group.  Required privilege: Group.Modify

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import openapi_client
from openapi_client.apis.tags import users_groups_api
from openapi_client.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2PasswordBearer
configuration = openapi_client.Configuration(
    host = "http://localhost",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_groups_api.UsersGroupsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'user_group_id': None,
        'user_id': None,
    }
    try:
        # Remove Member From Group
        api_response = api_instance.remove_member_from_group_v3_access_groups_user_group_id_members_user_id_delete(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling UsersGroupsApi->remove_member_from_group_v3_access_groups_user_group_id_members_user_id_delete: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
user_group_id | UserGroupIdSchema | | 
user_id | UserIdSchema | | 

# UserGroupIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | value must be a uuid

# UserIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#remove_member_from_group_v3_access_groups_user_group_id_members_user_id_delete.ApiResponseFor204) | Successful Response
422 | [ApiResponseFor422](#remove_member_from_group_v3_access_groups_user_group_id_members_user_id_delete.ApiResponseFor422) | Validation Error

#### remove_member_from_group_v3_access_groups_user_group_id_members_user_id_delete.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### remove_member_from_group_v3_access_groups_user_group_id_members_user_id_delete.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

[OAuth2PasswordBearer](../../../README.md#OAuth2PasswordBearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_user_group_v3_access_groups_user_group_id_put**
<a name="update_user_group_v3_access_groups_user_group_id_put"></a>
> UserGroup update_user_group_v3_access_groups_user_group_id_put(user_group_iduser_group_update)

Update User Group

Update a user group.  Required privilege: Group.Modify

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import openapi_client
from openapi_client.apis.tags import users_groups_api
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.user_group_update import UserGroupUpdate
from openapi_client.model.user_group import UserGroup
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2PasswordBearer
configuration = openapi_client.Configuration(
    host = "http://localhost",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = users_groups_api.UsersGroupsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'user_group_id': None,
    }
    body = UserGroupUpdate(None)
    try:
        # Update User Group
        api_response = api_instance.update_user_group_v3_access_groups_user_group_id_put(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UsersGroupsApi->update_user_group_v3_access_groups_user_group_id_put: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UserGroupUpdate**](../../models/UserGroupUpdate.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
user_group_id | UserGroupIdSchema | | 

# UserGroupIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_user_group_v3_access_groups_user_group_id_put.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#update_user_group_v3_access_groups_user_group_id_put.ApiResponseFor422) | Validation Error

#### update_user_group_v3_access_groups_user_group_id_put.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UserGroup**](../../models/UserGroup.md) |  | 


#### update_user_group_v3_access_groups_user_group_id_put.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

[OAuth2PasswordBearer](../../../README.md#OAuth2PasswordBearer)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

