#!/usr/bin/python3
""" City Module for HBNB project """

import models
from models.base_model import BaseModel, Base
# from models.place import Place
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ Class City that inherits from BaseModel and Base"""
    if models.storage_type == 'db':
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place", backref="cities", cascade="all, delete")
    else:
        name = ""
        state_id = ""

    def __init__(self, *args, **kwargs):
        """Initialise a city"""
        super().__init__(self, *args, **kwargs)
