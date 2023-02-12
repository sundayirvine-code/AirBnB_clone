#!/usr/bin/env python3
from models.base_model import BaseModel
"""Defines the class City"""


class City(BaseModel):
    """City Class

    This class is an extension of the BaseModel class. It represents a city and
    contains information about a city such as its name and state_id.

    Attributes:
    state_id (str): The id of the state the city belongs to.
    name (str): The name of the city.
    """
    state_id = ''
    name = ''

    def __init__(self, *args, **kwargs):
        """The constructor for City class.

        This constructor creates an instance of the City class and passes any
        arguments provided to the BaseModel class.

        Args:
        *args: A list of arguments to be passed to the BaseModel class.
        **kwargs: A dictionary of arguments to be passed to the BaseModel
          class.
        """
        super().__init__(*args, **kwargs)
