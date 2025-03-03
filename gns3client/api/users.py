from gns3client.client import openapi_client
from gns3client.client.openapi_client.apis.tags import users_api
from gns3client.client.openapi_client.model.token import Token
from gns3client.client.openapi_client.model.http_validation_error import HTTPValidationError
from gns3client.client.openapi_client.model.credentials import Credentials
from pprint import pprint


class UsersAPI:
    def __init__(self, host):
        self.host = host

    def authenticate(self, username: str, password: str):
        """Authenticate into GNS3 server.
        """
        configuration = openapi_client.Configuration(host=self.host)
        with openapi_client.ApiClient(configuration) as api_client:
            api_instance = users_api.UsersApi(api_client)

            body = Credentials(username=username, password=password)
            try:
                api_response = api_instance.authenticate_v3_access_users_authenticate_post(body=body,)
                token = api_response.body.get("access_token")
                return token
            except openapi_client.ApiException as e:
                print("Exception when calling UsersApi->authenticate_v3_access_users_authenticate_post: %s\n" % e)


