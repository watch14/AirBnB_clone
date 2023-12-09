#!/usr/bin/python3
"""Test"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test"""
    def test_default_values(self):
        """Test"""
        review_instance = Review()
        self.assertEqual(review_instance.place_id, "")
        self.assertEqual(review_instance.user_id, "")
        self.assertEqual(review_instance.text, "")

    def test_setting_attributes(self):
        """Test"""
        review_instance = Review()
        review_instance.place_id = "12345"
        review_instance.user_id = "user123"
        review_instance.text = "A great experience!"
        self.assertEqual(review_instance.place_id, "12345")
        self.assertEqual(review_instance.user_id, "user123")
        self.assertEqual(review_instance.text, "A great experience!")

    def test_inheritance(self):
        """Test"""
        review_instance = Review()


if __name__ == '__main__':
    unittest.main()
