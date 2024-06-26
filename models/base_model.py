#!/usr/bin/env python3

"""
The `BaseModel` class defines a base model
with unique ID and timestamps for creation and last
update, along with methods for saving and converting to a dictionary format.
"""

from datetime import datetime
import uuid


class BaseModel:
    """BaseModel class defines a base model with unique ID and timestamps."""

    def __init__(self, *args, **kwargs):
        """Initialize object with unique ID and timestamps."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(value))
                elif key != "__class__":
                    setattr(self, key, value)

    def __str__(self):
        """Return string representation of the object."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the 'updated_at' timestamp."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Convert object to a dictionary."""
        dic = dict()
        dic["__class__"] = self.__class__.__name__
        dic["id"] = self.id
        dic["created_at"] = self.created_at.isoformat()
        dic["updated_at"] = self.updated_at.isoformat()
        for key, value in self.__dict__.items():
            if key not in ("id", "created_at", "updated_at"):
                dic[key] = value
        return dic


# Testing the BaseModel class
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
print(my_model.id)
print(my_model)
print(type(my_model.created_at))
print("--")
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))

print("--")
my_new_model = BaseModel(**my_model_json)
print(my_new_model.id)
print(my_new_model)
print(type(my_new_model.created_at))
print("--")
print(my_model is my_new_model)
    