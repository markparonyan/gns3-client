import os, sys
import click

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from gns3client.client.openapi_client.apis.tags import controller_api
from gns3client.client import openapi_client



@click.command()
def _version(config):
    """
    Connect to the GNS3 server and fetch its version information.
    """
    configuration = openapi_client.Configuration(host=config.host)
    try:
        with openapi_client.ApiClient(configuration) as api_client:
            api_instance = controller_api.ControllerApi(api_client)
            api_response = api_instance.get_version_v3_version_get()
            click.echo(api_response.body.get('version'))
    except openapi_client.ApiException as e:
        click.echo(f"Exception when calling ControllerAPI->version: {e}")


@click.group()
def cli():
    """
    Commands related to the gns3client library itself.
    """
    pass


@cli.command()
def version():
    """
    Show the version of the gns3client library.
    """
    from gns3client import __version__
    click.echo(f"gns3client: {__version__}")

