import os
import click

@click.command()
@click.argument('project_name')
def init(project_name):
    """Initialize a new Python project."""
    project_structure = {
        "pycrate.toml": "[tool.pycrate]\n",
        "setup.py": "from setuptools import setup, find_packages\n\nsetup(name='{}', version='0.1', packages=find_packages())\n".format(project_name),
        "src": {},
        "tests": {}
    }

    os.makedirs(project_name)
    for key, value in project_structure.items():
        if isinstance(value, dict):
            os.makedirs(os.path.join(project_name, key))
        else:
            with open(os.path.join(project_name, key), 'w') as f:
                f.write(value)

    click.echo(f"Initialized project {project_name}")

