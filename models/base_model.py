#!/usr/bin/python3
"""
Define The class BaseModel
"""
import models
import uuid
from datetime import datetime


class BaseModel:
    """
    define the class atrribut
    """

    def __init__(self, *args, **kwargs):
        """Public instance attributes"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def __str__(self):
        """should print: [<class name>] (<self.id>) <self.__dict__>"""
        scn = self.__class__.__name__
        return "[{}] ({}) {}".format(scn, self.id, self.__dict__)

    def save(self):
        """ updates the public instance attribute
            updated_at with the current datetime """
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all
            keys/values of __dict__ of the instance """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict
