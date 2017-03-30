"""
Write a library that supports validating and formatting post codes for UK.
The details of which post codes are valid and which are the parts they consist of can be
found at https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Formatting.
The API that this library provides is your choice.

Author:  Gary Byrne
Created: 29/03/2017
GIT:     http://github.com/garyb1/PostCodes

Documentation for Postcodes API is available at http://postcodes.io/

Methods:
    print_postcode_details:
        Shows the following:
            - Validity of Postcode
            - Latitude and Longitude
            - Address
            - Parish
            - Outward Code
            - Inward Code
            - A list of all nearby postcodes

    is_postcode_valid:
        Returns a boolean if the postcode is valid or invalid.

Test a random list of valid postcodes created from http://www.ukpostcode.co.uk/random.htm
"""

from postcode import print_postcode_details, is_postcode_valid

def main():

    # TRUE
    print("The following should print True\n")
    print(is_postcode_valid("NR9 4QJ"))
    print(is_postcode_valid("N13 6DZ"))
    print(is_postcode_valid("CF83 1UQ"))
    print(is_postcode_valid("N1 8AL"))
    print(is_postcode_valid("PL4 8LL"))
    print(is_postcode_valid("CR0 8QD"))
    print(is_postcode_valid("RG27 9HW"))
    print(is_postcode_valid("HX30ST"))
    print(is_postcode_valid("EH127RJ"))

    # FALSE
    print("\nThe following should print False\n")
    print(is_postcode_valid("N9 4QJ"))
    print(is_postcode_valid("N3 6DZ"))
    print(is_postcode_valid("C83 1UQ"))
    print(is_postcode_valid("N22 8AL"))
    print(is_postcode_valid("PL22 8LL"))
    print(is_postcode_valid("CLO 8QD"))
    print(is_postcode_valid("R27 9HW"))
    print(is_postcode_valid("HX23DST"))
    print(is_postcode_valid("EH007RJ"))

    #PRINT DETAILS
    print_postcode_details("CR0 8QD")
    print_postcode_details("RG27 9HW")
    print_postcode_details("HX30ST")
    print_postcode_details("EH127RJ")


if __name__ == "__main__":
    main()