#!/usr/bin/python3
"""
Base Model class.
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    Base class for all objects in the AirBnB clone project.

    Attributes:
        id (str): A unique identifier for each instance (UUID).
        created_at (datetime): The date and time when the instance was created.
        updated_at (datetime): The date and time when the
        instance was last updated.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        Args:
            *args: Variable-length argument list
            **kwargs: Keyword arguments for initializing attributes.
                - created_at (str): ISO formatted string of the creation time.
                - updated_at (str): ISO formatted string of the update time.
                - Other custom attributes.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                if key != '__class__':
                    setattr(self, key, value)
        else:
            """ Generate a unique UUID for id,
            and set created_at and updated_at
            """
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the instance.

        Returns:
            str: A formatted string containing class
            name, id, and attribute dictionary.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Updates the updated_at attribute with the current datetime.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Converts the instance to a dictionary representation.

        Returns:
            dict: A dictionary containing all attributes of the instance.
                - __class__: The class name.
                - created_at: ISO formatted string of creation time.
                - updated_at: ISO formatted string of update time.
                - Other custom attributes.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    @classmethod
    def create_from_dict(cls, data):
        """
        Creates an instance of the class using a
        dictionary representation.

        Args:
            data (dict): Dictionary containing attributes
            for the instance.

        Returns:
            cls: An instance of the class with attributes
            populated from the dictionary.
        """
        if '__class__' in data:
            class_name = data.pop('__class__')
            if 'created_at' in data:
                data['created_at'] = datetime.strptime
                (data['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            if 'updated_at' in data:
                data['updated_at'] = datetime.strptime
                (data['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            return globals()[class_name](**data)
