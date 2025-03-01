import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from gns3client.client.openapi_client.apis.tags import controller_api
from gns3client.client import openapi_client


class ControllerAPI:
    def __init__(self, host):
        self.host = host

    def get_version(self):
        configuration = openapi_client.Configuration(host=self.host)
        try:
            with openapi_client.ApiClient(configuration) as api_client:
                api_instance = controller_api.ControllerApi(api_client)
                api_response = api_instance.get_version_v3_version_get()
                return api_response.body.get('version')
        except openapi_client.ApiException as e:
            print(f"Exception when calling ControllerAPI->version: {e}")

