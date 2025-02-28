# gns3client/cli.py
import os
import sys
import click

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from gns3client.client.openapi_client.apis.tags import controller_api
from gns3client.client import openapi_client


@click.group()
def cli():
    """
    GNS3 Client CLI

    Use this tool to manage GNS3 server.
    """
    pass


@cli.command()
@click.option('--host', default="127.0.0.1:3080", show_default=True, type=str, help='GNS3 server host')
def version(host):
    """
    Get GNS3 server version.
    """
    configuration = openapi_client.Configuration(host=host)
    try:
        with openapi_client.ApiClient(configuration) as api_client:
            api_instance = controller_api.ControllerApi(api_client)
            api_response = api_instance.get_version_v3_version_get()
            click.echo(api_response.body.get('version'))
    except openapi_client.ApiException as e:
        click.echo(f"Exception when calling ControllerAPI->version: {e}")


@cli.group(name="self")
def self():
    """
    Manage the gns3client library itself.
    """
    pass


@self.command()
def version():
    """
    Show the version of the gns3client library.
    """
    from gns3client import __version__
    click.echo(f"gns3client: {__version__}")

