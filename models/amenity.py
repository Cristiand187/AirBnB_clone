#!/usr/bin/python3
"""Module to define the amenity Class"""
import uuid
import datetime as dt
from models.base_model import BaseModel


class Amenity(BaseModel):
    """class that defines all common attributes/methods for other classes
    Args:
        BaseModel ([class]): [description]
    """
    def __init__(self):

        super().__init__()
        self.name = ""