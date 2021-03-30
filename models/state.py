#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Class State that inherits from Base"""
    if models.storage_type == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        name = ""

    if models.storage_type != 'db':
        @property
        def cities(self):
            """Getter returns the list of City instances
               - with the state_id = State.id"""
            list_cities = []
            # all: returns a dictionary of models currently in FileStorage"""
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    list_cities.append(city)
            return list_cities

    def __init__(self, *args, **kwargs):
        """Initializing of the state"""
        super().__init__(*args, **kwargs)
