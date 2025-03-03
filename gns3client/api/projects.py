import os
import sys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from gns3client.client.openapi_client.apis.tags import projects_api
from gns3client.client import openapi_client


class ProjectsAPI:
    def __init__(self, host):
        self.host = host

    def get_projects(self, access_token):
        """Get all GNS3 projects.
        """
        configuration = openapi_client.Configuration(host=self.host, access_token=access_token)
        try:
            with openapi_client.ApiClient(configuration) as api_client:
                api_instance = projects_api.ProjectsApi(api_client)
                api_response = api_instance.get_projects_v3_projects_get()
                return api_response.body
        except openapi_client.ApiException as e:
            print(f"Exception when calling ProjectsApi->get_projects_v3_projects_get: {e}")


    def get_project(self, access_token: str, project_id):
            """Get GNS3 project.
            """
            configuration = openapi_client.Configuration(host=self.host, access_token=access_token)
            try:
                with openapi_client.ApiClient(configuration) as api_client:
                    api_instance = projects_api.ProjectsApi(api_client)
                    api_response = api_instance.get_project_v3_projects_project_id_get(project_id)
                    return api_response.body
            except openapi_client.ApiException as e:
                print(f"Exception when calling ProjectsApi->get_projects_v3_projects_get: {e}")




