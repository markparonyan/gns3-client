import typing_extensions

from openapi_client.apis.tags import TagValues
from openapi_client.apis.tags.acl_api import ACLApi
from openapi_client.apis.tags.appliances_api import AppliancesApi
from openapi_client.apis.tags.computes_api import ComputesApi
from openapi_client.apis.tags.controller_api import ControllerApi
from openapi_client.apis.tags.drawings_api import DrawingsApi
from openapi_client.apis.tags.gns3_vm_api import GNS3VMApi
from openapi_client.apis.tags.images_api import ImagesApi
from openapi_client.apis.tags.links_api import LinksApi
from openapi_client.apis.tags.nodes_api import NodesApi
from openapi_client.apis.tags.privileges_api import PrivilegesApi
from openapi_client.apis.tags.projects_api import ProjectsApi
from openapi_client.apis.tags.resource_pools_api import ResourcePoolsApi
from openapi_client.apis.tags.roles_api import RolesApi
from openapi_client.apis.tags.snapshots_api import SnapshotsApi
from openapi_client.apis.tags.symbols_api import SymbolsApi
from openapi_client.apis.tags.templates_api import TemplatesApi
from openapi_client.apis.tags.users_api import UsersApi
from openapi_client.apis.tags.users_groups_api import UsersGroupsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ACL: ACLApi,
        TagValues.APPLIANCES: AppliancesApi,
        TagValues.COMPUTES: ComputesApi,
        TagValues.CONTROLLER: ControllerApi,
        TagValues.DRAWINGS: DrawingsApi,
        TagValues.GNS3_VM: GNS3VMApi,
        TagValues.IMAGES: ImagesApi,
        TagValues.LINKS: LinksApi,
        TagValues.NODES: NodesApi,
        TagValues.PRIVILEGES: PrivilegesApi,
        TagValues.PROJECTS: ProjectsApi,
        TagValues.RESOURCE_POOLS: ResourcePoolsApi,
        TagValues.ROLES: RolesApi,
        TagValues.SNAPSHOTS: SnapshotsApi,
        TagValues.SYMBOLS: SymbolsApi,
        TagValues.TEMPLATES: TemplatesApi,
        TagValues.USERS: UsersApi,
        TagValues.USERS_GROUPS: UsersGroupsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ACL: ACLApi,
        TagValues.APPLIANCES: AppliancesApi,
        TagValues.COMPUTES: ComputesApi,
        TagValues.CONTROLLER: ControllerApi,
        TagValues.DRAWINGS: DrawingsApi,
        TagValues.GNS3_VM: GNS3VMApi,
        TagValues.IMAGES: ImagesApi,
        TagValues.LINKS: LinksApi,
        TagValues.NODES: NodesApi,
        TagValues.PRIVILEGES: PrivilegesApi,
        TagValues.PROJECTS: ProjectsApi,
        TagValues.RESOURCE_POOLS: ResourcePoolsApi,
        TagValues.ROLES: RolesApi,
        TagValues.SNAPSHOTS: SnapshotsApi,
        TagValues.SYMBOLS: SymbolsApi,
        TagValues.TEMPLATES: TemplatesApi,
        TagValues.USERS: UsersApi,
        TagValues.USERS_GROUPS: UsersGroupsApi,
    }
)
