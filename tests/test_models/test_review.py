#!/usr/bin/env python3
import unittest
from datetime import datetime
import time
from models.review import Review
from models.__init__ import storage
"""Tests for class Review"""


class TestReview(unittest.TestCase):
    def test_instance_creation(self):
        """
        Test that Review creates an instance
        and that its attributes are of the correct type.
        """
        instance = Review()
        self.assertIsInstance(instance, Review)
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.place_id, str)
        self.assertIsInstance(instance.user_id, str)
        self.assertIsInstance(instance.text, str)

    def test_save(self):
        """
        Tests that the save method of the Review class
        updates the updated_at
        """
        instance = Review()
        time.sleep(0.000000000000001)
        instance.save()
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.place_id, str)
        self.assertIsInstance(instance.user_id, str)
        self.assertIsInstance(instance.text, str)
        self.assertNotEqual(instance.created_at, instance.updated_at)

    def test_string_representation(self):
        """
        Test the string representation of the Review instance
        """
        instance = Review()
        instance_string = instance.__str__()
        cls_name = instance.__class__.__name__
        test_string = f"[{cls_name}] {(instance.id)} {instance.__dict__}"
        self.assertEqual(instance_string, test_string)

    def test_dictionary_representation(self):
        """
        Tests that the to_dict method of the Review class
        returns a dictionary in the expected format
        """
        instance = Review()
        instance_dict = instance.to_dict()
        self.assertIsInstance(instance_dict, dict)
        self.assertIsInstance(instance_dict["id"], str)
        self.assertIsInstance(instance_dict["updated_at"], str)
        self.assertIsInstance(instance_dict["created_at"], str)
        self.assertEqual(instance_dict["__class__"], "Review")

    def test_save_adds_to_storage(self):
        """
        if the save method is adding the instance to the storage object.
        """
        instance = Review()
        instance.save()
        key = f"{instance.__class__.__name__}.{instance.id}"
        self.assertIn(key, storage._FileStorage__objects)
        self.assertIs(storage._FileStorage__objects[key], instance)


if __name__ == '__main__':
    unittest.main()
