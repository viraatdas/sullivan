# pycrate
Cargo for for Python - package manager for python

Built with Haskell

## Features
- [ ] **Initialize Projects**: Create a new Python project with a standard structure.
- [ ] **Install Packages**: Install Python packages and manage dependencies.
- [ ] **Configure Repository**: Set and configure package repositories.
- [ ] **Run Projects**: Run Python projects with a simple command.
- [ ] **Run Tests**: Run tests for your Python project.
- [ ] **Generate Documentation**: Generate documentation for your Python project.

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
└── src/
    └── main.py
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
