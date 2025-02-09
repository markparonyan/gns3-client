# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from openapi_client.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    ACL = "ACL"
    APPLIANCES = "Appliances"
    COMPUTES = "Computes"
    CONTROLLER = "Controller"
    DRAWINGS = "Drawings"
    GNS3_VM = "GNS3 VM"
    IMAGES = "Images"
    LINKS = "Links"
    NODES = "Nodes"
    PRIVILEGES = "Privileges"
    PROJECTS = "Projects"
    RESOURCE_POOLS = "Resource pools"
    ROLES = "Roles"
    SNAPSHOTS = "Snapshots"
    SYMBOLS = "Symbols"
    TEMPLATES = "Templates"
    USERS = "Users"
    USERS_GROUPS = "Users groups"
