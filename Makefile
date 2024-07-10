# Makefile for sullivan

# Variables
PACKAGE_NAME = sullivan
VERSION = $(shell python -c "import $(PACKAGE_NAME); print($(PACKAGE_NAME).__version__)")

.PHONY: help build clean publish test install uninstall

help:
	@echo "Makefile for $(PACKAGE_NAME)"
	@echo ""
	@echo "Usage:"
	@echo "  make build      - Build the package"
	@echo "  make clean      - Clean up build artifacts"
	@echo "  make publish    - Publish the package to PyPI"
	@echo "  make test       - Run tests"
	@echo "  make install    - Install the package locally"
	@echo "  make uninstall  - Uninstall the package"

build:
	@echo "Building the package..."
	python3 -m build

clean:
	@echo "Cleaning up build artifacts..."
	rm -rf build dist *.egg-info

publish: build
	@echo "Publishing the package to PyPI..."
	python3 -m twine upload --repository pypi dist/*

test:
	@echo "Running tests..."
	pytest

install:
	@echo "Installing the package locally..."
	pip install -e .

uninstall:
	@echo "Uninstalling the package..."
	pip uninstall -y $(PACKAGE_NAME)
