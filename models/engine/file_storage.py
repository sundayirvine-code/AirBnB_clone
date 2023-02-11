import json
import os


class FileStorage:
    """Serializes JSON files into instances
    and deserializes instances into JSON files
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the __objects attribute"""

        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key
        <obj class name>.id"""

        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            objects_dict = {}
            for key, value in FileStorage.__objects.items():
                objects_dict[key] = value.to_dict()
            json.dump(objects_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects(only
        if the JSON file (__file_path) exists;
        otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)"""

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

