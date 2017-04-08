#!/usr/bin/env python3

"""

Write a library that supports validating and formatting post codes for UK.
The details of which post codes are valid
and which are the parts they consist of can be found
at https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom.
The API that this library provides is your choice.

Author:  Gary Byrne
Created: 31/03/2017
GIT:     http://github.com/garyb1/PostCodes

Documentation for Postcodes API is available at http://postcodes.io/

"""

import json
import requests
import sys
import re
from geopy.geocoders import Nominatim


def get_postcode_data(postcode, optional_arg=None):
    """
        Uses requests to retrieve data from postcode api.
    """
    try:
        if not optional_arg:
            url = requests.get('https://api.postcodes.io/postcodes/' +
                               postcode)
        else:
            url = requests.get('https://api.postcodes.io/postcodes/' +
                               postcode + optional_arg)
        postcode_data = json.loads(url.text)
        return postcode_data
    except requests.exceptions.RequestException as e:
        print(e)
        sys.exit(1)


def get_outward_code(postcode):
    if is_postcode_valid(postcode):
        postcode_data = get_postcode_data(postcode)
        outcode = postcode_data["result"]["outcode"]
        return outcode


def get_inward_code(postcode):
    if is_postcode_valid(postcode):
        postcode_data = get_postcode_data(postcode)
        incode = postcode_data["result"]["incode"]
        return incode


def is_postcode_valid(postcode):
    """
        Uses regular expressions to test the pattern of the postcode.
        Test inward and outward code seperately

        Followed postcode format from www.mrs.org.uk/pdf/postcodeformat.pdf
    """
    inward_code = postcode.split(" ")[1]
    outward_code = postcode.split(" ")[0]

    if re.match("^[0-9][ABD-HJLNP-UW-Z]{2}$", inward_code) is None:
        return False
    if re.match("^[A-PR-UWYZ]{1}(([0-9]{1,2}|[0-9][A-HJKS-UW])|\
([A-HK-Y]{1}([0-9]{1,2}|[0-9][A-Z])))$", outward_code) is None:
        return False
    return True


def get_nearest_postcodes(postcode):
    postcodes = []
    postcode_data = get_postcode_data(postcode, '/nearest')
    if postcode_data["status"] == 200:
        for postcode in postcode_data["result"]:
            postcodes.append(postcode["postcode"])
    return postcodes


def show_details(postcode):
    """ The postcodes api provides latitude and longitude coordinates.
        I use these with the geopy api to retrieve
        address data of these coordinates.
        Geopy can be found here: https://github.com/geopy/geopy
    """
    if is_postcode_valid(postcode):
        postcode_data = get_postcode_data(postcode)
        result = postcode_data["result"]
        geolocator = Nominatim()
        location = geolocator.reverse(str(result["latitude"]) +
                                      "," + str(result["longitude"]))
        nearby = get_nearest_postcodes(postcode)
        coordinates = "Longitude: {} \nLatitude: {}\n"\
            .format(str(result["longitude"]), str(result["latitude"]))
        print("Valid Postcode: {}".format(str(is_postcode_valid(postcode))))
        print("Outward Code: {}".format(get_outward_code(postcode)))
        print("Inward Code: {}".format(get_inward_code(postcode)))
        print("\nAddress: \n{}".format(location.address))
        print("\nParish: {}\n".format(result["parish"]))
        print(coordinates)
        print("Nearby Postcodes: ")
        for postcode in nearby:
            print("- {}".format(postcode))


def print_postcode_details(postcode):
    print("\n\nShowing details for postcode " + postcode.upper())
    show_details(postcode)
