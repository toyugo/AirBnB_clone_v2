#!/usr/bin/python3
""" City Module for HBNB project """

from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey


Base = declarative_base()

class City(BaseModel, Base):
    """ Class City that inherits from BaseModel and Base"""
    __tablename__ = 'cities'
    name = Column(String(128),
                    nullable=False)
    state_id = Column(String(60),
            ForeignKey('states.id'),
            nullable=False)
