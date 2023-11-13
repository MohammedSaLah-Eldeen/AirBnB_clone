#!/usr/bin/python3
"""
defines the City Model.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """The city class to manage cities."""

    state_id = ""
    name = ""
