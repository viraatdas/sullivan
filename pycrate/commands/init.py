import os
import click

@click.command()
@click.argument('project_name')
def init(project_name):
    """Initialize a new Python project."""
    project_structure = {
        "pycrate.toml": f"""
[tool.pycrate]
name = "{project_name}"
version = "0.1.0"
authors = ["Your Name <you@example.com>"]
description = "A new Python project"

[tool.pycrate.dependencies]
# Regular dependencies: essential libraries for the project to run
pydantic = "latest"

[tool.pycrate.dev-dependencies]
# Development dependencies: tools needed for development (e.g., formatting, linting)
black = "latest"
flake8 = "latest"

[tool.pycrate.test-dependencies]
# Test dependencies: libraries required for testing
pytest = "latest"

[tool.pycrate.scripts]
# Entry point script for the project
main = "src/main.py"

[tool.pycrate.python]
# Python version specification: default is '>=3.6,<4.0'
# You can specify a range of versions like '>=3.6,<3.10'
# Or a specific version like '3.8'
# Or allow any version with '*'
version = "3.10"
""",
        "setup.py": f"""
from setuptools import setup, find_packages

setup(
    name='{project_name}', 
    version='0.1', 
    packages=find_packages()
)
""",
        "src/main.py": f"""# {project_name} main script

def main():
    print("Hello, PyCrate!")

if __name__ == "__main__":
    main()
""",
        "tests/test_main.py": f"""# Tests for {project_name}

def test_example():
    assert 1 + 1 == 2
""",
        "README.md": f"# {project_name}\n\nFill this with more details.",
        ".gitignore": """# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# Distribution / packaging
.Python
env/
venv/
ENV/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyCrate metadata
pycrate.egg-info/

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# PyCrate packages
target/

.DS_Store
"""
    }

    os.makedirs(project_name)
    for key, value in project_structure.items():
        if isinstance(value, dict):
            os.makedirs(os.path.join(project_name, key))
        else:
            # Ensure directory exists before creating the file
            file_path = os.path.join(project_name, key)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path, 'w') as f:
                f.write(value)

    click.echo(click.style(f"Initialized project {project_name}", fg="yellow", bold=True))

if __name__ == "__main__":
    init()
