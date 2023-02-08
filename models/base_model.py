#!/usr/bin/python3
import uuid
from datetime import datetime
"""The base model that defines all common attributes for other classes"""


class BaseModel:
    """The parent class that defines all common attributes for other classes"""
    def __init__(self, *args, **kwargs):
        if args:
            pass
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

    def __str__(self):
        return f"[{self.__class__.__name__}] {(self.id)} {self.__dict__}"

    def save(self):
        now = datetime.now()
        self.updated_at = now

    def to_dict(self):
        my_dict = self.__dict__.copy()
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['__class__'] = self.__class__.__name__
        return my_dict
