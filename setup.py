from setuptools import  find_packages
from distutils.core import setup 
setup(
    name = "pymy",
    version = "0.1",
    packages = find_packages(),
    # scripts = ['say_hello.py'],
    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    # install_requires = ['docutils>=0.3'],
    package_data = {
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst','*.md'],
        # And include any *.msg files found in the 'hello' package, too:
        # 'hello': ['*.msg'],
    },
    # metadata for upload to PyPI
    # author = "uzoice",
    description = "mysql quick util",
    license = "MIT",
    keywords = "mysql util quick",
    # url = "https://github.com/RocksonZeta/pymy",   # project home page, if any
    # could also include long_description, download_url, classifiers, etc.
)