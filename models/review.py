#!/usr/bin/env python3
from models.base_model import BaseModel
"""Defines the class Review"""


class Review(BaseModel):
    """
    The Review class inherits from BaseModel and represents
    a review made by a user.

    Attributes:
    place_id (str): The id of the Place being reviewed.
    user_id (str): The id of the User making the review.
    text (str): The review text.
    """
    place_id = ''
    user_id = ''
    text = ''

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the Review class.

        Args:
        *args: List of arguments.
        **kwargs: Dictionary of keyword arguments.
        """
        super().__init__(*args, **kwargs)
