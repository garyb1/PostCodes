
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='Postcodes',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='1.0.0',

    description='library that supports validating and formatting post codes for UK.',
    long_description='Write a library that supports validating and formatting post codes for UK.\
      The details of which post codes are valid and which are the parts they consist of can be found at \
      https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting.',

    # The project's main homepage.
    url='https://github.com/garyb1/PostCodes',

    # Author details
    author='Gary Byrne',
    author_email='garyb1@live.ie',

    # Choose your license
    license='MIT',
    py_modules=['postcode/postcode'],
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    # What does your project relate to?
    keywords='UK Postcodes',
    install_requires=['geopy==1.11.0', 'requests==2.13.0'],
)