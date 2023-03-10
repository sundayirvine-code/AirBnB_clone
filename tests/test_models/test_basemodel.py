#!/usr/bin/env python3
from models.base_model import BaseModel
from models.__init__ import storage
import unittest
from datetime import datetime
import time
"""Tests class BaseModel"""


class TestBaseModel(unittest.TestCase):
    def test_instance_creation(self):
        """
        Test that BaseModel creates an instance
        and that its attributes are of the correct type.
        """
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)
        self.assertIsInstance(instance.id, str)

    def test_save(self):
        """
        Tests that the save method of the BaseModel class
        updates the updated_at
        """
        instance = BaseModel()
        time.sleep(0.000000000000001)
        instance.save()
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)
        self.assertIsInstance(instance.id, str)
        self.assertNotEqual(instance.created_at, instance.updated_at)

    def test_string_representation(self):
        """
        Test the string representation of the BaseModel instance
        """
        instance = BaseModel()
        instance_string = instance.__str__()
        cls_name = instance.__class__.__name__
        test_string = f"[{cls_name}] {(instance.id)} {instance.__dict__}"
        self.assertEqual(instance_string, test_string)

    def test_dictionary_representation(self):
        """
        Tests that the to_dict method of the BaseModel class
        returns a dictionary in the expected format
        """
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertIsInstance(instance_dict, dict)
        self.assertIsInstance(instance_dict["id"], str)
        self.assertIsInstance(instance_dict["updated_at"], str)
        self.assertIsInstance(instance_dict["created_at"], str)
        self.assertEqual(instance_dict["__class__"], "BaseModel")

    def test_instance_creation_with_kwargs(self):
        """
        Test that BaseModel creates an instance with kwargs
        and that its attributes are of the correct type.
        """
        key_value = {
            'first_name': 'John',
            'last_name': 'Doe'
        }
        instance = BaseModel(**key_value)
        self.assertIsInstance(instance, BaseModel)
        self.assertIsInstance(instance.first_name, str)
        self.assertIsInstance(instance.last_name, str)
        self.assertEqual(instance.first_name, 'John')
        self.assertEqual(instance.last_name, 'Doe')

    def test_save_adds_to_storage(self):
        """
        if the save method is adding the instance to the storage object.
        """
        instance = BaseModel()
        instance.save()
        key = f"{instance.__class__.__name__}.{instance.id}"
        self.assertIn(key, storage._FileStorage__objects)
        self.assertIs(storage._FileStorage__objects[key], instance)


if __name__ == '__main__':
    unittest.main()
