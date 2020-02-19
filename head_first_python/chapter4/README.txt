## Create a module (vlsearch.py)
Insert here the logic of the module
	
# How to create a dist
## Create a distribution description(file setup.py)

from setuptools import setup

setup(
    name='vlsearch',
    version='1.0',
    description='Hf Python Chapter 4',
    author='HF Python 2e',
    author_email='hfpy2e@gmail.com',
    url='headfirstlabs.com',
    py_modules='vsearch'
)

## Generate a distribution file(vsearch.py, setup.py, and README.txt)
`python setup.py bdist_wheel`

##Install the distribution file
`pip install vvsearch-1.0-py3-none-any.whl`