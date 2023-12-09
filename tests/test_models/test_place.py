#!/usr/bin/python3
"""Test"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test"""
    def test_default_values(self):
        """Test"""
        place_instance = Place()
        self.assertEqual(place_instance.city_id, "")
        self.assertEqual(place_instance.user_id, "")
        self.assertEqual(place_instance.name, "")
        self.assertEqual(place_instance.description, "")
        self.assertEqual(place_instance.number_rooms, 0)
        self.assertEqual(place_instance.number_bathrooms, 0)
        self.assertEqual(place_instance.max_guest, 0)
        self.assertEqual(place_instance.price_by_night, 0)
        self.assertEqual(place_instance.latitude, 0.0)
        self.assertEqual(place_instance.longitude, 0.0)
        self.assertEqual(place_instance.amenity_ids, [])

    def test_setting_attributes(self):
        """Test"""
        place_instance = Place()
        place_instance.city_id = "city123"
        place_instance.user_id = "user123"
        place_instance.name = "Cozy Cottage"
        place_instance.description = "A charming place to stay."
        place_instance.number_rooms = 2
        place_instance.number_bathrooms = 1
        place_instance.max_guest = 4
        place_instance.price_by_night = 100
        place_instance.latitude = 37.7749
        place_instance.longitude = -122.4194
        place_instance.amenity_ids = ["amenity1", "amenity2"]

        self.assertEqual(place_instance.city_id, "city123")
        self.assertEqual(place_instance.user_id, "user123")
        self.assertEqual(place_instance.name, "Cozy Cottage")
        self.assertEqual(
                place_instance.description, "A charming place to stay.")
        self.assertEqual(place_instance.number_rooms, 2)
        self.assertEqual(place_instance.number_bathrooms, 1)
        self.assertEqual(place_instance.max_guest, 4)
        self.assertEqual(place_instance.price_by_night, 100)
        self.assertEqual(place_instance.latitude, 37.7749)
        self.assertEqual(place_instance.longitude, -122.4194)
        self.assertEqual(place_instance.amenity_ids, ["amenity1", "amenity2"])

    def test_inheritance(self):
        """Test"""
        place_instance = Place()


if __name__ == '__main__':
    unittest.main()
