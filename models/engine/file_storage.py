#!/usr/bin/python3
"""
defines the `FileStorage` class.
"""
import json

class FileStorage:
    """Class to serialize/deserialize data objects."""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns objects dictionary."""
        return FileStorage.__objects

    def new(self, obj):
        """sets in object dictionary the new obj."""
        new_obj = {
            f"{type(obj).__name__}.{obj.id}": obj,
        }
        self.all().update(new_obj)

    def save(self):
        """serializes __objects to the JSON file in the file path."""
        with open(FileStorage.__file_path, "w") as f:
            temp = self.all().copy()
            for key, obj in temp.items():
                temp[key] = obj.to_dict()

            json.dump(temp, f)
            
    def reload(self):
        """deserializes the json file to object dictionary."""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        
        clx = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review
        }
        
        try:
            with open(FileStorage.__file_path, "r") as f:
                objs = json.load(f)
                for key, dic in objs.items():
                    objs[key] = clx[dic['__class__']](**dic)

                self.all().update(objs)
                
        except FileNotFoundError:
            pass
