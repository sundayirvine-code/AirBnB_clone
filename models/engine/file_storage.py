#!/usr/bin/env python3
import json
import os
"""Defines the class FileStorage"""


class FileStorage:
    """Class for serializing and deserializing objects
    to and from a JSON file.

    Attributes:
        __file_path (str): The file path where the JSON data will be stored.
        __objects (dict): A dictionary storing objects, with the keys being
            formatted as '<class_name>.<id>'.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary of objects stored in the __objects attribute.

        Returns:
            dict: The dictionary of objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """Sets the given object in the __objects dictionary.

        Args:
            obj: The object to be added to the __objects dictionary.

        Returns:
            None
        """

        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes the __objects dictionary to a JSON file.

        Returns:
            None
        """
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            objects_dict = {}
            for key, value in FileStorage.__objects.items():
                objects_dict[key] = value.to_dict()
            json.dump(objects_dict, f)

    def reload(self):
        """Deserializes the JSON file to the __objects dictionary.

           If the file doesn't exist, this method does nothing and no
           exception is raised.

        Returns:
            None
        """

        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                objects_dict = json.load(f)

                from models.base_model import BaseModel
                from models.user import User
                from models.place import Place
                from models.state import State
                from models.city import City
                from models.amenity import Amenity
                from models.review import Review

                class_map = {
                    "BaseModel": BaseModel,
                    "User": User,
                    "Place": Place,
                    "State": State,
                    "City": City,
                    "Amenity": Amenity,
                    "Review": Review
                }

                for key, value in objects_dict.items():
                    class_name = key.split(".")[0]
                    if class_name in class_map:
                        obj = class_map[class_name](**value)
                        FileStorage.__objects[key] = obj
