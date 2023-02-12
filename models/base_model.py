#!/usr/bin/python3
import uuid
from datetime import datetime
import models
"""Defines the class BaseModel"""


class BaseModel:
    """The parent class that defines all common attributes for other classes.

    Attributes:
        id (str): A unique identifier for the object.
        created_at (datetime): The datetime the object was created.
        updated_at (datetime): The datetime the object was last updated.

    """
    def __init__(self, *args, **kwargs):
        """Initializes the id, created_at, and updated_at attributes.

        If no kwargs are provided, the id will be set to a newly generated
        UUID, created_at will be set to the current datetime, and updated_at
        will be set to the same value as created_at. If kwargs are provided,
        the id, created_at, and updated_at attributes will be set based on
        the values passed in the kwargs.

        Args:
            *args: Variable length argument list. Not used.
            **kwargs: Arbitrary keyword arguments. Can contain values for id,
                created_at, and updated_at.

        """

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
            models.storage.new(self)

    def __str__(self):
        """Returns a string representation of the object.

        The string representation is in the format:
        `[<Class Name>] (<id>) <object dictionary>`

        Returns:
            str: The string representation of the object.

        """

        return f"[{self.__class__.__name__}] {(self.id)} {self.__dict__}"

    def save(self):
        """"Updates the updated_at attribute with the current datetime.

        Also saves the object to the storage.

        """

        now = datetime.now()
        self.updated_at = now
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the object.

        The dictionary contains key-value pairs for id, created_at,
        updated_at, and class name. The created_at and updated_at values are
        formatted as strings in the ISO format.

        Returns:
            dict: A dictionary representation of the object.

        """

        my_dict = self.__dict__.copy()
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['__class__'] = self.__class__.__name__
        return my_dict
