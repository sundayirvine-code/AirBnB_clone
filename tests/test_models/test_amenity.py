import unittest
from datetime import datetime
import time
from models.amenity import Amenity
from models.__init__ import storage

class TestAmenity(unittest.TestCase):
    def test_instance_creation(self):
        """
        Test that Amenity creates an instance
        and that its attributes are of the correct type.
        """
        instance = Amenity()
        self.assertIsInstance(instance, Amenity)
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.name, str)

    def test_save(self):
        """
        Tests that the save method of the Amenity class
        updates the updated_at
        """
        instance = Amenity()
        time.sleep(0.000000000000001)
        instance.save()
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.name, str)
        self.assertNotEqual(instance.created_at, instance.updated_at)

    def test_string_representation(self):
        """
        Test the string representation of the Amenity instance
        """
        instance = Amenity()
        instance_string = instance.__str__()
        test_string = f"[{instance.__class__.__name__}] {(instance.id)} {instance.__dict__}"
        self.assertEqual(instance_string, test_string)

    def test_dictionary_representation(self):
        """
        Tests that the to_dict method of the Amenity class
        returns a dictionary in the expected format
        """
        instance = Amenity()
        instance_dict = instance.to_dict()
        self.assertIsInstance(instance_dict, dict)
        self.assertIsInstance(instance_dict["id"], str)
        self.assertIsInstance(instance_dict["updated_at"], str)
        self.assertIsInstance(instance_dict["created_at"], str)
        self.assertEqual(instance_dict["__class__"], "Amenity")
        
    def test_save_adds_to_storage(self):
        """
        if the save method is adding the instance to the storage object. 
        """
        instance = Amenity()
        instance.save()
        key = f"{instance.__class__.__name__}.{instance.id}"
        self.assertIn(key, storage._FileStorage__objects)
        self.assertIs(storage._FileStorage__objects[key], instance)

if __name__ == '__main__':
    unittest.main()
