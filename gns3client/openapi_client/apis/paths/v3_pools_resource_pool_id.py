from gns3client.openapi_client.paths.v3_pools_resource_pool_id.get import ApiForget
from gns3client.openapi_client.paths.v3_pools_resource_pool_id.put import ApiForput
from gns3client.openapi_client.paths.v3_pools_resource_pool_id.delete import ApiFordelete


class V3PoolsResourcePoolId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
