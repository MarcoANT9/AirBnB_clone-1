#!/usr/bin/python3
""" This class serializes instances to a JSON file and deserializes Json files
    to instances.                                                           """

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """ This class handels Json files with instances, it has 2 private class
    attributes and 4 public instance methods"""

    """====================================================================="""
    """= INIT & CLASS VARIABLES ============================================"""
    """====================================================================="""

    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
    __file_path: path to the JSON file
    __objects: objects will be stored
    """
    """ Initializes the class. """
    __file_path = "file.json"
    __objects = {}

    """====================================================================="""
    """== METHODS =========================================================="""
    """====================================================================="""

    """-----------"""
    """- Public --"""
    """-----------"""
    def all(self, cls=None):
        """returns a dictionary
        Return:
             returns a dictionary of __object
        """
        if (cls is not None):
            return self.__objects

        ret = {}
        for key, value in self.__objects.items():
            if key == cls:
                ret[key] = value
        return ret

    """------------------------------------------------------"""

    def delete(self, obj=None):
        """ Deletes an object form the database. """
        if obj is not None:
            delete = 0
            for key, value in self.__objects.items():
                if obj.name == value.name:
                    delete = value.id

            obj_class_name = (obj.__class__.__name__)
            delete = obj_class_name + "." + delete
            print(delete)
            if delete != 0:
                self.__objects.pop(delete)

    """------------------------------------------------------"""

    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    """------------------------------------------------------"""

    def save(self):
        """serialize the file path to JSON file path
        """
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    """------------------------------------------------------"""

    def reload(self):
        """serialize the file path to JSON file path
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    """-----------"""
    """- Private -"""
    """-----------"""

    """-----------"""
    """-- Class --"""
    """-----------"""

    """-----------"""
    """-- Static -"""
    """-----------"""

    """====================================================================="""
    """== SETTERS & GETTERS ================================================"""
    """====================================================================="""
