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
        "tests": {},
        "README.md": "# {} fill this more".format(project_name),
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
""",
    }

    os.makedirs(project_name)
    for key, value in project_structure.items():
        if isinstance(value, dict):
            os.makedirs(os.path.join(project_name, key))
        else:
            with open(os.path.join(project_name, key), 'w') as f:
                f.write(value)

    click.echo(click.style(f"Initialized project {project_name}", fg="green", bold=True))
    