from setuptools import setup, find_packages

setup(
    name='pyscorch',
    version='0.1.0',
    author='Viraat Das',
    author_email='viraat.laldas@gmail.com',
    description='Cargo for Python - a hassle-free package manager for Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/viraatdas/pycrate',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click',
        'toml',
    ],
    entry_points='''
        [console_scripts]
        pycrate=pycrate.cli:cli
    ''',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
