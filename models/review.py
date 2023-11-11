#!/usr/bin/python3
"""
defines the Review Model.
"""
from models.base_model import BaseModel

class Review(BaseModel):
    """The review class to manage reviews."""

    place_id = ""
    user_id = ""
    text = ""
