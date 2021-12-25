#!/usr/bin/python3
""" Write a python file that contains the class definition,
of a city and an instance Base = declarative_base()
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()


class City(Base):
    """ City class definition """

    __tablename__ = "cities"
    id = Column(
            Integer,
            autoincrement=True,
            unique=True,
            primary_key=True,
            nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(
            Integer,
            ForeignKey('states.id'),
            nullable=False)
