#!/usr/bin/env python3
from models.base_model import BaseModel
"""Defines the class Place"""


class Place(BaseModel):
    """The Place class extends the BaseModel class, and represents a place
       that a user can rent out.

    Attributes:
        city_id (str): A string representing the id of the city the
        place is located in.
        user_id (str): A string representing the id of the user who
        is the owner of the place.
        name (str): A string representing the name of the place.
        description (str): A string representing the description of the place.
        number_rooms (int): An integer representing the number of rooms
        in the place.
        number_bathrooms (int): An integer representing the number of
        bathrooms in the place.
        max_guest (int): An integer representing the maximum number of
        guests that can stay in the place.
        price_by_night (int): An integer representing the price per night
        for renting the place.
        latitude (float): A float representing the latitude coordinate of
        the place.
        longitude (float): A float representing the longitude coordinate of
        the place.
        amenity_ids (list): A list of strings representing the ids of the
        amenities the place has.
    """
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        """The constructor for the Place class. It calls the superclass
           constructor to properly initialize the object.
        Args:
            *args: The variable length arguments passed to the constructor.
            **kwargs: The keyword arguments passed to the constructor.
        """
        super().__init__(*args, **kwargs)
