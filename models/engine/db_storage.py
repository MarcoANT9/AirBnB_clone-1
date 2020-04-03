#!/usr/bin/python3
"""This is the new database storage engine."""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, relationship
from os import getenv
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage():
    """This is the class for database storage engine.
    """
    __engine = None
    __session = None

    def __init__(self):
        """Instantiation of DBStorage engine class.
        """
        MySQL_user = getenv('HBNB_MYSQL_USER')
        MySQL_pwd = getenv('HBNB_MYSQL_PWD')
        MySQL_host = getenv('HBNB_MYSQL_HOST')
        MySQL_db = getenv('HBNB_MYSQL_DB')
        MySQL_env = getenv('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            MySQL_user, MySQL_pwd, MySQL_host, MySQL_db), pool_pre_ping=True)

        if MySQL_env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Show all class objects.
        """
        my_dict = {}

        if cls:
            objects = self.__session.query(cls).all()
            for obj in objects:
                key = '{}.{}'.format(type(obj).__name__, obj.id)
                my_dict[key] = obj
        else:
            classes = ['State', 'City']
            for c in classes:
                objects = self.__session.query(eval(c)).all()
                for obj in objects:
                    key = '{}.{}'.format(type(obj).__name__, obj.id)
                    my_dict[key] = obj

        return my_dict

    def new(self, obj):
        """Add the object to current session.
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commit all changes of the current session.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session.
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables and create the current database
        session from the engine.
        """
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine,
                                              expire_on_commit=False))
        self.__session = Session()

    def close(self):
        """Call remove() on the private attribute self.__session.
        """
        self.__session.close()
