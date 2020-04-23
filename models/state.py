#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
import models
from models.city import City
from sqlalchemy.orm import relationship
from os import getenv
import os


class State(BaseModel, Base):
    """This is the class for State
            Attributes:
                name: input name
    """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state',
                              cascade='all, delete-orphan')
    else:
        @property
        def cities(self):
            """Return list of City instances with state_id equal to current
               State.id
            """
            cities = models.engine.all(City)
            list_cities = []
            for key, value in cities.items():
                if self.id == value.state_id:
                    list_cities.append(value)
            return list_cities
