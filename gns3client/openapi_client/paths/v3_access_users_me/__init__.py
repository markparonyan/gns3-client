# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from gns3client.openapi_client.paths.v3_access_users_me import Api

from gns3client.openapi_client.paths import PathValues

path = PathValues.V3_ACCESS_USERS_ME