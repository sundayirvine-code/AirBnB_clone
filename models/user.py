#!/usr/bin/env python3
"""Defines the class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents a user and stores their personal details
    Class attributes:
        email (str): The user's email
        password (str): The user's password
        first_name (str): The user's first_name
        last_name (str): The user's last_name
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
