<a name="__pageTop"></a>
# openapi_client.apis.tags.nodes_api.NodesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auto_idlepc_v3_projects_project_id_nodes_node_id_dynamips_auto_idlepc_get**](#auto_idlepc_v3_projects_project_id_nodes_node_id_dynamips_auto_idlepc_get) | **get** /v3/projects/{project_id}/nodes/{node_id}/dynamips/auto_idlepc | Auto Idlepc
[**console_reset_v3_projects_project_id_nodes_node_id_console_reset_post**](#console_reset_v3_projects_project_id_nodes_node_id_console_reset_post) | **post** /v3/projects/{project_id}/nodes/{node_id}/console/reset | Console Reset
[**create_disk_image_v3_projects_project_id_nodes_node_id_qemu_disk_image_disk_name_post**](#create_disk_image_v3_projects_project_id_nodes_node_id_qemu_disk_image_disk_name_post) | **post** /v3/projects/{project_id}/nodes/{node_id}/qemu/disk_image/{disk_name} | Create Disk Image
[**create_node_v3_projects_project_id_nodes_post**](#create_node_v3_projects_project_id_nodes_post) | **post** /v3/projects/{project_id}/nodes | Create Node
[**delete_disk_image_v3_projects_project_id_nodes_node_id_qemu_disk_image_disk_name_delete**](#delete_disk_image_v3_projects_project_id_nodes_node_id_qemu_disk_image_disk_name_delete) | **delete** /v3/projects/{project_id}/nodes/{node_id}/qemu/disk_image/{disk_name} | Delete Disk Image
[**delete_node_v3_projects_project_id_nodes_node_id_delete**](#delete_node_v3_projects_project_id_nodes_node_id_delete) | **delete** /v3/projects/{project_id}/nodes/{node_id} | Delete Node
[**duplicate_node_v3_projects_project_id_nodes_node_id_duplicate_post**](#duplicate_node_v3_projects_project_id_nodes_node_id_duplicate_post) | **post** /v3/projects/{project_id}/nodes/{node_id}/duplicate | Duplicate Node
[**get_file_v3_projects_project_id_nodes_node_id_files_file_path_get**](#get_file_v3_projects_project_id_nodes_node_id_files_file_path_get) | **get** /v3/projects/{project_id}/nodes/{node_id}/files/{file_path} | Get File
[**get_node_links_v3_projects_project_id_nodes_node_id_links_get**](#get_node_links_v3_projects_project_id_nodes_node_id_links_get) | **get** /v3/projects/{project_id}/nodes/{node_id}/links | Get Node Links
[**get_node_v3_projects_project_id_nodes_node_id_get**](#get_node_v3_projects_project_id_nodes_node_id_get) | **get** /v3/projects/{project_id}/nodes/{node_id} | Get Node
[**get_nodes_v3_projects_project_id_nodes_get**](#get_nodes_v3_projects_project_id_nodes_get) | **get** /v3/projects/{project_id}/nodes | Get Nodes
[**idlepc_proposals_v3_projects_project_id_nodes_node_id_dynamips_idlepc_proposals_get**](#idlepc_proposals_v3_projects_project_id_nodes_node_id_dynamips_idlepc_proposals_get) | **get** /v3/projects/{project_id}/nodes/{node_id}/dynamips/idlepc_proposals | Idlepc Proposals
[**isolate_node_v3_projects_project_id_nodes_node_id_isolate_post**](#isolate_node_v3_projects_project_id_nodes_node_id_isolate_post) | **post** /v3/projects/{project_id}/nodes/{node_id}/isolate | Isolate Node
[**post_file_v3_projects_project_id_nodes_node_id_files_file_path_post**](#post_file_v3_projects_project_id_nodes_node_id_files_file_path_post) | **post** /v3/projects/{project_id}/nodes/{node_id}/files/{file_path} | Post File
[**reload_all_nodes_v3_projects_project_id_nodes_reload_post**](#reload_all_nodes_v3_projects_project_id_nodes_reload_post) | **post** /v3/projects/{project_id}/nodes/reload | Reload All Nodes
[**reload_node_v3_projects_project_id_nodes_node_id_reload_post**](#reload_node_v3_projects_project_id_nodes_node_id_reload_post) | **post** /v3/projects/{project_id}/nodes/{node_id}/reload | Reload Node
[**reset_console_all_nodes_v3_projects_project_id_nodes_console_reset_post**](#reset_console_all_nodes_v3_projects_project_id_nodes_console_reset_post) | **post** /v3/projects/{project_id}/nodes/console/reset | Reset Console All Nodes
[**start_all_nodes_v3_projects_project_id_nodes_start_post**](#start_all_nodes_v3_projects_project_id_nodes_start_post) | **post** /v3/projects/{project_id}/nodes/start | Start All Nodes
[**start_node_v3_projects_project_id_nodes_node_id_start_post**](#start_node_v3_projects_project_id_nodes_node_id_start_post) | **post** /v3/projects/{project_id}/nodes/{node_id}/start | Start Node
[**stop_all_nodes_v3_projects_project_id_nodes_stop_post**](#stop_all_nodes_v3_projects_project_id_nodes_stop_post) | **post** /v3/projects/{project_id}/nodes/stop | Stop All Nodes
[**stop_node_v3_projects_project_id_nodes_node_id_stop_post**](#stop_node_v3_projects_project_id_nodes_node_id_stop_post) | **post** /v3/projects/{project_id}/nodes/{node_id}/stop | Stop Node
[**suspend_all_nodes_v3_projects_project_id_nodes_suspend_post**](#suspend_all_nodes_v3_projects_project_id_nodes_suspend_post) | **post** /v3/projects/{project_id}/nodes/suspend | Suspend All Nodes
[**suspend_node_v3_projects_project_id_nodes_node_id_suspend_post**](#suspend_node_v3_projects_project_id_nodes_node_id_suspend_post) | **post** /v3/projects/{project_id}/nodes/{node_id}/suspend | Suspend Node
[**unisolate_node_v3_projects_project_id_nodes_node_id_unisolate_post**](#unisolate_node_v3_projects_project_id_nodes_node_id_unisolate_post) | **post** /v3/projects/{project_id}/nodes/{node_id}/unisolate | Unisolate Node
[**update_disk_image_v3_projects_project_id_nodes_node_id_qemu_disk_image_disk_name_put**](#update_disk_image_v3_projects_project_id_nodes_node_id_qemu_disk_image_disk_name_put) | **put** /v3/projects/{project_id}/nodes/{node_id}/qemu/disk_image/{disk_name} | Update Disk Image
[**update_node_v3_projects_project_id_nodes_node_id_put**](#update_node_v3_projects_project_id_nodes_node_id_put) | **put** /v3/projects/{project_id}/nodes/{node_id} | Update Node

# **auto_idlepc_v3_projects_project_id_nodes_node_id_dynamips_auto_idlepc_get**
<a name="auto_idlepc_v3_projects_project_id_nodes_node_id_dynamips_auto_idlepc_get"></a>
> bool, date, datetime, dict, float, int, list, str, none_type auto_idlepc_v3_projects_project_id_nodes_node_id_dynamips_auto_idlepc_get(node_idproject_id)

Auto Idlepc

Compute an Idle-PC value for a Dynamips node  Required privilege: Node.Audit

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import openapi_client
from openapi_client.apis.tags import nodes_api
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.error_message import ErrorMessage
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
    api_instance = nodes_api.NodesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'node_id': None,
        'project_id': None,
    }
    try:
        # Auto Idlepc
        api_response = api_instance.auto_idlepc_v3_projects_project_id_nodes_node_id_dynamips_auto_idlepc_get(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NodesApi->auto_idlepc_v3_projects_project_id_nodes_node_id_dynamips_auto_idlepc_get: %s\n" % e)
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
node_id | NodeIdSchema | | 
project_id | ProjectIdSchema | | 

# NodeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | value must be a uuid

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#auto_idlepc_v3_projects_project_id_nodes_node_id_dynamips_auto_idlepc_get.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#auto_idlepc_v3_projects_project_id_nodes_node_id_dynamips_auto_idlepc_get.ApiResponseFor404) | Could not find project or node
422 | [ApiResponseFor422](#auto_idlepc_v3_projects_project_id_nodes_node_id_dynamips_auto_idlepc_get.ApiResponseFor422) | Validation Error

#### auto_idlepc_v3_projects_project_id_nodes_node_id_dynamips_auto_idlepc_get.ApiResponseFor200
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

#### auto_idlepc_v3_projects_project_id_nodes_node_id_dynamips_auto_idlepc_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorMessage**](../../models/ErrorMessage.md) |  | 


#### auto_idlepc_v3_projects_project_id_nodes_node_id_dynamips_auto_idlepc_get.ApiResponseFor422
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

# **console_reset_v3_projects_project_id_nodes_node_id_console_reset_post**
<a name="console_reset_v3_projects_project_id_nodes_node_id_console_reset_post"></a>
> console_reset_v3_projects_project_id_nodes_node_id_console_reset_post(node_idproject_id)

Console Reset

Reset a console for a given node.  Required privilege: Node.Console

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import openapi_client
from openapi_client.apis.tags import nodes_api
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.error_message import ErrorMessage
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
    api_instance = nodes_api.NodesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'node_id': None,
        'project_id': None,
    }
    try:
        # Console Reset
        api_response = api_instance.console_reset_v3_projects_project_id_nodes_node_id_console_reset_post(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling NodesApi->console_reset_v3_projects_project_id_nodes_node_id_console_reset_post: %s\n" % e)
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
node_id | NodeIdSchema | | 
project_id | ProjectIdSchema | | 

# NodeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | value must be a uuid

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#console_reset_v3_projects_project_id_nodes_node_id_console_reset_post.ApiResponseFor204) | Successful Response
404 | [ApiResponseFor404](#console_reset_v3_projects_project_id_nodes_node_id_console_reset_post.ApiResponseFor404) | Could not find project or node
422 | [ApiResponseFor422](#console_reset_v3_projects_project_id_nodes_node_id_console_reset_post.ApiResponseFor422) | Validation Error

#### console_reset_v3_projects_project_id_nodes_node_id_console_reset_post.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### console_reset_v3_projects_project_id_nodes_node_id_console_reset_post.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorMessage**](../../models/ErrorMessage.md) |  | 


#### console_reset_v3_projects_project_id_nodes_node_id_console_reset_post.ApiResponseFor422
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

# **create_disk_image_v3_projects_project_id_nodes_node_id_qemu_disk_image_disk_name_post**
<a name="create_disk_image_v3_projects_project_id_nodes_node_id_qemu_disk_image_disk_name_post"></a>
> create_disk_image_v3_projects_project_id_nodes_node_id_qemu_disk_image_disk_name_post(disk_namenode_idproject_idqemu_disk_image_create)

Create Disk Image

Create a Qemu disk image.  Required privilege: Node.Allocate

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import openapi_client
from openapi_client.apis.tags import nodes_api
from openapi_client.model.qemu_disk_image_create import QemuDiskImageCreate
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.error_message import ErrorMessage
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
    api_instance = nodes_api.NodesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'disk_name': None,
        'node_id': None,
        'project_id': None,
    }
    body = QemuDiskImageCreate(None)
    try:
        # Create Disk Image
        api_response = api_instance.create_disk_image_v3_projects_project_id_nodes_node_id_qemu_disk_image_disk_name_post(
            path_params=path_params,
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling NodesApi->create_disk_image_v3_projects_project_id_nodes_node_id_qemu_disk_image_disk_name_post: %s\n" % e)
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
[**QemuDiskImageCreate**](../../models/QemuDiskImageCreate.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
disk_name | DiskNameSchema | | 
node_id | NodeIdSchema | | 
project_id | ProjectIdSchema | | 

# DiskNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# NodeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | value must be a uuid

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#create_disk_image_v3_projects_project_id_nodes_node_id_qemu_disk_image_disk_name_post.ApiResponseFor204) | Successful Response
404 | [ApiResponseFor404](#create_disk_image_v3_projects_project_id_nodes_node_id_qemu_disk_image_disk_name_post.ApiResponseFor404) | Could not find project or node
422 | [ApiResponseFor422](#create_disk_image_v3_projects_project_id_nodes_node_id_qemu_disk_image_disk_name_post.ApiResponseFor422) | Validation Error

#### create_disk_image_v3_projects_project_id_nodes_node_id_qemu_disk_image_disk_name_post.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### create_disk_image_v3_projects_project_id_nodes_node_id_qemu_disk_image_disk_name_post.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorMessage**](../../models/ErrorMessage.md) |  | 


#### create_disk_image_v3_projects_project_id_nodes_node_id_qemu_disk_image_disk_name_post.ApiResponseFor422
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

# **create_node_v3_projects_project_id_nodes_post**
<a name="create_node_v3_projects_project_id_nodes_post"></a>
> Node create_node_v3_projects_project_id_nodes_post(project_idnode_create)

Create Node

Create a new node.  Required privilege: Node.Allocate

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import openapi_client
from openapi_client.apis.tags import nodes_api
from openapi_client.model.node import Node
from openapi_client.model.node_create import NodeCreate
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.error_message import ErrorMessage
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
    api_instance = nodes_api.NodesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'project_id': None,
    }
    body = NodeCreate(None)
    try:
        # Create Node
        api_response = api_instance.create_node_v3_projects_project_id_nodes_post(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NodesApi->create_node_v3_projects_project_id_nodes_post: %s\n" % e)
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
[**NodeCreate**](../../models/NodeCreate.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
project_id | ProjectIdSchema | | 

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_node_v3_projects_project_id_nodes_post.ApiResponseFor201) | Successful Response
404 | [ApiResponseFor404](#create_node_v3_projects_project_id_nodes_post.ApiResponseFor404) | Could not find project
409 | [ApiResponseFor409](#create_node_v3_projects_project_id_nodes_post.ApiResponseFor409) | Could not create node
422 | [ApiResponseFor422](#create_node_v3_projects_project_id_nodes_post.ApiResponseFor422) | Validation Error

#### create_node_v3_projects_project_id_nodes_post.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Node**](../../models/Node.md) |  | 


#### create_node_v3_projects_project_id_nodes_post.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorMessage**](../../models/ErrorMessage.md) |  | 


#### create_node_v3_projects_project_id_nodes_post.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorMessage**](../../models/ErrorMessage.md) |  | 


#### create_node_v3_projects_project_id_nodes_post.ApiResponseFor422
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

# **delete_disk_image_v3_projects_project_id_nodes_node_id_qemu_disk_image_disk_name_delete**
<a name="delete_disk_image_v3_projects_project_id_nodes_node_id_qemu_disk_image_disk_name_delete"></a>
> delete_disk_image_v3_projects_project_id_nodes_node_id_qemu_disk_image_disk_name_delete(disk_namenode_idproject_id)

Delete Disk Image

Delete a Qemu disk image.  Required privilege: Node.Allocate

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import openapi_client
from openapi_client.apis.tags import nodes_api
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.error_message import ErrorMessage
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
    api_instance = nodes_api.NodesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'disk_name': None,
        'node_id': None,
        'project_id': None,
    }
    try:
        # Delete Disk Image
        api_response = api_instance.delete_disk_image_v3_projects_project_id_nodes_node_id_qemu_disk_image_disk_name_delete(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling NodesApi->delete_disk_image_v3_projects_project_id_nodes_node_id_qemu_disk_image_disk_name_delete: %s\n" % e)
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
disk_name | DiskNameSchema | | 
node_id | NodeIdSchema | | 
project_id | ProjectIdSchema | | 

# DiskNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# NodeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | value must be a uuid

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_disk_image_v3_projects_project_id_nodes_node_id_qemu_disk_image_disk_name_delete.ApiResponseFor204) | Successful Response
404 | [ApiResponseFor404](#delete_disk_image_v3_projects_project_id_nodes_node_id_qemu_disk_image_disk_name_delete.ApiResponseFor404) | Could not find project or node
422 | [ApiResponseFor422](#delete_disk_image_v3_projects_project_id_nodes_node_id_qemu_disk_image_disk_name_delete.ApiResponseFor422) | Validation Error

#### delete_disk_image_v3_projects_project_id_nodes_node_id_qemu_disk_image_disk_name_delete.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_disk_image_v3_projects_project_id_nodes_node_id_qemu_disk_image_disk_name_delete.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorMessage**](../../models/ErrorMessage.md) |  | 


#### delete_disk_image_v3_projects_project_id_nodes_node_id_qemu_disk_image_disk_name_delete.ApiResponseFor422
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

# **delete_node_v3_projects_project_id_nodes_node_id_delete**
<a name="delete_node_v3_projects_project_id_nodes_node_id_delete"></a>
> delete_node_v3_projects_project_id_nodes_node_id_delete(node_idproject_id)

Delete Node

Delete a node from a project.  Required privilege: Node.Allocate

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import openapi_client
from openapi_client.apis.tags import nodes_api
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.error_message import ErrorMessage
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
    api_instance = nodes_api.NodesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'node_id': None,
        'project_id': None,
    }
    try:
        # Delete Node
        api_response = api_instance.delete_node_v3_projects_project_id_nodes_node_id_delete(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling NodesApi->delete_node_v3_projects_project_id_nodes_node_id_delete: %s\n" % e)
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
node_id | NodeIdSchema | | 
project_id | ProjectIdSchema | | 

# NodeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | value must be a uuid

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_node_v3_projects_project_id_nodes_node_id_delete.ApiResponseFor204) | Successful Response
404 | [ApiResponseFor404](#delete_node_v3_projects_project_id_nodes_node_id_delete.ApiResponseFor404) | Could not find project or node
409 | [ApiResponseFor409](#delete_node_v3_projects_project_id_nodes_node_id_delete.ApiResponseFor409) | Cannot delete node
422 | [ApiResponseFor422](#delete_node_v3_projects_project_id_nodes_node_id_delete.ApiResponseFor422) | Validation Error

#### delete_node_v3_projects_project_id_nodes_node_id_delete.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_node_v3_projects_project_id_nodes_node_id_delete.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorMessage**](../../models/ErrorMessage.md) |  | 


#### delete_node_v3_projects_project_id_nodes_node_id_delete.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorMessage**](../../models/ErrorMessage.md) |  | 


#### delete_node_v3_projects_project_id_nodes_node_id_delete.ApiResponseFor422
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

# **duplicate_node_v3_projects_project_id_nodes_node_id_duplicate_post**
<a name="duplicate_node_v3_projects_project_id_nodes_node_id_duplicate_post"></a>
> Node duplicate_node_v3_projects_project_id_nodes_node_id_duplicate_post(node_idproject_idnode_duplicate)

Duplicate Node

Duplicate a node.  Required privilege: Node.Allocate

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import openapi_client
from openapi_client.apis.tags import nodes_api
from openapi_client.model.node import Node
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.error_message import ErrorMessage
from openapi_client.model.node_duplicate import NodeDuplicate
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
    api_instance = nodes_api.NodesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'node_id': None,
        'project_id': None,
    }
    body = NodeDuplicate(None)
    try:
        # Duplicate Node
        api_response = api_instance.duplicate_node_v3_projects_project_id_nodes_node_id_duplicate_post(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NodesApi->duplicate_node_v3_projects_project_id_nodes_node_id_duplicate_post: %s\n" % e)
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
[**NodeDuplicate**](../../models/NodeDuplicate.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
node_id | NodeIdSchema | | 
project_id | ProjectIdSchema | | 

# NodeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | value must be a uuid

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#duplicate_node_v3_projects_project_id_nodes_node_id_duplicate_post.ApiResponseFor201) | Successful Response
404 | [ApiResponseFor404](#duplicate_node_v3_projects_project_id_nodes_node_id_duplicate_post.ApiResponseFor404) | Could not find project or node
422 | [ApiResponseFor422](#duplicate_node_v3_projects_project_id_nodes_node_id_duplicate_post.ApiResponseFor422) | Validation Error

#### duplicate_node_v3_projects_project_id_nodes_node_id_duplicate_post.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Node**](../../models/Node.md) |  | 


#### duplicate_node_v3_projects_project_id_nodes_node_id_duplicate_post.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorMessage**](../../models/ErrorMessage.md) |  | 


#### duplicate_node_v3_projects_project_id_nodes_node_id_duplicate_post.ApiResponseFor422
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

# **get_file_v3_projects_project_id_nodes_node_id_files_file_path_get**
<a name="get_file_v3_projects_project_id_nodes_node_id_files_file_path_get"></a>
> bool, date, datetime, dict, float, int, list, str, none_type get_file_v3_projects_project_id_nodes_node_id_files_file_path_get(file_pathnode_idproject_id)

Get File

Return a file from the node directory.  Required privilege: Node.Audit

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import openapi_client
from openapi_client.apis.tags import nodes_api
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.error_message import ErrorMessage
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
    api_instance = nodes_api.NodesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'file_path': None,
        'node_id': None,
        'project_id': None,
    }
    try:
        # Get File
        api_response = api_instance.get_file_v3_projects_project_id_nodes_node_id_files_file_path_get(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NodesApi->get_file_v3_projects_project_id_nodes_node_id_files_file_path_get: %s\n" % e)
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
file_path | FilePathSchema | | 
node_id | NodeIdSchema | | 
project_id | ProjectIdSchema | | 

# FilePathSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# NodeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | value must be a uuid

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_file_v3_projects_project_id_nodes_node_id_files_file_path_get.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#get_file_v3_projects_project_id_nodes_node_id_files_file_path_get.ApiResponseFor404) | Could not find project or node
422 | [ApiResponseFor422](#get_file_v3_projects_project_id_nodes_node_id_files_file_path_get.ApiResponseFor422) | Validation Error

#### get_file_v3_projects_project_id_nodes_node_id_files_file_path_get.ApiResponseFor200
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

#### get_file_v3_projects_project_id_nodes_node_id_files_file_path_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorMessage**](../../models/ErrorMessage.md) |  | 


#### get_file_v3_projects_project_id_nodes_node_id_files_file_path_get.ApiResponseFor422
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

# **get_node_links_v3_projects_project_id_nodes_node_id_links_get**
<a name="get_node_links_v3_projects_project_id_nodes_node_id_links_get"></a>
> bool, date, datetime, dict, float, int, list, str, none_type get_node_links_v3_projects_project_id_nodes_node_id_links_get(node_idproject_id)

Get Node Links

Return all the links connected to a node.  Required privilege: Link.Audit

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import openapi_client
from openapi_client.apis.tags import nodes_api
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.error_message import ErrorMessage
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
    api_instance = nodes_api.NodesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'node_id': None,
        'project_id': None,
    }
    try:
        # Get Node Links
        api_response = api_instance.get_node_links_v3_projects_project_id_nodes_node_id_links_get(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NodesApi->get_node_links_v3_projects_project_id_nodes_node_id_links_get: %s\n" % e)
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
node_id | NodeIdSchema | | 
project_id | ProjectIdSchema | | 

# NodeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | value must be a uuid

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_node_links_v3_projects_project_id_nodes_node_id_links_get.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#get_node_links_v3_projects_project_id_nodes_node_id_links_get.ApiResponseFor404) | Could not find project or node
422 | [ApiResponseFor422](#get_node_links_v3_projects_project_id_nodes_node_id_links_get.ApiResponseFor422) | Validation Error

#### get_node_links_v3_projects_project_id_nodes_node_id_links_get.ApiResponseFor200
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

#### get_node_links_v3_projects_project_id_nodes_node_id_links_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorMessage**](../../models/ErrorMessage.md) |  | 


#### get_node_links_v3_projects_project_id_nodes_node_id_links_get.ApiResponseFor422
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

# **get_node_v3_projects_project_id_nodes_node_id_get**
<a name="get_node_v3_projects_project_id_nodes_node_id_get"></a>
> Node get_node_v3_projects_project_id_nodes_node_id_get(node_idproject_id)

Get Node

Return a node from a given project.  Required privilege: Node.Audit

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import openapi_client
from openapi_client.apis.tags import nodes_api
from openapi_client.model.node import Node
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.error_message import ErrorMessage
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
    api_instance = nodes_api.NodesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'node_id': None,
        'project_id': None,
    }
    try:
        # Get Node
        api_response = api_instance.get_node_v3_projects_project_id_nodes_node_id_get(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NodesApi->get_node_v3_projects_project_id_nodes_node_id_get: %s\n" % e)
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
node_id | NodeIdSchema | | 
project_id | ProjectIdSchema | | 

# NodeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | value must be a uuid

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_node_v3_projects_project_id_nodes_node_id_get.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#get_node_v3_projects_project_id_nodes_node_id_get.ApiResponseFor404) | Could not find project or node
422 | [ApiResponseFor422](#get_node_v3_projects_project_id_nodes_node_id_get.ApiResponseFor422) | Validation Error

#### get_node_v3_projects_project_id_nodes_node_id_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Node**](../../models/Node.md) |  | 


#### get_node_v3_projects_project_id_nodes_node_id_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorMessage**](../../models/ErrorMessage.md) |  | 


#### get_node_v3_projects_project_id_nodes_node_id_get.ApiResponseFor422
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

# **get_nodes_v3_projects_project_id_nodes_get**
<a name="get_nodes_v3_projects_project_id_nodes_get"></a>
> bool, date, datetime, dict, float, int, list, str, none_type get_nodes_v3_projects_project_id_nodes_get(project_id)

Get Nodes

Return all nodes belonging to a given project.  Required privilege: Node.Audit

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import openapi_client
from openapi_client.apis.tags import nodes_api
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.error_message import ErrorMessage
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
    api_instance = nodes_api.NodesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'project_id': None,
    }
    try:
        # Get Nodes
        api_response = api_instance.get_nodes_v3_projects_project_id_nodes_get(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NodesApi->get_nodes_v3_projects_project_id_nodes_get: %s\n" % e)
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
project_id | ProjectIdSchema | | 

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_nodes_v3_projects_project_id_nodes_get.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#get_nodes_v3_projects_project_id_nodes_get.ApiResponseFor404) | Could not find project or node
422 | [ApiResponseFor422](#get_nodes_v3_projects_project_id_nodes_get.ApiResponseFor422) | Validation Error

#### get_nodes_v3_projects_project_id_nodes_get.ApiResponseFor200
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

#### get_nodes_v3_projects_project_id_nodes_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorMessage**](../../models/ErrorMessage.md) |  | 


#### get_nodes_v3_projects_project_id_nodes_get.ApiResponseFor422
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

# **idlepc_proposals_v3_projects_project_id_nodes_node_id_dynamips_idlepc_proposals_get**
<a name="idlepc_proposals_v3_projects_project_id_nodes_node_id_dynamips_idlepc_proposals_get"></a>
> bool, date, datetime, dict, float, int, list, str, none_type idlepc_proposals_v3_projects_project_id_nodes_node_id_dynamips_idlepc_proposals_get(node_idproject_id)

Idlepc Proposals

Compute a list of potential idle-pc values for a Dynamips node  Required privilege: Node.Audit

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import openapi_client
from openapi_client.apis.tags import nodes_api
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.error_message import ErrorMessage
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
    api_instance = nodes_api.NodesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'node_id': None,
        'project_id': None,
    }
    try:
        # Idlepc Proposals
        api_response = api_instance.idlepc_proposals_v3_projects_project_id_nodes_node_id_dynamips_idlepc_proposals_get(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NodesApi->idlepc_proposals_v3_projects_project_id_nodes_node_id_dynamips_idlepc_proposals_get: %s\n" % e)
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
node_id | NodeIdSchema | | 
project_id | ProjectIdSchema | | 

# NodeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | value must be a uuid

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#idlepc_proposals_v3_projects_project_id_nodes_node_id_dynamips_idlepc_proposals_get.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#idlepc_proposals_v3_projects_project_id_nodes_node_id_dynamips_idlepc_proposals_get.ApiResponseFor404) | Could not find project or node
422 | [ApiResponseFor422](#idlepc_proposals_v3_projects_project_id_nodes_node_id_dynamips_idlepc_proposals_get.ApiResponseFor422) | Validation Error

#### idlepc_proposals_v3_projects_project_id_nodes_node_id_dynamips_idlepc_proposals_get.ApiResponseFor200
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

#### idlepc_proposals_v3_projects_project_id_nodes_node_id_dynamips_idlepc_proposals_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorMessage**](../../models/ErrorMessage.md) |  | 


#### idlepc_proposals_v3_projects_project_id_nodes_node_id_dynamips_idlepc_proposals_get.ApiResponseFor422
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

# **isolate_node_v3_projects_project_id_nodes_node_id_isolate_post**
<a name="isolate_node_v3_projects_project_id_nodes_node_id_isolate_post"></a>
> isolate_node_v3_projects_project_id_nodes_node_id_isolate_post(node_idproject_id)

Isolate Node

Isolate a node (suspend all attached links).  Required privilege: Link.Modify

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import openapi_client
from openapi_client.apis.tags import nodes_api
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.error_message import ErrorMessage
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
    api_instance = nodes_api.NodesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'node_id': None,
        'project_id': None,
    }
    try:
        # Isolate Node
        api_response = api_instance.isolate_node_v3_projects_project_id_nodes_node_id_isolate_post(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling NodesApi->isolate_node_v3_projects_project_id_nodes_node_id_isolate_post: %s\n" % e)
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
node_id | NodeIdSchema | | 
project_id | ProjectIdSchema | | 

# NodeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | value must be a uuid

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#isolate_node_v3_projects_project_id_nodes_node_id_isolate_post.ApiResponseFor204) | Successful Response
404 | [ApiResponseFor404](#isolate_node_v3_projects_project_id_nodes_node_id_isolate_post.ApiResponseFor404) | Could not find project or node
422 | [ApiResponseFor422](#isolate_node_v3_projects_project_id_nodes_node_id_isolate_post.ApiResponseFor422) | Validation Error

#### isolate_node_v3_projects_project_id_nodes_node_id_isolate_post.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### isolate_node_v3_projects_project_id_nodes_node_id_isolate_post.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorMessage**](../../models/ErrorMessage.md) |  | 


#### isolate_node_v3_projects_project_id_nodes_node_id_isolate_post.ApiResponseFor422
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

# **post_file_v3_projects_project_id_nodes_node_id_files_file_path_post**
<a name="post_file_v3_projects_project_id_nodes_node_id_files_file_path_post"></a>
> bool, date, datetime, dict, float, int, list, str, none_type post_file_v3_projects_project_id_nodes_node_id_files_file_path_post(file_pathnode_idproject_id)

Post File

Write a file in the node directory.  Required privilege: Node.Modify

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import openapi_client
from openapi_client.apis.tags import nodes_api
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.error_message import ErrorMessage
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
    api_instance = nodes_api.NodesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'file_path': None,
        'node_id': None,
        'project_id': None,
    }
    try:
        # Post File
        api_response = api_instance.post_file_v3_projects_project_id_nodes_node_id_files_file_path_post(
            path_params=path_params,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NodesApi->post_file_v3_projects_project_id_nodes_node_id_files_file_path_post: %s\n" % e)
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
file_path | FilePathSchema | | 
node_id | NodeIdSchema | | 
project_id | ProjectIdSchema | | 

# FilePathSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# NodeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | value must be a uuid

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#post_file_v3_projects_project_id_nodes_node_id_files_file_path_post.ApiResponseFor201) | Successful Response
404 | [ApiResponseFor404](#post_file_v3_projects_project_id_nodes_node_id_files_file_path_post.ApiResponseFor404) | Could not find project or node
422 | [ApiResponseFor422](#post_file_v3_projects_project_id_nodes_node_id_files_file_path_post.ApiResponseFor422) | Validation Error

#### post_file_v3_projects_project_id_nodes_node_id_files_file_path_post.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

#### post_file_v3_projects_project_id_nodes_node_id_files_file_path_post.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorMessage**](../../models/ErrorMessage.md) |  | 


#### post_file_v3_projects_project_id_nodes_node_id_files_file_path_post.ApiResponseFor422
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

# **reload_all_nodes_v3_projects_project_id_nodes_reload_post**
<a name="reload_all_nodes_v3_projects_project_id_nodes_reload_post"></a>
> reload_all_nodes_v3_projects_project_id_nodes_reload_post(project_id)

Reload All Nodes

Reload all nodes belonging to a given project.  Required privilege: Node.PowerMgmt

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import openapi_client
from openapi_client.apis.tags import nodes_api
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.error_message import ErrorMessage
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
    api_instance = nodes_api.NodesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'project_id': None,
    }
    try:
        # Reload All Nodes
        api_response = api_instance.reload_all_nodes_v3_projects_project_id_nodes_reload_post(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling NodesApi->reload_all_nodes_v3_projects_project_id_nodes_reload_post: %s\n" % e)
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
project_id | ProjectIdSchema | | 

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#reload_all_nodes_v3_projects_project_id_nodes_reload_post.ApiResponseFor204) | Successful Response
404 | [ApiResponseFor404](#reload_all_nodes_v3_projects_project_id_nodes_reload_post.ApiResponseFor404) | Could not find project or node
422 | [ApiResponseFor422](#reload_all_nodes_v3_projects_project_id_nodes_reload_post.ApiResponseFor422) | Validation Error

#### reload_all_nodes_v3_projects_project_id_nodes_reload_post.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### reload_all_nodes_v3_projects_project_id_nodes_reload_post.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorMessage**](../../models/ErrorMessage.md) |  | 


#### reload_all_nodes_v3_projects_project_id_nodes_reload_post.ApiResponseFor422
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

# **reload_node_v3_projects_project_id_nodes_node_id_reload_post**
<a name="reload_node_v3_projects_project_id_nodes_node_id_reload_post"></a>
> reload_node_v3_projects_project_id_nodes_node_id_reload_post(node_idproject_id)

Reload Node

Reload a node.  Required privilege: Node.PowerMgmt

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import openapi_client
from openapi_client.apis.tags import nodes_api
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.error_message import ErrorMessage
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
    api_instance = nodes_api.NodesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'node_id': None,
        'project_id': None,
    }
    try:
        # Reload Node
        api_response = api_instance.reload_node_v3_projects_project_id_nodes_node_id_reload_post(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling NodesApi->reload_node_v3_projects_project_id_nodes_node_id_reload_post: %s\n" % e)
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
node_id | NodeIdSchema | | 
project_id | ProjectIdSchema | | 

# NodeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | value must be a uuid

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#reload_node_v3_projects_project_id_nodes_node_id_reload_post.ApiResponseFor204) | Successful Response
404 | [ApiResponseFor404](#reload_node_v3_projects_project_id_nodes_node_id_reload_post.ApiResponseFor404) | Could not find project or node
422 | [ApiResponseFor422](#reload_node_v3_projects_project_id_nodes_node_id_reload_post.ApiResponseFor422) | Validation Error

#### reload_node_v3_projects_project_id_nodes_node_id_reload_post.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### reload_node_v3_projects_project_id_nodes_node_id_reload_post.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorMessage**](../../models/ErrorMessage.md) |  | 


#### reload_node_v3_projects_project_id_nodes_node_id_reload_post.ApiResponseFor422
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

# **reset_console_all_nodes_v3_projects_project_id_nodes_console_reset_post**
<a name="reset_console_all_nodes_v3_projects_project_id_nodes_console_reset_post"></a>
> reset_console_all_nodes_v3_projects_project_id_nodes_console_reset_post(project_id)

Reset Console All Nodes

Reset console for all nodes belonging to the project.  Required privilege: Node.Console

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import openapi_client
from openapi_client.apis.tags import nodes_api
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.error_message import ErrorMessage
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
    api_instance = nodes_api.NodesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'project_id': None,
    }
    try:
        # Reset Console All Nodes
        api_response = api_instance.reset_console_all_nodes_v3_projects_project_id_nodes_console_reset_post(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling NodesApi->reset_console_all_nodes_v3_projects_project_id_nodes_console_reset_post: %s\n" % e)
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
project_id | ProjectIdSchema | | 

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#reset_console_all_nodes_v3_projects_project_id_nodes_console_reset_post.ApiResponseFor204) | Successful Response
404 | [ApiResponseFor404](#reset_console_all_nodes_v3_projects_project_id_nodes_console_reset_post.ApiResponseFor404) | Could not find project or node
422 | [ApiResponseFor422](#reset_console_all_nodes_v3_projects_project_id_nodes_console_reset_post.ApiResponseFor422) | Validation Error

#### reset_console_all_nodes_v3_projects_project_id_nodes_console_reset_post.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### reset_console_all_nodes_v3_projects_project_id_nodes_console_reset_post.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorMessage**](../../models/ErrorMessage.md) |  | 


#### reset_console_all_nodes_v3_projects_project_id_nodes_console_reset_post.ApiResponseFor422
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

# **start_all_nodes_v3_projects_project_id_nodes_start_post**
<a name="start_all_nodes_v3_projects_project_id_nodes_start_post"></a>
> start_all_nodes_v3_projects_project_id_nodes_start_post(project_id)

Start All Nodes

Start all nodes belonging to a given project.  Required privilege: Node.PowerMgmt

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import openapi_client
from openapi_client.apis.tags import nodes_api
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.error_message import ErrorMessage
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
    api_instance = nodes_api.NodesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'project_id': None,
    }
    try:
        # Start All Nodes
        api_response = api_instance.start_all_nodes_v3_projects_project_id_nodes_start_post(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling NodesApi->start_all_nodes_v3_projects_project_id_nodes_start_post: %s\n" % e)
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
project_id | ProjectIdSchema | | 

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#start_all_nodes_v3_projects_project_id_nodes_start_post.ApiResponseFor204) | Successful Response
404 | [ApiResponseFor404](#start_all_nodes_v3_projects_project_id_nodes_start_post.ApiResponseFor404) | Could not find project or node
422 | [ApiResponseFor422](#start_all_nodes_v3_projects_project_id_nodes_start_post.ApiResponseFor422) | Validation Error

#### start_all_nodes_v3_projects_project_id_nodes_start_post.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### start_all_nodes_v3_projects_project_id_nodes_start_post.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorMessage**](../../models/ErrorMessage.md) |  | 


#### start_all_nodes_v3_projects_project_id_nodes_start_post.ApiResponseFor422
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

# **start_node_v3_projects_project_id_nodes_node_id_start_post**
<a name="start_node_v3_projects_project_id_nodes_node_id_start_post"></a>
> start_node_v3_projects_project_id_nodes_node_id_start_post(node_idproject_idbody)

Start Node

Start a node.  Required privilege: Node.PowerMgmt

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import openapi_client
from openapi_client.apis.tags import nodes_api
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.error_message import ErrorMessage
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
    api_instance = nodes_api.NodesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'node_id': None,
        'project_id': None,
    }
    body = None
    try:
        # Start Node
        api_response = api_instance.start_node_v3_projects_project_id_nodes_node_id_start_post(
            path_params=path_params,
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling NodesApi->start_node_v3_projects_project_id_nodes_node_id_start_post: %s\n" % e)
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

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
node_id | NodeIdSchema | | 
project_id | ProjectIdSchema | | 

# NodeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | value must be a uuid

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#start_node_v3_projects_project_id_nodes_node_id_start_post.ApiResponseFor204) | Successful Response
404 | [ApiResponseFor404](#start_node_v3_projects_project_id_nodes_node_id_start_post.ApiResponseFor404) | Could not find project or node
422 | [ApiResponseFor422](#start_node_v3_projects_project_id_nodes_node_id_start_post.ApiResponseFor422) | Validation Error

#### start_node_v3_projects_project_id_nodes_node_id_start_post.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### start_node_v3_projects_project_id_nodes_node_id_start_post.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorMessage**](../../models/ErrorMessage.md) |  | 


#### start_node_v3_projects_project_id_nodes_node_id_start_post.ApiResponseFor422
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

# **stop_all_nodes_v3_projects_project_id_nodes_stop_post**
<a name="stop_all_nodes_v3_projects_project_id_nodes_stop_post"></a>
> stop_all_nodes_v3_projects_project_id_nodes_stop_post(project_id)

Stop All Nodes

Stop all nodes belonging to a given project.  Required privilege: Node.PowerMgmt

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import openapi_client
from openapi_client.apis.tags import nodes_api
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.error_message import ErrorMessage
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
    api_instance = nodes_api.NodesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'project_id': None,
    }
    try:
        # Stop All Nodes
        api_response = api_instance.stop_all_nodes_v3_projects_project_id_nodes_stop_post(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling NodesApi->stop_all_nodes_v3_projects_project_id_nodes_stop_post: %s\n" % e)
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
project_id | ProjectIdSchema | | 

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#stop_all_nodes_v3_projects_project_id_nodes_stop_post.ApiResponseFor204) | Successful Response
404 | [ApiResponseFor404](#stop_all_nodes_v3_projects_project_id_nodes_stop_post.ApiResponseFor404) | Could not find project or node
422 | [ApiResponseFor422](#stop_all_nodes_v3_projects_project_id_nodes_stop_post.ApiResponseFor422) | Validation Error

#### stop_all_nodes_v3_projects_project_id_nodes_stop_post.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### stop_all_nodes_v3_projects_project_id_nodes_stop_post.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorMessage**](../../models/ErrorMessage.md) |  | 


#### stop_all_nodes_v3_projects_project_id_nodes_stop_post.ApiResponseFor422
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

# **stop_node_v3_projects_project_id_nodes_node_id_stop_post**
<a name="stop_node_v3_projects_project_id_nodes_node_id_stop_post"></a>
> stop_node_v3_projects_project_id_nodes_node_id_stop_post(node_idproject_id)

Stop Node

Stop a node.  Required privilege: Node.PowerMgmt

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import openapi_client
from openapi_client.apis.tags import nodes_api
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.error_message import ErrorMessage
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
    api_instance = nodes_api.NodesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'node_id': None,
        'project_id': None,
    }
    try:
        # Stop Node
        api_response = api_instance.stop_node_v3_projects_project_id_nodes_node_id_stop_post(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling NodesApi->stop_node_v3_projects_project_id_nodes_node_id_stop_post: %s\n" % e)
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
node_id | NodeIdSchema | | 
project_id | ProjectIdSchema | | 

# NodeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | value must be a uuid

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#stop_node_v3_projects_project_id_nodes_node_id_stop_post.ApiResponseFor204) | Successful Response
404 | [ApiResponseFor404](#stop_node_v3_projects_project_id_nodes_node_id_stop_post.ApiResponseFor404) | Could not find project or node
422 | [ApiResponseFor422](#stop_node_v3_projects_project_id_nodes_node_id_stop_post.ApiResponseFor422) | Validation Error

#### stop_node_v3_projects_project_id_nodes_node_id_stop_post.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### stop_node_v3_projects_project_id_nodes_node_id_stop_post.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorMessage**](../../models/ErrorMessage.md) |  | 


#### stop_node_v3_projects_project_id_nodes_node_id_stop_post.ApiResponseFor422
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

# **suspend_all_nodes_v3_projects_project_id_nodes_suspend_post**
<a name="suspend_all_nodes_v3_projects_project_id_nodes_suspend_post"></a>
> suspend_all_nodes_v3_projects_project_id_nodes_suspend_post(project_id)

Suspend All Nodes

Suspend all nodes belonging to a given project.  Required privilege: Node.PowerMgmt

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import openapi_client
from openapi_client.apis.tags import nodes_api
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.error_message import ErrorMessage
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
    api_instance = nodes_api.NodesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'project_id': None,
    }
    try:
        # Suspend All Nodes
        api_response = api_instance.suspend_all_nodes_v3_projects_project_id_nodes_suspend_post(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling NodesApi->suspend_all_nodes_v3_projects_project_id_nodes_suspend_post: %s\n" % e)
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
project_id | ProjectIdSchema | | 

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#suspend_all_nodes_v3_projects_project_id_nodes_suspend_post.ApiResponseFor204) | Successful Response
404 | [ApiResponseFor404](#suspend_all_nodes_v3_projects_project_id_nodes_suspend_post.ApiResponseFor404) | Could not find project or node
422 | [ApiResponseFor422](#suspend_all_nodes_v3_projects_project_id_nodes_suspend_post.ApiResponseFor422) | Validation Error

#### suspend_all_nodes_v3_projects_project_id_nodes_suspend_post.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### suspend_all_nodes_v3_projects_project_id_nodes_suspend_post.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorMessage**](../../models/ErrorMessage.md) |  | 


#### suspend_all_nodes_v3_projects_project_id_nodes_suspend_post.ApiResponseFor422
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

# **suspend_node_v3_projects_project_id_nodes_node_id_suspend_post**
<a name="suspend_node_v3_projects_project_id_nodes_node_id_suspend_post"></a>
> suspend_node_v3_projects_project_id_nodes_node_id_suspend_post(node_idproject_id)

Suspend Node

Suspend a node.  Required privilege: Node.PowerMgmt

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import openapi_client
from openapi_client.apis.tags import nodes_api
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.error_message import ErrorMessage
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
    api_instance = nodes_api.NodesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'node_id': None,
        'project_id': None,
    }
    try:
        # Suspend Node
        api_response = api_instance.suspend_node_v3_projects_project_id_nodes_node_id_suspend_post(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling NodesApi->suspend_node_v3_projects_project_id_nodes_node_id_suspend_post: %s\n" % e)
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
node_id | NodeIdSchema | | 
project_id | ProjectIdSchema | | 

# NodeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | value must be a uuid

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#suspend_node_v3_projects_project_id_nodes_node_id_suspend_post.ApiResponseFor204) | Successful Response
404 | [ApiResponseFor404](#suspend_node_v3_projects_project_id_nodes_node_id_suspend_post.ApiResponseFor404) | Could not find project or node
422 | [ApiResponseFor422](#suspend_node_v3_projects_project_id_nodes_node_id_suspend_post.ApiResponseFor422) | Validation Error

#### suspend_node_v3_projects_project_id_nodes_node_id_suspend_post.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### suspend_node_v3_projects_project_id_nodes_node_id_suspend_post.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorMessage**](../../models/ErrorMessage.md) |  | 


#### suspend_node_v3_projects_project_id_nodes_node_id_suspend_post.ApiResponseFor422
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

# **unisolate_node_v3_projects_project_id_nodes_node_id_unisolate_post**
<a name="unisolate_node_v3_projects_project_id_nodes_node_id_unisolate_post"></a>
> unisolate_node_v3_projects_project_id_nodes_node_id_unisolate_post(node_idproject_id)

Unisolate Node

Un-isolate a node (resume all attached suspended links).  Required privilege: Link.Modify

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import openapi_client
from openapi_client.apis.tags import nodes_api
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.error_message import ErrorMessage
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
    api_instance = nodes_api.NodesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'node_id': None,
        'project_id': None,
    }
    try:
        # Unisolate Node
        api_response = api_instance.unisolate_node_v3_projects_project_id_nodes_node_id_unisolate_post(
            path_params=path_params,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling NodesApi->unisolate_node_v3_projects_project_id_nodes_node_id_unisolate_post: %s\n" % e)
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
node_id | NodeIdSchema | | 
project_id | ProjectIdSchema | | 

# NodeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | value must be a uuid

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#unisolate_node_v3_projects_project_id_nodes_node_id_unisolate_post.ApiResponseFor204) | Successful Response
404 | [ApiResponseFor404](#unisolate_node_v3_projects_project_id_nodes_node_id_unisolate_post.ApiResponseFor404) | Could not find project or node
422 | [ApiResponseFor422](#unisolate_node_v3_projects_project_id_nodes_node_id_unisolate_post.ApiResponseFor422) | Validation Error

#### unisolate_node_v3_projects_project_id_nodes_node_id_unisolate_post.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### unisolate_node_v3_projects_project_id_nodes_node_id_unisolate_post.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorMessage**](../../models/ErrorMessage.md) |  | 


#### unisolate_node_v3_projects_project_id_nodes_node_id_unisolate_post.ApiResponseFor422
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

# **update_disk_image_v3_projects_project_id_nodes_node_id_qemu_disk_image_disk_name_put**
<a name="update_disk_image_v3_projects_project_id_nodes_node_id_qemu_disk_image_disk_name_put"></a>
> update_disk_image_v3_projects_project_id_nodes_node_id_qemu_disk_image_disk_name_put(disk_namenode_idproject_idqemu_disk_image_update)

Update Disk Image

Update a Qemu disk image.  Required privilege: Node.Allocate

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import openapi_client
from openapi_client.apis.tags import nodes_api
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.error_message import ErrorMessage
from openapi_client.model.qemu_disk_image_update import QemuDiskImageUpdate
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
    api_instance = nodes_api.NodesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'disk_name': None,
        'node_id': None,
        'project_id': None,
    }
    body = QemuDiskImageUpdate(None)
    try:
        # Update Disk Image
        api_response = api_instance.update_disk_image_v3_projects_project_id_nodes_node_id_qemu_disk_image_disk_name_put(
            path_params=path_params,
            body=body,
        )
    except openapi_client.ApiException as e:
        print("Exception when calling NodesApi->update_disk_image_v3_projects_project_id_nodes_node_id_qemu_disk_image_disk_name_put: %s\n" % e)
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
[**QemuDiskImageUpdate**](../../models/QemuDiskImageUpdate.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
disk_name | DiskNameSchema | | 
node_id | NodeIdSchema | | 
project_id | ProjectIdSchema | | 

# DiskNameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

# NodeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | value must be a uuid

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#update_disk_image_v3_projects_project_id_nodes_node_id_qemu_disk_image_disk_name_put.ApiResponseFor204) | Successful Response
404 | [ApiResponseFor404](#update_disk_image_v3_projects_project_id_nodes_node_id_qemu_disk_image_disk_name_put.ApiResponseFor404) | Could not find project or node
422 | [ApiResponseFor422](#update_disk_image_v3_projects_project_id_nodes_node_id_qemu_disk_image_disk_name_put.ApiResponseFor422) | Validation Error

#### update_disk_image_v3_projects_project_id_nodes_node_id_qemu_disk_image_disk_name_put.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### update_disk_image_v3_projects_project_id_nodes_node_id_qemu_disk_image_disk_name_put.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorMessage**](../../models/ErrorMessage.md) |  | 


#### update_disk_image_v3_projects_project_id_nodes_node_id_qemu_disk_image_disk_name_put.ApiResponseFor422
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

# **update_node_v3_projects_project_id_nodes_node_id_put**
<a name="update_node_v3_projects_project_id_nodes_node_id_put"></a>
> Node update_node_v3_projects_project_id_nodes_node_id_put(node_idproject_idnode_update)

Update Node

Update a node.  Required privilege: Node.Modify

### Example

* OAuth Authentication (OAuth2PasswordBearer):
```python
import openapi_client
from openapi_client.apis.tags import nodes_api
from openapi_client.model.node import Node
from openapi_client.model.http_validation_error import HTTPValidationError
from openapi_client.model.error_message import ErrorMessage
from openapi_client.model.node_update import NodeUpdate
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
    api_instance = nodes_api.NodesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'node_id': None,
        'project_id': None,
    }
    body = NodeUpdate(None)
    try:
        # Update Node
        api_response = api_instance.update_node_v3_projects_project_id_nodes_node_id_put(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling NodesApi->update_node_v3_projects_project_id_nodes_node_id_put: %s\n" % e)
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
[**NodeUpdate**](../../models/NodeUpdate.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
node_id | NodeIdSchema | | 
project_id | ProjectIdSchema | | 

# NodeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | value must be a uuid

# ProjectIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | value must be a uuid

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_node_v3_projects_project_id_nodes_node_id_put.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#update_node_v3_projects_project_id_nodes_node_id_put.ApiResponseFor404) | Could not find project or node
422 | [ApiResponseFor422](#update_node_v3_projects_project_id_nodes_node_id_put.ApiResponseFor422) | Validation Error

#### update_node_v3_projects_project_id_nodes_node_id_put.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Node**](../../models/Node.md) |  | 


#### update_node_v3_projects_project_id_nodes_node_id_put.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorMessage**](../../models/ErrorMessage.md) |  | 


#### update_node_v3_projects_project_id_nodes_node_id_put.ApiResponseFor422
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

