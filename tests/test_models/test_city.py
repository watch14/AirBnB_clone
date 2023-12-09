#!/usr/bin/python3
"""test"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """test"""
    def setUp(self):
        """test"""
        pass

    def tearDown(self):
        """test"""
        pass

    def test_city_attributes(self):
        """test"""
        city = City()
        city.state_id = "CA"
        city.name = "San Francisco"

        self.assertEqual(city.state_id, "CA")
        self.assertEqual(city.name, "San Francisco")

    def test_city_instance_of_base_model(self):
        """test"""
        city = City()


if __name__ == '__main__':
    unittest.main()
