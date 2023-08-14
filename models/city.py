#!/usr/bin/env python3
"""City class"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class representing a City."""
    state_id = ""
    name = ""
    places = []
