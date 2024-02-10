#!/usr/bin/python3
"""Define the Class Review """
from models.base_model import BaseModel


class Review(BaseModel):
    """Define The class Attributes """

    place_id = ""
    user_id = ""
    text = ""
