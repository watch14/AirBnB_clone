#!/usr/bin/python3
"""test"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_default_name(self):
        """Test if the default 'name' attribute is an empty string."""
        amenity_instance = Amenity()
        self.assertEqual(amenity_instance.name, "")

    def test_setting_name(self):
        """Test if the 'name' attribute can be set correctly."""
        amenity_instance = Amenity()
        amenity_instance.name = "Swimming Pool"
        self.assertEqual(amenity_instance.name, "Swimming Pool")

    def test_inheritance(self):
        """Test if Amenity class inherits from BaseModel."""
        amenity_instance = Amenity()


if __name__ == '__main__':
    unittest.main()
