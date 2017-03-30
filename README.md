# PostCodes

## Description
Write a library that supports validating and formatting post codes for UK.
The details of which post codes are valid and which are the parts they consist of can be found at
https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting.

This library uses the geopy and postcodes.io API.

## Contents of Library

The postcodes library file is postcode.py
Inside the library there is a number of methods available to use.

```python

get_postcode_data(postcode, optional_arg=None):

```

The get_postcode_data function takes 2 arguments - 1 of which is optional.
Argument 1 is the postcode we would like to get data of.
The optional argument is an extra endpoint available in the postcodes api eg /validate.

```python

def is_postcode_valid(postcode):

```
This function takes in a postcode as an argument and returns true if it is a valid postcode and false if it is invalid.

```python

def get_outward_code(postcode):

```

This function takes in a postcode as an argument and returns the outward code of it.

```python

def get_inward_code(postcode):

```

This function takes in a postcode as an argument and returns the inward code of it.
Inward code is the last 3 characters of the postcode.
The inward code assists in the delivery of post within a postal district.

```python

def get_nearest_postcodes(postcode):

```

This function takes a postcode as an argument and returns a list of nearby postcodes.

```python

def show_details(postcode):

```
This function takes in a postcode as an argument and prints the following:
- Validity of Postcode
- Latitude and Longitude
- Address
- Parish
- Outward Code
- Inward Code
- A list of all nearby postcodes

## Installation

###### Clone the Repository

`git@github.com:garyb1/PostCodes.git`

###### Installing and Running

```python

   # Install pip dependencies
   pip install -r requirements.txt

   # Run Setup file
   python setup.py install

   # Run the tests.py file with the unittest module
   python -m unittest tests.py

```

## Usage

To import any function from the postcode library:

```python
from postcode.postcode import [function_name(s)]

# if file is at root directory
from postcode import [function_name(s)]

```

for example
```python
# In tests.py (at root)
from postcode.postcode import *

```
This imports all functions from our library.

Simply call these imported functions as you wish.

