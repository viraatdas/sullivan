import os
import subprocess
import sys
import click
import toml

@click.command()
@click.argument('package_name')
@click.option('--dev', is_flag=True, help='Install as a development dependency.')
@click.option('--test', is_flag=True, help='Install as a test dependency.')
def install(package_name, dev, test):
    """Install a package and add it to sullivan.toml."""
    # Read sullivan.toml
    with open('sullivan.toml', 'r') as f:
        config = toml.load(f)
    
    # Determine the target section
    if dev:
        section = 'dev-dependencies'
    elif test:
        section = 'test-dependencies'
    else:
        section = 'dependencies'
    
    # Install the package using pip, but target a specific directory
    target_dir = os.path.join('target', 'dependencies')
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    # Install package to target directory
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--target', target_dir, package_name])
    
    # Add the package to the appropriate section in sullivan.toml
    if section not in config['tool']['sullivan']:
        config['tool']['sullivan'][section] = {}
    
    config['tool']['sullivan'][section][package_name] = get_installed_version(package_name, target_dir)
    
    with open('sullivan.toml', 'w') as f:
        toml.dump(config, f)
    
    click.echo(click.style(f"Installed {package_name} ({section})", fg="green"))

def get_installed_version(package_name, target_dir):
    """Get the version of an installed package."""
    try:
        result = subprocess.check_output([sys.executable, '-m', 'pip', 'show', '--target', target_dir, package_name])
        for line in result.decode().split('\n'):
            if line.startswith('Version:'):
                return line.split()[1]
    except subprocess.CalledProcessError:
        return 'unknown'

if __name__ == '__main__':
    install()
