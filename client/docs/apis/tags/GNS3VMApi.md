<a name="__pageTop"></a>
# openapi_client.apis.tags.gns3_vm_api.GNS3VMApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_engines_v3_gns3vm_engines_get**](#get_engines_v3_gns3vm_engines_get) | **get** /v3/gns3vm/engines | Get Engines
[**get_gns3vm_settings_v3_gns3vm_get**](#get_gns3vm_settings_v3_gns3vm_get) | **get** /v3/gns3vm | Get Gns3Vm Settings
[**get_vms_v3_gns3vm_engines_engine_vms_get**](#get_vms_v3_gns3vm_engines_engine_vms_get) | **get** /v3/gns3vm/engines/{engine}/vms | Get Vms
[**update_gns3vm_settings_v3_gns3vm_put**](#update_gns3vm_settings_v3_gns3vm_put) | **put** /v3/gns3vm | Update Gns3Vm Settings

# **get_engines_v3_gns3vm_engines_get**
<a name="get_engines_v3_gns3vm_engines_get"></a>
> bool, date, datetime, dict, float, int, list, str, none_type get_engines_v3_gns3vm_engines_get()

Get Engines

Return the list of supported engines for the GNS3VM.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import openapi_client
from openapi_client.apis.tags import gns3_vm_api
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
    api_instance = gns3_vm_api.GNS3VMApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Engines
        api_response = api_instance.get_engines_v3_gns3vm_engines_get()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GNS3VMApi->get_engines_v3_gns3vm_engines_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_engines_v3_gns3vm_engines_get.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#get_engines_v3_gns3vm_engines_get.ApiResponseFor422) | Validation Error

#### get_engines_v3_gns3vm_engines_get.ApiResponseFor200
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

#### get_engines_v3_gns3vm_engines_get.ApiResponseFor422
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

# **get_gns3vm_settings_v3_gns3vm_get**
<a name="get_gns3vm_settings_v3_gns3vm_get"></a>
> GNS3VM get_gns3vm_settings_v3_gns3vm_get()

Get Gns3Vm Settings

Return the GNS3 VM settings.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import openapi_client
from openapi_client.apis.tags import gns3_vm_api
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.gns3_vm import GNS3VM
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
    api_instance = gns3_vm_api.GNS3VMApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Gns3Vm Settings
        api_response = api_instance.get_gns3vm_settings_v3_gns3vm_get()
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GNS3VMApi->get_gns3vm_settings_v3_gns3vm_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_gns3vm_settings_v3_gns3vm_get.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#get_gns3vm_settings_v3_gns3vm_get.ApiResponseFor422) | Validation Error

#### get_gns3vm_settings_v3_gns3vm_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GNS3VM**](../../models/GNS3VM.md) |  | 


#### get_gns3vm_settings_v3_gns3vm_get.ApiResponseFor422
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

# **get_vms_v3_gns3vm_engines_engine_vms_get**
<a name="get_vms_v3_gns3vm_engines_engine_vms_get"></a>
> bool, date, datetime, dict, float, int, list, str, none_type get_vms_v3_gns3vm_engines_engine_vms_get(engine)

Get Vms

Return all the available VMs for a specific virtualization engine.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import openapi_client
from openapi_client.apis.tags import gns3_vm_api
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
    api_instance = gns3_vm_api.GNS3VMApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'engine': None,
    }
    try:
        # Get Vms
        api_response = api_instance.get_vms_v3_gns3vm_engines_engine_vms_get(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GNS3VMApi->get_vms_v3_gns3vm_engines_engine_vms_get: %s\n" % e)
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
engine | EngineSchema | | 

# EngineSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_vms_v3_gns3vm_engines_engine_vms_get.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#get_vms_v3_gns3vm_engines_engine_vms_get.ApiResponseFor422) | Validation Error

#### get_vms_v3_gns3vm_engines_engine_vms_get.ApiResponseFor200
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

#### get_vms_v3_gns3vm_engines_engine_vms_get.ApiResponseFor422
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

# **update_gns3vm_settings_v3_gns3vm_put**
<a name="update_gns3vm_settings_v3_gns3vm_put"></a>
> GNS3VM update_gns3vm_settings_v3_gns3vm_put(gns3_vm)

Update Gns3Vm Settings

Update the GNS3 VM settings.

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import openapi_client
from openapi_client.apis.tags import gns3_vm_api
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.gns3_vm import GNS3VM
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
    api_instance = gns3_vm_api.GNS3VMApi(api_client)

    # example passing only required values which don't have defaults set
    body = GNS3VM(None)
    try:
        # Update Gns3Vm Settings
        api_response = api_instance.update_gns3vm_settings_v3_gns3vm_put(
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GNS3VMApi->update_gns3vm_settings_v3_gns3vm_put: %s\n" % e)
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
[**GNS3VM**](../../models/GNS3VM.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_gns3vm_settings_v3_gns3vm_put.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#update_gns3vm_settings_v3_gns3vm_put.ApiResponseFor422) | Validation Error

#### update_gns3vm_settings_v3_gns3vm_put.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GNS3VM**](../../models/GNS3VM.md) |  | 


#### update_gns3vm_settings_v3_gns3vm_put.ApiResponseFor422
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

