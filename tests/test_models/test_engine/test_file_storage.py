#!/usr/bin/python3
"""test"""

import unittest
from models.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os
import json


class TestFileStorage(unittest.TestCase):
    """test"""

    def setUp(self):
        """test"""
        self.file_storage = FileStorage()

    def tearDown(self):
        """test"""
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_attributes(self):
        """test"""
        self.assertTrue(hasattr(FileStorage, '_FileStorage__file_path'))
        self.assertTrue(hasattr(FileStorage, '_FileStorage__objects'))

    def test_default_values(self):
        """test"""
        self.assertEqual(FileStorage._FileStorage__file_path, "file.json")
        self.assertEqual(FileStorage._FileStorage__objects, {})

    def test_all(self):
        """test"""
        self.assertEqual(self.file_storage.all(), {})

    def test_new(self):
        """test"""
        user = User()
        self.file_storage.new(user)
        key = "{}.{}".format(user.__class__.__name__, user.id)
        self.assertTrue(key in self.file_storage.all())

    def test_save_reload(self):
        """test"""
        user = User()
        user.email = "test@example.com"
        user.password = "password123"
        user.first_name = "John"
        user.last_name = "Doe"
        self.file_storage.new(user)
        self.file_storage.save()
        self.file_storage.reload()
        key = "{}.{}".format(user.__class__.__name__, user.id)
        reloaded_user = self.file_storage.all()[key]
        self.assertEqual(reloaded_user.email, "test@example.com")
        self.assertEqual(reloaded_user.password, "password123")
        self.assertEqual(reloaded_user.first_name, "John")
        self.assertEqual(reloaded_user.last_name, "Doe")

    def test_reload_nonexistent_file(self):
        """test"""
        self.file_storage.reload()
        self.assertEqual(self.file_storage.all(), {})

    def test_reload_empty_file(self):
        """test"""
        with open(FileStorage._FileStorage__file_path, "w") as f:
            f.write("")
        self.file_storage.reload()
        self.assertEqual(self.file_storage.all(), {})

    def test_reload_corrupted_file(self):
        """test"""
        with open(FileStorage._FileStorage__file_path, "w") as f:
            f.write("This is not a valid JSON content.")
        self.file_storage.reload()
        self.assertEqual(self.file_storage.all(), {})

    def test_reload_with_different_classes(self):
        """test"""
        user = User()
        state = State()
        self.file_storage.new(user)
        self.file_storage.new(state)
        self.file_storage.save()
        self.file_storage.reload()
        key_user = "{}.{}".format(user.__class__.__name__, user.id)
        key_state = "{}.{}".format(state.__class__.__name__, state.id)
        self.assertTrue(key_user in self.file_storage.all())
        self.assertTrue(key_state in self.file_storage.all())


if __name__ == "__main__":
    unittest.main()
