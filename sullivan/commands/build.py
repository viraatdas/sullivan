import os
import subprocess
import click
import toml
import sys

from sullivan.optimization.PyPyOptimization import PyPyOptimization

@click.command()
def build():
    """
    Build the project by ensuring all dependencies are installed.
    
    Run any optimizations if needed
    """
    with open('sullivan.toml', 'r') as f:
        config = toml.load(f)
    
    target_dir = os.path.join('target', 'dependencies')
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    dependencies = config['tool']['sullivan'].get('dependencies', {})
    dev_dependencies = config['tool']['sullivan'].get('dev-dependencies', {})
    test_dependencies = config['tool']['sullivan'].get('test-dependencies', {})

    all_dependencies = {**dependencies, **dev_dependencies, **test_dependencies}

    for package_name, version in all_dependencies.items():
        install_package(package_name, version, target_dir)

    optimization_level = config['tool']['sullivan']['optimization'].get("level", "O")
    if optimization_level == "O":
        pass
    elif optimization_level == "O1": 
        # Only PyPy optimization
        pypy_optimization = PyPyOptimization("boom")
        pass
    elif optimization_level == "O2":
        # PyPy and Cython Optimization
        pass

    click.echo(click.style("Build completed. All dependencies are installed.", fg="red"))

def install_package(package_name, version, target_dir):
    """Install a specific package version to the target directory."""
    if version == "latest":
        package_str = f"{package_name}" if version != 'unknown' else package_name
    else:
      package_str = f"{package_name}=={version}" if version != 'unknown' else package_name
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--target', target_dir, package_str])
