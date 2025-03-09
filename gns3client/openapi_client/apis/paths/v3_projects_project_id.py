from gns3client.openapi_client.paths.v3_projects_project_id.get import ApiForget
from gns3client.openapi_client.paths.v3_projects_project_id.put import ApiForput
from gns3client.openapi_client.paths.v3_projects_project_id.delete import ApiFordelete


class V3ProjectsProjectId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
