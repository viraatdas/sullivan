from setuptools import setup, find_packages

setup(
    name='pycrate',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'pycrate=pycrate.cli:main',
        ],
    },
    test_suite='tests',
)

