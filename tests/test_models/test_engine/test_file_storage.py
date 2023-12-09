#!/usr/bin/python3
"""test file storage"""
import unittest
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class TestFileStorage(unittest.TestCase):
    """tests"""
    def setUp(self):
        """Set up for test cases."""
        self.storage = storage
        self.storage.reload()

    def tearDown(self):
        """Tear down after test cases."""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_save_and_reload(self):
        """Test if saving and reloading works correctly."""
        user = User()
        state = State()
        city = City()
        amenity = Amenity()
        place = Place()
        review = Review()

        self.storage.new(user)
        self.storage.new(state)
        self.storage.new(city)
        self.storage.new(amenity)
        self.storage.new(place)
        self.storage.new(review)

        self.storage.save()

        self.storage.__objects = {}

        self.storage.reload()

        self.assertTrue(isinstance(
            self.storage.all()["User." + user.id], User))
        self.assertTrue(isinstance(
            self.storage.all()["State." + state.id], State))
        self.assertTrue(isinstance(
            self.storage.all()["City." + city.id], City))
        self.assertTrue(isinstance(
            self.storage.all()["Amenity." + amenity.id], Amenity))
        self.assertTrue(isinstance(
            self.storage.all()["Place." + place.id], Place))
        self.assertTrue(isinstance(
            self.storage.all()["Review." + review.id], Review))

    def test_new_method(self):
        """Test if new method adds objects to the storage."""
        user = User()
        state = State()

        self.storage.new(user)
        self.storage.new(state)

        self.assertTrue(
                isinstance(self.storage.all()["User." + user.id], User))
        self.assertTrue(
                isinstance(self.storage.all()["State." + state.id], State))


if __name__ == '__main__':
    unittest.main()
