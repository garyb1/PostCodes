#!/usr/bin/env python3

"""
Testing was done on a random list of valid
postcodes created from http://www.ukpostcode.co.uk/random.htm

Most important functions:
    - is_postcode_valid
    - get_postcode_date

"""


import unittest
from postcode.postcode import *


class TestLibraryMethods(unittest.TestCase):

    def test_postcode_validity(self):
        self.assertTrue(is_postcode_valid("NR9 4QJ"))
        self.assertTrue(is_postcode_valid("CF83 1UQ"))
        self.assertTrue(is_postcode_valid("N1 8AL"))
        self.assertTrue(is_postcode_valid("PL4 8LL"))
        self.assertTrue(is_postcode_valid("CR0 8QD"))
        self.assertTrue(is_postcode_valid("RG27 9HW"))
        self.assertTrue(is_postcode_valid("HX30ST"))
        self.assertTrue(is_postcode_valid("EH127RJ"))

        self.assertFalse(is_postcode_valid("N29 422SJ"))
        self.assertFalse(is_postcode_valid("CFDS 1UQ"))
        self.assertFalse(is_postcode_valid("N13 8XL"))
        self.assertFalse(is_postcode_valid("PX4 8LL"))
        self.assertFalse(is_postcode_valid("CR2 2QD"))
        self.assertFalse(is_postcode_valid("RGS7 9HW"))
        self.assertFalse(is_postcode_valid("HXSW0ST"))
        self.assertFalse(is_postcode_valid("EH17RJ"))

    def test_nearby_function(self):
        self.assertTrue(get_nearest_postcodes("NR9 4QJ"))
        self.assertTrue(get_nearest_postcodes("CR0 8QD"))
        assert not get_nearest_postcodes("CFDS 1UQ")

    def test_postcode_data(self):
        # 202 response code means postcode is valid
        self.assertEqual(get_postcode_data("NR9 4QJ")["status"], 200)
        # 404 response code means postcode not found
        self.assertEqual(get_postcode_data("CFDS 4QJ")["status"], 404)

if __name__ == '__main__':
    unittest.main()
