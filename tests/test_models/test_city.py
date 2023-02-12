#!/usr/bin/env python3
import unittest
from datetime import datetime
import time
from models.city import City
from models.__init__ import storage
"""Tests class City"""


class TestCity(unittest.TestCase):
    def test_instance_creation(self):
        """
        Test that City creates an instance
        and that its attributes are of the correct type.
        """
        instance = City()
        self.assertIsInstance(instance, City)
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.state_id, str)
        self.assertIsInstance(instance.name, str)

    def test_save(self):
        """
        Tests that the save method of the City class
        updates the updated_at
        """
        instance = City()
        time.sleep(0.000000000000001)
        instance.save()
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.state_id, str)
        self.assertIsInstance(instance.name, str)
        self.assertNotEqual(instance.created_at, instance.updated_at)

    def test_string_representation(self):
        """
        Test the string representation of the City instance
        """
        instance = City()
        instance_string = instance.__str__()
        test_string = f"[{instance.__class__.__name__}] {(instance.id)} {instance.__dict__}"
        self.assertEqual(instance_string, test_string)

    def test_dictionary_representation(self):
        """
        Tests that the to_dict method of the City class
        returns a dictionary in the expected format
        """
        instance = City()
        instance_dict = instance.to_dict()
        self.assertIsInstance(instance_dict, dict)
        self.assertIsInstance(instance_dict["id"], str)
        self.assertIsInstance(instance_dict["updated_at"], str)
        self.assertIsInstance(instance_dict["created_at"], str)
        self.assertEqual(instance_dict["__class__"], "City")

    def test_save_adds_to_storage(self):
        """
        if the save method is adding the instance to the storage object.
        """
        instance = City()
        instance.save()
        key = f"{instance.__class__.__name__}.{instance.id}"
        self.assertIn(key, storage._FileStorage__objects)
        self.assertIs(storage._FileStorage__objects[key], instance)


if __name__ == '__main__':
    unittest.main()
