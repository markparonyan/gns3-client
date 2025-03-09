import typing_extensions

from gns3client.openapi_client.paths import PathValues
from gns3client.openapi_client.apis.paths.v3_version import V3Version
from gns3client.openapi_client.apis.paths.v3_reload import V3Reload
from gns3client.openapi_client.apis.paths.v3_shutdown import V3Shutdown
from gns3client.openapi_client.apis.paths.v3_iou_license import V3IouLicense
from gns3client.openapi_client.apis.paths.v3_statistics import V3Statistics
from gns3client.openapi_client.apis.paths.v3_notifications import V3Notifications
from gns3client.openapi_client.apis.paths.v3_access_users_login import V3AccessUsersLogin
from gns3client.openapi_client.apis.paths.v3_access_users_authenticate import V3AccessUsersAuthenticate
from gns3client.openapi_client.apis.paths.v3_access_users_me import V3AccessUsersMe
from gns3client.openapi_client.apis.paths.v3_access_users import V3AccessUsers
from gns3client.openapi_client.apis.paths.v3_access_users_user_id import V3AccessUsersUserId
from gns3client.openapi_client.apis.paths.v3_access_users_user_id_groups import V3AccessUsersUserIdGroups
from gns3client.openapi_client.apis.paths.v3_access_groups import V3AccessGroups
from gns3client.openapi_client.apis.paths.v3_access_groups_user_group_id import V3AccessGroupsUserGroupId
from gns3client.openapi_client.apis.paths.v3_access_groups_user_group_id_members import V3AccessGroupsUserGroupIdMembers
from gns3client.openapi_client.apis.paths.v3_access_groups_user_group_id_members_user_id import V3AccessGroupsUserGroupIdMembersUserId
from gns3client.openapi_client.apis.paths.v3_access_roles import V3AccessRoles
from gns3client.openapi_client.apis.paths.v3_access_roles_role_id import V3AccessRolesRoleId
from gns3client.openapi_client.apis.paths.v3_access_roles_role_id_privileges import V3AccessRolesRoleIdPrivileges
from gns3client.openapi_client.apis.paths.v3_access_roles_role_id_privileges_privilege_id import V3AccessRolesRoleIdPrivilegesPrivilegeId
from gns3client.openapi_client.apis.paths.v3_access_privileges import V3AccessPrivileges
from gns3client.openapi_client.apis.paths.v3_access_acl_endpoints import V3AccessAclEndpoints
from gns3client.openapi_client.apis.paths.v3_access_acl import V3AccessAcl
from gns3client.openapi_client.apis.paths.v3_access_acl_ace_id import V3AccessAclAceId
from gns3client.openapi_client.apis.paths.v3_images_qemu_image_path import V3ImagesQemuImagePath
from gns3client.openapi_client.apis.paths.v3_images import V3Images
from gns3client.openapi_client.apis.paths.v3_images_upload_image_path import V3ImagesUploadImagePath
from gns3client.openapi_client.apis.paths.v3_images_prune import V3ImagesPrune
from gns3client.openapi_client.apis.paths.v3_images_install import V3ImagesInstall
from gns3client.openapi_client.apis.paths.v3_images_image_path import V3ImagesImagePath
from gns3client.openapi_client.apis.paths.v3_templates import V3Templates
from gns3client.openapi_client.apis.paths.v3_templates_template_id import V3TemplatesTemplateId
from gns3client.openapi_client.apis.paths.v3_templates_template_id_duplicate import V3TemplatesTemplateIdDuplicate
from gns3client.openapi_client.apis.paths.v3_projects import V3Projects
from gns3client.openapi_client.apis.paths.v3_projects_project_id import V3ProjectsProjectId
from gns3client.openapi_client.apis.paths.v3_projects_project_id_stats import V3ProjectsProjectIdStats
from gns3client.openapi_client.apis.paths.v3_projects_project_id_close import V3ProjectsProjectIdClose
from gns3client.openapi_client.apis.paths.v3_projects_project_id_open import V3ProjectsProjectIdOpen
from gns3client.openapi_client.apis.paths.v3_projects_load import V3ProjectsLoad
from gns3client.openapi_client.apis.paths.v3_projects_project_id_notifications import V3ProjectsProjectIdNotifications
from gns3client.openapi_client.apis.paths.v3_projects_project_id_export import V3ProjectsProjectIdExport
from gns3client.openapi_client.apis.paths.v3_projects_project_id_import import V3ProjectsProjectIdImport
from gns3client.openapi_client.apis.paths.v3_projects_project_id_duplicate import V3ProjectsProjectIdDuplicate
from gns3client.openapi_client.apis.paths.v3_projects_project_id_locked import V3ProjectsProjectIdLocked
from gns3client.openapi_client.apis.paths.v3_projects_project_id_lock import V3ProjectsProjectIdLock
from gns3client.openapi_client.apis.paths.v3_projects_project_id_unlock import V3ProjectsProjectIdUnlock
from gns3client.openapi_client.apis.paths.v3_projects_project_id_files_file_path import V3ProjectsProjectIdFilesFilePath
from gns3client.openapi_client.apis.paths.v3_projects_project_id_templates_template_id import V3ProjectsProjectIdTemplatesTemplateId
from gns3client.openapi_client.apis.paths.v3_projects_project_id_nodes import V3ProjectsProjectIdNodes
from gns3client.openapi_client.apis.paths.v3_projects_project_id_nodes_start import V3ProjectsProjectIdNodesStart
from gns3client.openapi_client.apis.paths.v3_projects_project_id_nodes_stop import V3ProjectsProjectIdNodesStop
from gns3client.openapi_client.apis.paths.v3_projects_project_id_nodes_suspend import V3ProjectsProjectIdNodesSuspend
from gns3client.openapi_client.apis.paths.v3_projects_project_id_nodes_reload import V3ProjectsProjectIdNodesReload
from gns3client.openapi_client.apis.paths.v3_projects_project_id_nodes_node_id import V3ProjectsProjectIdNodesNodeId
from gns3client.openapi_client.apis.paths.v3_projects_project_id_nodes_node_id_duplicate import V3ProjectsProjectIdNodesNodeIdDuplicate
from gns3client.openapi_client.apis.paths.v3_projects_project_id_nodes_node_id_start import V3ProjectsProjectIdNodesNodeIdStart
from gns3client.openapi_client.apis.paths.v3_projects_project_id_nodes_node_id_stop import V3ProjectsProjectIdNodesNodeIdStop
from gns3client.openapi_client.apis.paths.v3_projects_project_id_nodes_node_id_suspend import V3ProjectsProjectIdNodesNodeIdSuspend
from gns3client.openapi_client.apis.paths.v3_projects_project_id_nodes_node_id_reload import V3ProjectsProjectIdNodesNodeIdReload
from gns3client.openapi_client.apis.paths.v3_projects_project_id_nodes_node_id_isolate import V3ProjectsProjectIdNodesNodeIdIsolate
from gns3client.openapi_client.apis.paths.v3_projects_project_id_nodes_node_id_unisolate import V3ProjectsProjectIdNodesNodeIdUnisolate
from gns3client.openapi_client.apis.paths.v3_projects_project_id_nodes_node_id_links import V3ProjectsProjectIdNodesNodeIdLinks
from gns3client.openapi_client.apis.paths.v3_projects_project_id_nodes_node_id_dynamips_auto_idlepc import V3ProjectsProjectIdNodesNodeIdDynamipsAutoIdlepc
from gns3client.openapi_client.apis.paths.v3_projects_project_id_nodes_node_id_dynamips_idlepc_proposals import V3ProjectsProjectIdNodesNodeIdDynamipsIdlepcProposals
from gns3client.openapi_client.apis.paths.v3_projects_project_id_nodes_node_id_qemu_disk_image_disk_name import V3ProjectsProjectIdNodesNodeIdQemuDiskImageDiskName
from gns3client.openapi_client.apis.paths.v3_projects_project_id_nodes_node_id_files_file_path import V3ProjectsProjectIdNodesNodeIdFilesFilePath
from gns3client.openapi_client.apis.paths.v3_projects_project_id_nodes_console_reset import V3ProjectsProjectIdNodesConsoleReset
from gns3client.openapi_client.apis.paths.v3_projects_project_id_nodes_node_id_console_reset import V3ProjectsProjectIdNodesNodeIdConsoleReset
from gns3client.openapi_client.apis.paths.v3_projects_project_id_links import V3ProjectsProjectIdLinks
from gns3client.openapi_client.apis.paths.v3_projects_project_id_links_link_id_available_filters import V3ProjectsProjectIdLinksLinkIdAvailableFilters
from gns3client.openapi_client.apis.paths.v3_projects_project_id_links_link_id import V3ProjectsProjectIdLinksLinkId
from gns3client.openapi_client.apis.paths.v3_projects_project_id_links_link_id_reset import V3ProjectsProjectIdLinksLinkIdReset
from gns3client.openapi_client.apis.paths.v3_projects_project_id_links_link_id_capture_start import V3ProjectsProjectIdLinksLinkIdCaptureStart
from gns3client.openapi_client.apis.paths.v3_projects_project_id_links_link_id_capture_stop import V3ProjectsProjectIdLinksLinkIdCaptureStop
from gns3client.openapi_client.apis.paths.v3_projects_project_id_links_link_id_capture_stream import V3ProjectsProjectIdLinksLinkIdCaptureStream
from gns3client.openapi_client.apis.paths.v3_projects_project_id_drawings import V3ProjectsProjectIdDrawings
from gns3client.openapi_client.apis.paths.v3_projects_project_id_drawings_drawing_id import V3ProjectsProjectIdDrawingsDrawingId
from gns3client.openapi_client.apis.paths.v3_symbols import V3Symbols
from gns3client.openapi_client.apis.paths.v3_symbols_symbol_id_raw import V3SymbolsSymbolIdRaw
from gns3client.openapi_client.apis.paths.v3_symbols_symbol_id_dimensions import V3SymbolsSymbolIdDimensions
from gns3client.openapi_client.apis.paths.v3_symbols_default_symbols import V3SymbolsDefaultSymbols
from gns3client.openapi_client.apis.paths.v3_projects_project_id_snapshots import V3ProjectsProjectIdSnapshots
from gns3client.openapi_client.apis.paths.v3_projects_project_id_snapshots_snapshot_id import V3ProjectsProjectIdSnapshotsSnapshotId
from gns3client.openapi_client.apis.paths.v3_projects_project_id_snapshots_snapshot_id_restore import V3ProjectsProjectIdSnapshotsSnapshotIdRestore
from gns3client.openapi_client.apis.paths.v3_computes import V3Computes
from gns3client.openapi_client.apis.paths.v3_computes_compute_id_connect import V3ComputesComputeIdConnect
from gns3client.openapi_client.apis.paths.v3_computes_compute_id import V3ComputesComputeId
from gns3client.openapi_client.apis.paths.v3_computes_compute_id_docker_images import V3ComputesComputeIdDockerImages
from gns3client.openapi_client.apis.paths.v3_computes_compute_id_virtualbox_vms import V3ComputesComputeIdVirtualboxVms
from gns3client.openapi_client.apis.paths.v3_computes_compute_id_vmware_vms import V3ComputesComputeIdVmwareVms
from gns3client.openapi_client.apis.paths.v3_computes_compute_id_dynamips_auto_idlepc import V3ComputesComputeIdDynamipsAutoIdlepc
from gns3client.openapi_client.apis.paths.v3_computes_compute_id_emulator_endpoint_path import V3ComputesComputeIdEmulatorEndpointPath
from gns3client.openapi_client.apis.paths.v3_appliances import V3Appliances
from gns3client.openapi_client.apis.paths.v3_appliances_appliance_id import V3AppliancesApplianceId
from gns3client.openapi_client.apis.paths.v3_appliances_appliance_id_version import V3AppliancesApplianceIdVersion
from gns3client.openapi_client.apis.paths.v3_appliances_appliance_id_install import V3AppliancesApplianceIdInstall
from gns3client.openapi_client.apis.paths.v3_pools import V3Pools
from gns3client.openapi_client.apis.paths.v3_pools_resource_pool_id import V3PoolsResourcePoolId
from gns3client.openapi_client.apis.paths.v3_pools_resource_pool_id_resources import V3PoolsResourcePoolIdResources
from gns3client.openapi_client.apis.paths.v3_pools_resource_pool_id_resources_resource_id import V3PoolsResourcePoolIdResourcesResourceId
from gns3client.openapi_client.apis.paths.v3_gns3vm_engines import V3Gns3vmEngines
from gns3client.openapi_client.apis.paths.v3_gns3vm_engines_engine_vms import V3Gns3vmEnginesEngineVms
from gns3client.openapi_client.apis.paths.v3_gns3vm import V3Gns3vm

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.V3_VERSION: V3Version,
        PathValues.V3_RELOAD: V3Reload,
        PathValues.V3_SHUTDOWN: V3Shutdown,
        PathValues.V3_IOU_LICENSE: V3IouLicense,
        PathValues.V3_STATISTICS: V3Statistics,
        PathValues.V3_NOTIFICATIONS: V3Notifications,
        PathValues.V3_ACCESS_USERS_LOGIN: V3AccessUsersLogin,
        PathValues.V3_ACCESS_USERS_AUTHENTICATE: V3AccessUsersAuthenticate,
        PathValues.V3_ACCESS_USERS_ME: V3AccessUsersMe,
        PathValues.V3_ACCESS_USERS: V3AccessUsers,
        PathValues.V3_ACCESS_USERS_USER_ID: V3AccessUsersUserId,
        PathValues.V3_ACCESS_USERS_USER_ID_GROUPS: V3AccessUsersUserIdGroups,
        PathValues.V3_ACCESS_GROUPS: V3AccessGroups,
        PathValues.V3_ACCESS_GROUPS_USER_GROUP_ID: V3AccessGroupsUserGroupId,
        PathValues.V3_ACCESS_GROUPS_USER_GROUP_ID_MEMBERS: V3AccessGroupsUserGroupIdMembers,
        PathValues.V3_ACCESS_GROUPS_USER_GROUP_ID_MEMBERS_USER_ID: V3AccessGroupsUserGroupIdMembersUserId,
        PathValues.V3_ACCESS_ROLES: V3AccessRoles,
        PathValues.V3_ACCESS_ROLES_ROLE_ID: V3AccessRolesRoleId,
        PathValues.V3_ACCESS_ROLES_ROLE_ID_PRIVILEGES: V3AccessRolesRoleIdPrivileges,
        PathValues.V3_ACCESS_ROLES_ROLE_ID_PRIVILEGES_PRIVILEGE_ID: V3AccessRolesRoleIdPrivilegesPrivilegeId,
        PathValues.V3_ACCESS_PRIVILEGES: V3AccessPrivileges,
        PathValues.V3_ACCESS_ACL_ENDPOINTS: V3AccessAclEndpoints,
        PathValues.V3_ACCESS_ACL: V3AccessAcl,
        PathValues.V3_ACCESS_ACL_ACE_ID: V3AccessAclAceId,
        PathValues.V3_IMAGES_QEMU_IMAGE_PATH: V3ImagesQemuImagePath,
        PathValues.V3_IMAGES: V3Images,
        PathValues.V3_IMAGES_UPLOAD_IMAGE_PATH: V3ImagesUploadImagePath,
        PathValues.V3_IMAGES_PRUNE: V3ImagesPrune,
        PathValues.V3_IMAGES_INSTALL: V3ImagesInstall,
        PathValues.V3_IMAGES_IMAGE_PATH: V3ImagesImagePath,
        PathValues.V3_TEMPLATES: V3Templates,
        PathValues.V3_TEMPLATES_TEMPLATE_ID: V3TemplatesTemplateId,
        PathValues.V3_TEMPLATES_TEMPLATE_ID_DUPLICATE: V3TemplatesTemplateIdDuplicate,
        PathValues.V3_PROJECTS: V3Projects,
        PathValues.V3_PROJECTS_PROJECT_ID: V3ProjectsProjectId,
        PathValues.V3_PROJECTS_PROJECT_ID_STATS: V3ProjectsProjectIdStats,
        PathValues.V3_PROJECTS_PROJECT_ID_CLOSE: V3ProjectsProjectIdClose,
        PathValues.V3_PROJECTS_PROJECT_ID_OPEN: V3ProjectsProjectIdOpen,
        PathValues.V3_PROJECTS_LOAD: V3ProjectsLoad,
        PathValues.V3_PROJECTS_PROJECT_ID_NOTIFICATIONS: V3ProjectsProjectIdNotifications,
        PathValues.V3_PROJECTS_PROJECT_ID_EXPORT: V3ProjectsProjectIdExport,
        PathValues.V3_PROJECTS_PROJECT_ID_IMPORT: V3ProjectsProjectIdImport,
        PathValues.V3_PROJECTS_PROJECT_ID_DUPLICATE: V3ProjectsProjectIdDuplicate,
        PathValues.V3_PROJECTS_PROJECT_ID_LOCKED: V3ProjectsProjectIdLocked,
        PathValues.V3_PROJECTS_PROJECT_ID_LOCK: V3ProjectsProjectIdLock,
        PathValues.V3_PROJECTS_PROJECT_ID_UNLOCK: V3ProjectsProjectIdUnlock,
        PathValues.V3_PROJECTS_PROJECT_ID_FILES_FILE_PATH: V3ProjectsProjectIdFilesFilePath,
        PathValues.V3_PROJECTS_PROJECT_ID_TEMPLATES_TEMPLATE_ID: V3ProjectsProjectIdTemplatesTemplateId,
        PathValues.V3_PROJECTS_PROJECT_ID_NODES: V3ProjectsProjectIdNodes,
        PathValues.V3_PROJECTS_PROJECT_ID_NODES_START: V3ProjectsProjectIdNodesStart,
        PathValues.V3_PROJECTS_PROJECT_ID_NODES_STOP: V3ProjectsProjectIdNodesStop,
        PathValues.V3_PROJECTS_PROJECT_ID_NODES_SUSPEND: V3ProjectsProjectIdNodesSuspend,
        PathValues.V3_PROJECTS_PROJECT_ID_NODES_RELOAD: V3ProjectsProjectIdNodesReload,
        PathValues.V3_PROJECTS_PROJECT_ID_NODES_NODE_ID: V3ProjectsProjectIdNodesNodeId,
        PathValues.V3_PROJECTS_PROJECT_ID_NODES_NODE_ID_DUPLICATE: V3ProjectsProjectIdNodesNodeIdDuplicate,
        PathValues.V3_PROJECTS_PROJECT_ID_NODES_NODE_ID_START: V3ProjectsProjectIdNodesNodeIdStart,
        PathValues.V3_PROJECTS_PROJECT_ID_NODES_NODE_ID_STOP: V3ProjectsProjectIdNodesNodeIdStop,
        PathValues.V3_PROJECTS_PROJECT_ID_NODES_NODE_ID_SUSPEND: V3ProjectsProjectIdNodesNodeIdSuspend,
        PathValues.V3_PROJECTS_PROJECT_ID_NODES_NODE_ID_RELOAD: V3ProjectsProjectIdNodesNodeIdReload,
        PathValues.V3_PROJECTS_PROJECT_ID_NODES_NODE_ID_ISOLATE: V3ProjectsProjectIdNodesNodeIdIsolate,
        PathValues.V3_PROJECTS_PROJECT_ID_NODES_NODE_ID_UNISOLATE: V3ProjectsProjectIdNodesNodeIdUnisolate,
        PathValues.V3_PROJECTS_PROJECT_ID_NODES_NODE_ID_LINKS: V3ProjectsProjectIdNodesNodeIdLinks,
        PathValues.V3_PROJECTS_PROJECT_ID_NODES_NODE_ID_DYNAMIPS_AUTO_IDLEPC: V3ProjectsProjectIdNodesNodeIdDynamipsAutoIdlepc,
        PathValues.V3_PROJECTS_PROJECT_ID_NODES_NODE_ID_DYNAMIPS_IDLEPC_PROPOSALS: V3ProjectsProjectIdNodesNodeIdDynamipsIdlepcProposals,
        PathValues.V3_PROJECTS_PROJECT_ID_NODES_NODE_ID_QEMU_DISK_IMAGE_DISK_NAME: V3ProjectsProjectIdNodesNodeIdQemuDiskImageDiskName,
        PathValues.V3_PROJECTS_PROJECT_ID_NODES_NODE_ID_FILES_FILE_PATH: V3ProjectsProjectIdNodesNodeIdFilesFilePath,
        PathValues.V3_PROJECTS_PROJECT_ID_NODES_CONSOLE_RESET: V3ProjectsProjectIdNodesConsoleReset,
        PathValues.V3_PROJECTS_PROJECT_ID_NODES_NODE_ID_CONSOLE_RESET: V3ProjectsProjectIdNodesNodeIdConsoleReset,
        PathValues.V3_PROJECTS_PROJECT_ID_LINKS: V3ProjectsProjectIdLinks,
        PathValues.V3_PROJECTS_PROJECT_ID_LINKS_LINK_ID_AVAILABLE_FILTERS: V3ProjectsProjectIdLinksLinkIdAvailableFilters,
        PathValues.V3_PROJECTS_PROJECT_ID_LINKS_LINK_ID: V3ProjectsProjectIdLinksLinkId,
        PathValues.V3_PROJECTS_PROJECT_ID_LINKS_LINK_ID_RESET: V3ProjectsProjectIdLinksLinkIdReset,
        PathValues.V3_PROJECTS_PROJECT_ID_LINKS_LINK_ID_CAPTURE_START: V3ProjectsProjectIdLinksLinkIdCaptureStart,
        PathValues.V3_PROJECTS_PROJECT_ID_LINKS_LINK_ID_CAPTURE_STOP: V3ProjectsProjectIdLinksLinkIdCaptureStop,
        PathValues.V3_PROJECTS_PROJECT_ID_LINKS_LINK_ID_CAPTURE_STREAM: V3ProjectsProjectIdLinksLinkIdCaptureStream,
        PathValues.V3_PROJECTS_PROJECT_ID_DRAWINGS: V3ProjectsProjectIdDrawings,
        PathValues.V3_PROJECTS_PROJECT_ID_DRAWINGS_DRAWING_ID: V3ProjectsProjectIdDrawingsDrawingId,
        PathValues.V3_SYMBOLS: V3Symbols,
        PathValues.V3_SYMBOLS_SYMBOL_ID_RAW: V3SymbolsSymbolIdRaw,
        PathValues.V3_SYMBOLS_SYMBOL_ID_DIMENSIONS: V3SymbolsSymbolIdDimensions,
        PathValues.V3_SYMBOLS_DEFAULT_SYMBOLS: V3SymbolsDefaultSymbols,
        PathValues.V3_PROJECTS_PROJECT_ID_SNAPSHOTS: V3ProjectsProjectIdSnapshots,
        PathValues.V3_PROJECTS_PROJECT_ID_SNAPSHOTS_SNAPSHOT_ID: V3ProjectsProjectIdSnapshotsSnapshotId,
        PathValues.V3_PROJECTS_PROJECT_ID_SNAPSHOTS_SNAPSHOT_ID_RESTORE: V3ProjectsProjectIdSnapshotsSnapshotIdRestore,
        PathValues.V3_COMPUTES: V3Computes,
        PathValues.V3_COMPUTES_COMPUTE_ID_CONNECT: V3ComputesComputeIdConnect,
        PathValues.V3_COMPUTES_COMPUTE_ID: V3ComputesComputeId,
        PathValues.V3_COMPUTES_COMPUTE_ID_DOCKER_IMAGES: V3ComputesComputeIdDockerImages,
        PathValues.V3_COMPUTES_COMPUTE_ID_VIRTUALBOX_VMS: V3ComputesComputeIdVirtualboxVms,
        PathValues.V3_COMPUTES_COMPUTE_ID_VMWARE_VMS: V3ComputesComputeIdVmwareVms,
        PathValues.V3_COMPUTES_COMPUTE_ID_DYNAMIPS_AUTO_IDLEPC: V3ComputesComputeIdDynamipsAutoIdlepc,
        PathValues.V3_COMPUTES_COMPUTE_ID_EMULATOR_ENDPOINT_PATH: V3ComputesComputeIdEmulatorEndpointPath,
        PathValues.V3_APPLIANCES: V3Appliances,
        PathValues.V3_APPLIANCES_APPLIANCE_ID: V3AppliancesApplianceId,
        PathValues.V3_APPLIANCES_APPLIANCE_ID_VERSION: V3AppliancesApplianceIdVersion,
        PathValues.V3_APPLIANCES_APPLIANCE_ID_INSTALL: V3AppliancesApplianceIdInstall,
        PathValues.V3_POOLS: V3Pools,
        PathValues.V3_POOLS_RESOURCE_POOL_ID: V3PoolsResourcePoolId,
        PathValues.V3_POOLS_RESOURCE_POOL_ID_RESOURCES: V3PoolsResourcePoolIdResources,
        PathValues.V3_POOLS_RESOURCE_POOL_ID_RESOURCES_RESOURCE_ID: V3PoolsResourcePoolIdResourcesResourceId,
        PathValues.V3_GNS3VM_ENGINES: V3Gns3vmEngines,
        PathValues.V3_GNS3VM_ENGINES_ENGINE_VMS: V3Gns3vmEnginesEngineVms,
        PathValues.V3_GNS3VM: V3Gns3vm,
    }
)

path_to_api = PathToApi(
    {
        PathValues.V3_VERSION: V3Version,
        PathValues.V3_RELOAD: V3Reload,
        PathValues.V3_SHUTDOWN: V3Shutdown,
        PathValues.V3_IOU_LICENSE: V3IouLicense,
        PathValues.V3_STATISTICS: V3Statistics,
        PathValues.V3_NOTIFICATIONS: V3Notifications,
        PathValues.V3_ACCESS_USERS_LOGIN: V3AccessUsersLogin,
        PathValues.V3_ACCESS_USERS_AUTHENTICATE: V3AccessUsersAuthenticate,
        PathValues.V3_ACCESS_USERS_ME: V3AccessUsersMe,
        PathValues.V3_ACCESS_USERS: V3AccessUsers,
        PathValues.V3_ACCESS_USERS_USER_ID: V3AccessUsersUserId,
        PathValues.V3_ACCESS_USERS_USER_ID_GROUPS: V3AccessUsersUserIdGroups,
        PathValues.V3_ACCESS_GROUPS: V3AccessGroups,
        PathValues.V3_ACCESS_GROUPS_USER_GROUP_ID: V3AccessGroupsUserGroupId,
        PathValues.V3_ACCESS_GROUPS_USER_GROUP_ID_MEMBERS: V3AccessGroupsUserGroupIdMembers,
        PathValues.V3_ACCESS_GROUPS_USER_GROUP_ID_MEMBERS_USER_ID: V3AccessGroupsUserGroupIdMembersUserId,
        PathValues.V3_ACCESS_ROLES: V3AccessRoles,
        PathValues.V3_ACCESS_ROLES_ROLE_ID: V3AccessRolesRoleId,
        PathValues.V3_ACCESS_ROLES_ROLE_ID_PRIVILEGES: V3AccessRolesRoleIdPrivileges,
        PathValues.V3_ACCESS_ROLES_ROLE_ID_PRIVILEGES_PRIVILEGE_ID: V3AccessRolesRoleIdPrivilegesPrivilegeId,
        PathValues.V3_ACCESS_PRIVILEGES: V3AccessPrivileges,
        PathValues.V3_ACCESS_ACL_ENDPOINTS: V3AccessAclEndpoints,
        PathValues.V3_ACCESS_ACL: V3AccessAcl,
        PathValues.V3_ACCESS_ACL_ACE_ID: V3AccessAclAceId,
        PathValues.V3_IMAGES_QEMU_IMAGE_PATH: V3ImagesQemuImagePath,
        PathValues.V3_IMAGES: V3Images,
        PathValues.V3_IMAGES_UPLOAD_IMAGE_PATH: V3ImagesUploadImagePath,
        PathValues.V3_IMAGES_PRUNE: V3ImagesPrune,
        PathValues.V3_IMAGES_INSTALL: V3ImagesInstall,
        PathValues.V3_IMAGES_IMAGE_PATH: V3ImagesImagePath,
        PathValues.V3_TEMPLATES: V3Templates,
        PathValues.V3_TEMPLATES_TEMPLATE_ID: V3TemplatesTemplateId,
        PathValues.V3_TEMPLATES_TEMPLATE_ID_DUPLICATE: V3TemplatesTemplateIdDuplicate,
        PathValues.V3_PROJECTS: V3Projects,
        PathValues.V3_PROJECTS_PROJECT_ID: V3ProjectsProjectId,
        PathValues.V3_PROJECTS_PROJECT_ID_STATS: V3ProjectsProjectIdStats,
        PathValues.V3_PROJECTS_PROJECT_ID_CLOSE: V3ProjectsProjectIdClose,
        PathValues.V3_PROJECTS_PROJECT_ID_OPEN: V3ProjectsProjectIdOpen,
        PathValues.V3_PROJECTS_LOAD: V3ProjectsLoad,
        PathValues.V3_PROJECTS_PROJECT_ID_NOTIFICATIONS: V3ProjectsProjectIdNotifications,
        PathValues.V3_PROJECTS_PROJECT_ID_EXPORT: V3ProjectsProjectIdExport,
        PathValues.V3_PROJECTS_PROJECT_ID_IMPORT: V3ProjectsProjectIdImport,
        PathValues.V3_PROJECTS_PROJECT_ID_DUPLICATE: V3ProjectsProjectIdDuplicate,
        PathValues.V3_PROJECTS_PROJECT_ID_LOCKED: V3ProjectsProjectIdLocked,
        PathValues.V3_PROJECTS_PROJECT_ID_LOCK: V3ProjectsProjectIdLock,
        PathValues.V3_PROJECTS_PROJECT_ID_UNLOCK: V3ProjectsProjectIdUnlock,
        PathValues.V3_PROJECTS_PROJECT_ID_FILES_FILE_PATH: V3ProjectsProjectIdFilesFilePath,
        PathValues.V3_PROJECTS_PROJECT_ID_TEMPLATES_TEMPLATE_ID: V3ProjectsProjectIdTemplatesTemplateId,
        PathValues.V3_PROJECTS_PROJECT_ID_NODES: V3ProjectsProjectIdNodes,
        PathValues.V3_PROJECTS_PROJECT_ID_NODES_START: V3ProjectsProjectIdNodesStart,
        PathValues.V3_PROJECTS_PROJECT_ID_NODES_STOP: V3ProjectsProjectIdNodesStop,
        PathValues.V3_PROJECTS_PROJECT_ID_NODES_SUSPEND: V3ProjectsProjectIdNodesSuspend,
        PathValues.V3_PROJECTS_PROJECT_ID_NODES_RELOAD: V3ProjectsProjectIdNodesReload,
        PathValues.V3_PROJECTS_PROJECT_ID_NODES_NODE_ID: V3ProjectsProjectIdNodesNodeId,
        PathValues.V3_PROJECTS_PROJECT_ID_NODES_NODE_ID_DUPLICATE: V3ProjectsProjectIdNodesNodeIdDuplicate,
        PathValues.V3_PROJECTS_PROJECT_ID_NODES_NODE_ID_START: V3ProjectsProjectIdNodesNodeIdStart,
        PathValues.V3_PROJECTS_PROJECT_ID_NODES_NODE_ID_STOP: V3ProjectsProjectIdNodesNodeIdStop,
        PathValues.V3_PROJECTS_PROJECT_ID_NODES_NODE_ID_SUSPEND: V3ProjectsProjectIdNodesNodeIdSuspend,
        PathValues.V3_PROJECTS_PROJECT_ID_NODES_NODE_ID_RELOAD: V3ProjectsProjectIdNodesNodeIdReload,
        PathValues.V3_PROJECTS_PROJECT_ID_NODES_NODE_ID_ISOLATE: V3ProjectsProjectIdNodesNodeIdIsolate,
        PathValues.V3_PROJECTS_PROJECT_ID_NODES_NODE_ID_UNISOLATE: V3ProjectsProjectIdNodesNodeIdUnisolate,
        PathValues.V3_PROJECTS_PROJECT_ID_NODES_NODE_ID_LINKS: V3ProjectsProjectIdNodesNodeIdLinks,
        PathValues.V3_PROJECTS_PROJECT_ID_NODES_NODE_ID_DYNAMIPS_AUTO_IDLEPC: V3ProjectsProjectIdNodesNodeIdDynamipsAutoIdlepc,
        PathValues.V3_PROJECTS_PROJECT_ID_NODES_NODE_ID_DYNAMIPS_IDLEPC_PROPOSALS: V3ProjectsProjectIdNodesNodeIdDynamipsIdlepcProposals,
        PathValues.V3_PROJECTS_PROJECT_ID_NODES_NODE_ID_QEMU_DISK_IMAGE_DISK_NAME: V3ProjectsProjectIdNodesNodeIdQemuDiskImageDiskName,
        PathValues.V3_PROJECTS_PROJECT_ID_NODES_NODE_ID_FILES_FILE_PATH: V3ProjectsProjectIdNodesNodeIdFilesFilePath,
        PathValues.V3_PROJECTS_PROJECT_ID_NODES_CONSOLE_RESET: V3ProjectsProjectIdNodesConsoleReset,
        PathValues.V3_PROJECTS_PROJECT_ID_NODES_NODE_ID_CONSOLE_RESET: V3ProjectsProjectIdNodesNodeIdConsoleReset,
        PathValues.V3_PROJECTS_PROJECT_ID_LINKS: V3ProjectsProjectIdLinks,
        PathValues.V3_PROJECTS_PROJECT_ID_LINKS_LINK_ID_AVAILABLE_FILTERS: V3ProjectsProjectIdLinksLinkIdAvailableFilters,
        PathValues.V3_PROJECTS_PROJECT_ID_LINKS_LINK_ID: V3ProjectsProjectIdLinksLinkId,
        PathValues.V3_PROJECTS_PROJECT_ID_LINKS_LINK_ID_RESET: V3ProjectsProjectIdLinksLinkIdReset,
        PathValues.V3_PROJECTS_PROJECT_ID_LINKS_LINK_ID_CAPTURE_START: V3ProjectsProjectIdLinksLinkIdCaptureStart,
        PathValues.V3_PROJECTS_PROJECT_ID_LINKS_LINK_ID_CAPTURE_STOP: V3ProjectsProjectIdLinksLinkIdCaptureStop,
        PathValues.V3_PROJECTS_PROJECT_ID_LINKS_LINK_ID_CAPTURE_STREAM: V3ProjectsProjectIdLinksLinkIdCaptureStream,
        PathValues.V3_PROJECTS_PROJECT_ID_DRAWINGS: V3ProjectsProjectIdDrawings,
        PathValues.V3_PROJECTS_PROJECT_ID_DRAWINGS_DRAWING_ID: V3ProjectsProjectIdDrawingsDrawingId,
        PathValues.V3_SYMBOLS: V3Symbols,
        PathValues.V3_SYMBOLS_SYMBOL_ID_RAW: V3SymbolsSymbolIdRaw,
        PathValues.V3_SYMBOLS_SYMBOL_ID_DIMENSIONS: V3SymbolsSymbolIdDimensions,
        PathValues.V3_SYMBOLS_DEFAULT_SYMBOLS: V3SymbolsDefaultSymbols,
        PathValues.V3_PROJECTS_PROJECT_ID_SNAPSHOTS: V3ProjectsProjectIdSnapshots,
        PathValues.V3_PROJECTS_PROJECT_ID_SNAPSHOTS_SNAPSHOT_ID: V3ProjectsProjectIdSnapshotsSnapshotId,
        PathValues.V3_PROJECTS_PROJECT_ID_SNAPSHOTS_SNAPSHOT_ID_RESTORE: V3ProjectsProjectIdSnapshotsSnapshotIdRestore,
        PathValues.V3_COMPUTES: V3Computes,
        PathValues.V3_COMPUTES_COMPUTE_ID_CONNECT: V3ComputesComputeIdConnect,
        PathValues.V3_COMPUTES_COMPUTE_ID: V3ComputesComputeId,
        PathValues.V3_COMPUTES_COMPUTE_ID_DOCKER_IMAGES: V3ComputesComputeIdDockerImages,
        PathValues.V3_COMPUTES_COMPUTE_ID_VIRTUALBOX_VMS: V3ComputesComputeIdVirtualboxVms,
        PathValues.V3_COMPUTES_COMPUTE_ID_VMWARE_VMS: V3ComputesComputeIdVmwareVms,
        PathValues.V3_COMPUTES_COMPUTE_ID_DYNAMIPS_AUTO_IDLEPC: V3ComputesComputeIdDynamipsAutoIdlepc,
        PathValues.V3_COMPUTES_COMPUTE_ID_EMULATOR_ENDPOINT_PATH: V3ComputesComputeIdEmulatorEndpointPath,
        PathValues.V3_APPLIANCES: V3Appliances,
        PathValues.V3_APPLIANCES_APPLIANCE_ID: V3AppliancesApplianceId,
        PathValues.V3_APPLIANCES_APPLIANCE_ID_VERSION: V3AppliancesApplianceIdVersion,
        PathValues.V3_APPLIANCES_APPLIANCE_ID_INSTALL: V3AppliancesApplianceIdInstall,
        PathValues.V3_POOLS: V3Pools,
        PathValues.V3_POOLS_RESOURCE_POOL_ID: V3PoolsResourcePoolId,
        PathValues.V3_POOLS_RESOURCE_POOL_ID_RESOURCES: V3PoolsResourcePoolIdResources,
        PathValues.V3_POOLS_RESOURCE_POOL_ID_RESOURCES_RESOURCE_ID: V3PoolsResourcePoolIdResourcesResourceId,
        PathValues.V3_GNS3VM_ENGINES: V3Gns3vmEngines,
        PathValues.V3_GNS3VM_ENGINES_ENGINE_VMS: V3Gns3vmEnginesEngineVms,
        PathValues.V3_GNS3VM: V3Gns3vm,
    }
)
