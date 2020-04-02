#!/usr/bin/python3
""" This class is the database for the AirBnB project """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from models.base_model import Basemodel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage():
    """ Storage Engine using SQLalchemy. """

    """====================================================================="""
    """= INIT & CLASS VARIABLES ============================================"""
    """====================================================================="""

    __engine = None
    __session = None

    def __init__(self):
        """ Initializes the class """
        """ Engine parameters Environment variables:
                 → User = HBNB_MYSQL_USER
                 → Password = HBNB_MYSQL_PWD
                 → Host = HBNB_MYSQL_HOST
                 → Database = HBNB_MYSQL_DB
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}:3306/{}'
                                      .format(os.getenv('HBNB_MYSQL_USER'),
                                              os.getenv('BNB_MYSQL_PWD'),
                                              os.getenv('HBNB_MYSQL_HOST'),
                                              os.getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    """====================================================================="""
    """== METHODS =========================================================="""
    """====================================================================="""

    """----------"""
    """- Public -"""
    """----------"""

    def all(self, cls=None):
        """ This method queries all objects depending on the class name. """
        dictt = {}
        if cls:
            objs = self.__session.query(cls).all()

        else:
            objs = []
            classes = ['Amenity', 'City', 'Place', 'Review', 'State', 'User']
            for clss in classes:
                ret = self.__session.query(eval(clss))
                for r in ret:
                    objs.append(result)

        for obj in objs:
            key = type(obj).__name__ + "." + obj.id
            ret[key] = obj

        return ret

    def new(self, obj):
        """ Adds element into the session. """
        self.__session.add(obj)

    def save(self):
        """ Saves the changes """
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes an object. """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Creates all tables in database. """
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))

        self.__session = Session()

    """-----------"""
    """- Private -"""
    """-----------"""

    """-----------"""
    """- Class ---"""
    """-----------"""

    """-----------"""
    """- Static --"""
    """-----------"""

    """====================================================================="""
    """== SETTERS & GETTERS ================================================"""
    """====================================================================="""
