# coding: utf-8

# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from gns3client.openapi_client.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from gns3client.openapi_client.model.ace import ACE
from gns3client.openapi_client.model.ace_create import ACECreate
from gns3client.openapi_client.model.ace_type import ACEType
from gns3client.openapi_client.model.ace_update import ACEUpdate
from gns3client.openapi_client.model.adapter_type import AdapterType
from gns3client.openapi_client.model.appliance import Appliance
from gns3client.openapi_client.model.appliance_image import ApplianceImage
from gns3client.openapi_client.model.appliance_version import ApplianceVersion
from gns3client.openapi_client.model.appliance_version_images import ApplianceVersionImages
from gns3client.openapi_client.model.arch import Arch
from gns3client.openapi_client.model.auto_idle_pc import AutoIdlePC
from gns3client.openapi_client.model.availability import Availability
from gns3client.openapi_client.model.body_load_project_v3_projects_load_post import BodyLoadProjectV3ProjectsLoadPost
from gns3client.openapi_client.model.boot_priority import BootPriority
from gns3client.openapi_client.model.capabilities import Capabilities
from gns3client.openapi_client.model.category_input import CategoryInput
from gns3client.openapi_client.model.chassis import Chassis
from gns3client.openapi_client.model.compression import Compression
from gns3client.openapi_client.model.compute import Compute
from gns3client.openapi_client.model.compute_create import ComputeCreate
from gns3client.openapi_client.model.compute_docker_image import ComputeDockerImage
from gns3client.openapi_client.model.compute_update import ComputeUpdate
from gns3client.openapi_client.model.compute_v_mware_vm import ComputeVMwareVM
from gns3client.openapi_client.model.compute_virtual_box_vm import ComputeVirtualBoxVM
from gns3client.openapi_client.model.console_type1 import ConsoleType1
from gns3client.openapi_client.model.console_type_input import ConsoleTypeInput
from gns3client.openapi_client.model.credentials import Credentials
from gns3client.openapi_client.model.custom_adapter import CustomAdapter
from gns3client.openapi_client.model.disk_interface import DiskInterface
from gns3client.openapi_client.model.docker import Docker
from gns3client.openapi_client.model.drawing import Drawing
from gns3client.openapi_client.model.dynamips import Dynamips
from gns3client.openapi_client.model.dynamips_slot import DynamipsSlot
from gns3client.openapi_client.model.dynamips_wic import DynamipsWic
from gns3client.openapi_client.model.engine import Engine
from gns3client.openapi_client.model.error_message import ErrorMessage
from gns3client.openapi_client.model.gns3_vm import GNS3VM
from gns3client.openapi_client.model.gns3server_schemas_common_console_type import Gns3serverSchemasCommonConsoleType
from gns3client.openapi_client.model.gns3server_schemas_controller_appliances_category import Gns3serverSchemasControllerAppliancesCategory
from gns3client.openapi_client.model.gns3server_schemas_controller_appliances_console_type import Gns3serverSchemasControllerAppliancesConsoleType
from gns3client.openapi_client.model.gns3server_schemas_controller_links_link_type import Gns3serverSchemasControllerLinksLinkType
from gns3client.openapi_client.model.gns3server_schemas_controller_nodes_link_type import Gns3serverSchemasControllerNodesLinkType
from gns3client.openapi_client.model.gns3server_schemas_controller_templates_category import Gns3serverSchemasControllerTemplatesCategory
from gns3client.openapi_client.model.http_validation_error import HTTPValidationError
from gns3client.openapi_client.model.iou_license import IOULicense
from gns3client.openapi_client.model.image import Image
from gns3client.openapi_client.model.image_type import ImageType
from gns3client.openapi_client.model.iou import Iou
from gns3client.openapi_client.model.kvm import Kvm
from gns3client.openapi_client.model.label import Label
from gns3client.openapi_client.model.link import Link
from gns3client.openapi_client.model.link_create import LinkCreate
from gns3client.openapi_client.model.link_node import LinkNode
from gns3client.openapi_client.model.link_style import LinkStyle
from gns3client.openapi_client.model.link_update import LinkUpdate
from gns3client.openapi_client.model.logged_in_user_update import LoggedInUserUpdate
from gns3client.openapi_client.model.midplane import Midplane
from gns3client.openapi_client.model.node import Node
from gns3client.openapi_client.model.node_create import NodeCreate
from gns3client.openapi_client.model.node_duplicate import NodeDuplicate
from gns3client.openapi_client.model.node_port import NodePort
from gns3client.openapi_client.model.node_status import NodeStatus
from gns3client.openapi_client.model.node_type import NodeType
from gns3client.openapi_client.model.node_update import NodeUpdate
from gns3client.openapi_client.model.npe import Npe
from gns3client.openapi_client.model.platform import Platform
from gns3client.openapi_client.model.privilege import Privilege
from gns3client.openapi_client.model.process_priority import ProcessPriority
from gns3client.openapi_client.model.project import Project
from gns3client.openapi_client.model.project_compression import ProjectCompression
from gns3client.openapi_client.model.project_create import ProjectCreate
from gns3client.openapi_client.model.project_duplicate import ProjectDuplicate
from gns3client.openapi_client.model.project_status import ProjectStatus
from gns3client.openapi_client.model.project_update import ProjectUpdate
from gns3client.openapi_client.model.protocol import Protocol
from gns3client.openapi_client.model.qemu import Qemu
from gns3client.openapi_client.model.qemu_disk_image_adapter_type import QemuDiskImageAdapterType
from gns3client.openapi_client.model.qemu_disk_image_create import QemuDiskImageCreate
from gns3client.openapi_client.model.qemu_disk_image_format import QemuDiskImageFormat
from gns3client.openapi_client.model.qemu_disk_image_on_off import QemuDiskImageOnOff
from gns3client.openapi_client.model.qemu_disk_image_preallocation import QemuDiskImagePreallocation
from gns3client.openapi_client.model.qemu_disk_image_subformat import QemuDiskImageSubformat
from gns3client.openapi_client.model.qemu_disk_image_update import QemuDiskImageUpdate
from gns3client.openapi_client.model.registry_version import RegistryVersion
from gns3client.openapi_client.model.resource import Resource
from gns3client.openapi_client.model.resource_pool import ResourcePool
from gns3client.openapi_client.model.resource_pool_create import ResourcePoolCreate
from gns3client.openapi_client.model.resource_pool_update import ResourcePoolUpdate
from gns3client.openapi_client.model.resource_type import ResourceType
from gns3client.openapi_client.model.role import Role
from gns3client.openapi_client.model.role_create import RoleCreate
from gns3client.openapi_client.model.role_update import RoleUpdate
from gns3client.openapi_client.model.snapshot import Snapshot
from gns3client.openapi_client.model.snapshot_create import SnapshotCreate
from gns3client.openapi_client.model.status import Status
from gns3client.openapi_client.model.supplier import Supplier
from gns3client.openapi_client.model.template import Template
from gns3client.openapi_client.model.template_create import TemplateCreate
from gns3client.openapi_client.model.template_update import TemplateUpdate
from gns3client.openapi_client.model.template_usage import TemplateUsage
from gns3client.openapi_client.model.token import Token
from gns3client.openapi_client.model.user import User
from gns3client.openapi_client.model.user_create import UserCreate
from gns3client.openapi_client.model.user_group import UserGroup
from gns3client.openapi_client.model.user_group_create import UserGroupCreate
from gns3client.openapi_client.model.user_group_update import UserGroupUpdate
from gns3client.openapi_client.model.user_update import UserUpdate
from gns3client.openapi_client.model.validation_error import ValidationError
from gns3client.openapi_client.model.variable import Variable
from gns3client.openapi_client.model.version import Version
from gns3client.openapi_client.model.when_exit import WhenExit
