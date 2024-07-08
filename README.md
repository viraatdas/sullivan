# pycrate
Cargo for for Python - package manager for python

## Features
- [ ] **Initialize Projects**: Create a new Python project with a standard structure.
- [ ] **Install Packages**: Install Python packages and manage dependencies.
- [ ] **Configure Repository**: Set and configure package repositories.
- [ ] **Run Projects**: Run Python projects with a simple command.
- [ ] **Run Tests**: Run tests for your Python project.
- [ ] **Generate Documentation**: Generate documentation for your Python project.
- [ ] Super fast dependency management
- [ ] Better lock file management
- [ ] Easy to publish to pypi/other repositories
- [ ] Integrated testing and coverage
- [ ] Security features to identify old packages
- [ ] Easily allow you to configure Python versions (without explicitly using pyenv)

## Installation
*todo*

## Usage

### Initialize a project
```
pycrate init <project_name>
```

Ex.
```
pycrate init my_project
```

This will produce:
```
my_project/
├── pycrate.toml
├── setup.py
├── src/
│   └── main.py
├── tests/
│   └── test_main.py
├── target/
│   └── dependencies/
```

### Install a package
```
pycrate install <package_name>
```

### Configure repository 
```
pycrate configure <repository_url>
``` 

This can also be modified from the `pycrate.toml` file

### Run the project
```
pycrate run
```

### Run tests
```
pycrate test
```


### Generate documentation
```
pycrate doc
```


## Local dependency management
To mimic Cargo’s local installation approach:

- Dependencies will be installed in a target/dependencies directory within the project.
- Each project's environment will be isolated to ensure no conflicts with global Python packages.


## Notes 
- Ensure compatibility with existing tools and libraries within the Python ecosystem.
- Provide a clear and simple way to manage Python versions.
- Optimize performance for dependency resolution and installation.
