#!/usr/bin/python3
"""Defines the class BaseModel"""
import uuid
from datetime import datetime


class BaseModel:
    """The parent class that defines all common attributes for other classes"""

    def __init__(self, *args, **kwargs):
        """Initializes the id, created_at, and updated_at attributes."""

        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    pass
                else:
                    if key == 'created_at' or key == 'updated_at':
                        value = \
                            datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            now = (datetime.now())
            self.created_at = now
            self.updated_at = now
            from models.__init__ import storage
            storage.new(self)

    def __str__(self):
        """Returns a string representation of the object."""

        return f"[{self.__class__.__name__}] {(self.id)} {self.__dict__}"

    def save(self):
        """Updates the updated_at attribute with the current datetime."""

        now = datetime.now()
        self.updated_at = now
        from models.__init__ import storage
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the object."""

        my_dict = self.__dict__.copy()
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['__class__'] = self.__class__.__name__
        return my_dict
