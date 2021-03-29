#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


"""Allows us to create classes that include directives to describe
the actual database table they will be mapped to"""
Base = declarative_base()


class State(BaseModel, Base):
    """Class State that inherits from Base"""
     __tablename__ = 'states'
    name = Column(String(128),
                  nullable=False)
