import unittest
from datetime import datetime
import time
from models.user import User
from models.__init__ import storage

class TestUser(unittest.TestCase):
    def test_instance_creation(self):
        """
        Test that User creates an instance
        and that its attributes are of the correct type.
        """       
        instance = User()
        self.assertIsInstance(instance, User)
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.email, str)
        self.assertIsInstance(instance.password, str)
        self.assertIsInstance(instance.first_name, str)
        self.assertIsInstance(instance.last_name, str)

    def test_save(self):
        """
        Tests that the save method of the User class
        updates the updated_at
        """
        instance = User()
        time.sleep(0.000000000000001)
        instance.save()
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.email, str)
        self.assertIsInstance(instance.password, str)
        self.assertIsInstance(instance.first_name, str)
        self.assertIsInstance(instance.last_name, str)
        self.assertNotEqual(instance.created_at, instance.updated_at)

    def test_string_representation(self):
        """
        Test the string representation of the User instance
        """
        instance = User()
        instance_string = instance.__str__()
        test_string = f"[{instance.__class__.__name__}] {(instance.id)} {instance.__dict__}"
        self.assertEqual(instance_string, test_string)

    def test_dictionary_representation(self):
        """
        Tests that the to_dict method of the User class
        returns a dictionary in the expected format
        """
        instance = User()
        instance_dict = instance.to_dict()
        self.assertIsInstance(instance_dict, dict)
        self.assertIsInstance(instance_dict["id"], str)
        self.assertIsInstance(instance_dict["updated_at"], str)
        self.assertIsInstance(instance_dict["created_at"], str)
        self.assertEqual(instance_dict["__class__"], "User")

    def test_instance_creation_with_kwargs(self):
        """
        Test that User creates an instance with kwargs
        and that its attributes are of the correct type.
        """
        key_value = {
            'email': 'johndoe@example.com',
            'password': 'password123',
            'first_name': 'John',
            'last_name': 'Doe'
        }
        instance = User(**key_value) 
        self.assertIsInstance(instance, User)
        self.assertIsInstance(instance.email, str)
        self.assertIsInstance(instance.password, str)
        self.assertIsInstance(instance.first_name, str)
        self.assertIsInstance(instance.last_name, str)
        self.assertEqual(instance.email, 'johndoe@example.com')
        self.assertEqual(instance.password, 'password123')
        self.assertEqual(instance.first_name, 'John')
        self.assertEqual(instance.last_name, 'Doe')

    def test_save_adds_to_storage(self):
        """
        if the save method is adding the instance to the storage object. 
        """
        instance = User()
        instance.save()
        key = f"{instance.__class__.__name__}.{instance.id}"
        self.assertIn(key, storage._FileStorage__objects)
        self.assertIsInstance(storage._FileStorage__objects[key], User)
        self.assertIs(storage._FileStorage__objects[key], instance)

if __name__ == '__main__':
    unittest.main()