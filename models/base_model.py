"""
Defines the BaseModel class.
"""
import uuid
from datetime import datetime

class BaseModel:
    """Base Class for all other classes."""

    def __init__(self, *args, **kwargs):
        """init all new instances of this class."""

        if kwargs != {}:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)
            
        else:
            self.id = str(uuid.uuid4)
            self.created_at = datetime.now()
            self.updated_at = datetime.now()


    def save(self):
        """updates the pub instance attr updated_at with the current datetime."""
        self.updated_at = datetime.now()


    def to_dict(self):
        """returns a dictionary representation of the object."""
        d = self.__dict__
        d['__class__'] = type(self).__name__
        d['created_at'] = self.created_at.isoformat()
        d['updated_at'] = self.updated_at.isoformat()
        
        return d

        
    def __str__(self):
        """returns a string representation of an instance"""
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"
