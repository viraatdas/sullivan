import os
import subprocess
import click
import toml
import sys
from pycrate.commands.build import build

@click.command()
def run():
    """Run the main script of the project."""
    # Build the project to ensure dependencies are installed
    build.callback()

    with open('pycrate.toml', 'r') as f:
        config = toml.load(f)
    
    main_script = config['tool']['pycrate']['scripts'].get('main')
    
    if not main_script or not os.path.exists(main_script):
        click.echo(click.style("Error: Main script not found.", fg="red"))
        return
    
    # Run the main script with the appropriate PYTHONPATH
    target_dir = os.path.join('target', 'dependencies')
    env = os.environ.copy()
    env['PYTHONPATH'] = f"{target_dir}{os.pathsep}{env.get('PYTHONPATH', '')}"
    subprocess.check_call([sys.executable, main_script], env=env)
