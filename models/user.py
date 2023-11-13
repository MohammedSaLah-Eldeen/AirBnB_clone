#!/usr/bin/python3
"""
defines the User Model.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """The user class to manage users."""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
