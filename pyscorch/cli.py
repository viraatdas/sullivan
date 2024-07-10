import click
from pycrate.commands import init, install, build, run

@click.group()
def cli():
    pass

cli.add_command(init.init)
cli.add_command(install.install)
cli.add_command(build.build)
cli.add_command(run.run)

if __name__ == "__main__":
    cli()
