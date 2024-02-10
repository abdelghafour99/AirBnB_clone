#!/usr/bin/python3
""" Define the Class User """
from models.base_model import BaseModel


class User(BaseModel):
    """ Define The class Attributes """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
