from gns3client.openapi_client.paths.v3_templates_template_id.get import ApiForget
from gns3client.openapi_client.paths.v3_templates_template_id.put import ApiForput
from gns3client.openapi_client.paths.v3_templates_template_id.delete import ApiFordelete


class V3TemplatesTemplateId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
