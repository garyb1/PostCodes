"""

Write a library that supports validating and formatting post codes for UK.
The details of which post codes are valid and which are the parts they consist of can be
found at https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting.
The API that this library provides is your choice.

Author:  Gary Byrne
Created: 29/03/2017
GIT:     http://github.com/garyb1/PostCodes

Documentation for Postcodes API is available at http://postcodes.io/

"""

import json, requests
from geopy.geocoders import Nominatim

def get_postcode_data(postcode, optional_arg=None):
    """
        Uses requests to retrieve data from postcode api.
    """
    if not optional_arg:
        url = requests.get('https://api.postcodes.io/postcodes/' + postcode)
    else:
        url = requests.get('https://api.postcodes.io/postcodes/' + postcode + optional_arg)
    data = json.loads(url.text)
    return data

def is_postcode_valid(postcode):
    data = get_postcode_data(postcode, '/validate')
    result = data["result"]
    return result

def get_outward_code(postcode):

    """ remove whitespacing from the postcode so we
        can compare postcodes with or without it the same way.
        If postcode is 6 characters then the outward code is first 3
        else its the first 4 characters
    """
    if is_postcode_valid(postcode):
        data = get_postcode_data(postcode)
        postcode = data["result"]["postcode"].replace(" ", "")
        return postcode[0:-3]

def get_inward_code(postcode):

    """ Inward code is the last 3 characters of the postcode.
        The inward code assists in the delivery of post within a postal district.
    """
    if is_postcode_valid(postcode):
        data = get_postcode_data(postcode)
        postcode = data["result"]["postcode"]
        return postcode[-3:]

def get_nearest_postcodes(postcode):

    postcodes = []
    data = get_postcode_data(postcode, '/nearest')
    for index in range(len(data["result"])):
        postcodes.append(data["result"][index]["postcode"])
    return postcodes

def show_details(postcode):

    """ The postcodes api provides latitude and longitude coordinates.
        I use these with the geopy api to retrieve address data of these coordinates.
        Geopy can be found here: https://github.com/geopy/geopy
    """
    if is_postcode_valid(postcode):
        data = get_postcode_data(postcode)
        result = data["result"]
        latitude = result["latitude"]
        longitude = result["longitude"]
        geolocator = Nominatim()
        location = geolocator.reverse(str(latitude)+","+str(longitude))
        address = location.address
        nearby = get_nearest_postcodes(postcode)
        coordinates = "Longitude: {} \nLatitude: {}\n".format(longitude, latitude)
        print("Valid Postcode: {}".format(str(is_postcode_valid(postcode))))
        print("Outward Code: {}".format(get_outward_code(postcode)))
        print("Inward Code: {}".format(get_inward_code(postcode)))
        print("\nAddress: \n{}".format(address))
        print("\nParish: {}\n".format(result["parish"]))
        print(coordinates)
        print("Nearby Postcodes: ")
        for postcode in nearby:
            print("- {}".format(postcode))

def print_postcode_details(postcode):
    print("\n\nShowing details for postcode " + postcode.upper())
    show_details(postcode)