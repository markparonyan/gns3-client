import os
import sys
import click

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

from .api.projects import ProjectsAPI
from .api.controller import ControllerAPI
from .api.users import UsersAPI


@click.group()
@click.option('--host', default="127.0.0.1:3080", show_default=True, type=str, help='GNS3 server host')
@click.pass_context
def cli(ctx, host):
    """
    GNS3 Client CLI

    Use this tool to manage GNS3 server.
    """
    ctx.obj = {}
    ctx.obj['host'] = host
    ctx.obj['access_token'] = UsersAPI(ctx.obj.get('host')).authenticate("admin", "admin")


@cli.command()
@click.pass_context
def version(ctx):
    host = ctx.obj.get('host')
    controller = ControllerAPI(host)
    click.echo(controller.get_version())


@cli.command()
@click.pass_context
def projects(ctx):
    host = ctx.obj.get('host')
    access_token = ctx.obj.get('access_token')
    project = ProjectsAPI(host)
    click.echo(project.get_projects(access_token))


@cli.command()
@click.pass_context
def project(ctx):
    host = ctx.obj.get('host')
    access_token = ctx.obj.get('access_token')
    project = ProjectsAPI(host)
    click.echo(project.get_project(access_token=access_token, project_id="adfa"))


@cli.command()
@click.pass_context
def auth(ctx):
    host = ctx.obj.get('host')
    token = UsersAPI(host)
    click.echo(token.authenticate())


# -------------------manage gns3client library------------------------

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

