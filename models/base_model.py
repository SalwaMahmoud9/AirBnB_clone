#!/usr/bin/python3
"""Defines a base model class."""
import json
from uuid import uuid4
from datetime import datetime


class BaseModel(object):
    """docstring for BaseModel"""
    def __init__(self):
        """Initialize a Base.

        Args:
            id: id of the Base.
            created_at: created_at of the Base.
            updated_at: iupdated_atd of the Base.
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Return class name, id, and the dictionary"""
        return ("[{}] ({}) <{}>".format(self.__class__.__name__, self.id,
                                        self.__dict__))

    def save(self):
        """save"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return dictionary"""
        dic = self.__dict__.copy()
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        dic["__class__"] = self.__class__.__name__
        return dic
