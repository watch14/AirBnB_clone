#!/usr/bin/python3
"""test"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """test"""
    def setUp(self):
        """test"""
        pass

    def tearDown(self):
        """test"""
        pass

    def test_state_attributes(self):
        """test"""
        state = State()
        state.name = "California"

        self.assertEqual(state.name, "California")

    def test_state_instance_of_base_model(self):
        """test"""
        state = State()


if __name__ == '__main__':
    unittest.main()
