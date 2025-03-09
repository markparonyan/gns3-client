# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from gns3client.openapi_client.paths.v3_computes_compute_id_connect import Api

from gns3client.openapi_client.paths import PathValues

path = PathValues.V3_COMPUTES_COMPUTE_ID_CONNECT