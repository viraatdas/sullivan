import click
from pycrate.commands import init

@click.group()
def cli():
    pass

cli.add_command(init.init)

if __name__ == "__main__":
    cli()
