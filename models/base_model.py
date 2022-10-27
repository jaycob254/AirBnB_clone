#!/usr/bin/python3
import uuid
from datetime import datetime

"""BaseModel that defines all common attributes/methods"""


class BaseModel:
    """BaseModel Class Details"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Prints in the form: [<class name>] (<self.id>) <self.__dict__>"""
        tmp = '[{}] ({}) {}'
        return tmp.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time"""
        self.updated_at = datetime.now()
        return

    def to_dict(self):
        """Return a dictionary containing all keys/values of the instance"""
        new_dictionary = self.__dict__.copy()
        new_dictionary.update({'__class__': str(self.__class__.__name__)})
        new_dictionary["created_at"] = self.created_at.isoformat()
        new_dictionary["updated_at"] = self.updated_at.isoformat()
