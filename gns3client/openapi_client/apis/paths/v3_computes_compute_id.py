from gns3client.openapi_client.paths.v3_computes_compute_id.get import ApiForget
from gns3client.openapi_client.paths.v3_computes_compute_id.put import ApiForput
from gns3client.openapi_client.paths.v3_computes_compute_id.delete import ApiFordelete


class V3ComputesComputeId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
