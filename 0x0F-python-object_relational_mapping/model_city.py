#!/usr/bin/python3
"""
Write a Python file similar to
model_state.py named model_city.py
that contains the class definition
of a City.
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String

Base = declarative_base()


class City(Base):
    """Class City"""

    __tablename__ = 'cities'

    id = Column(Integer,
                autoincrement=True,
                primary_key=True,
                nullable=False)

    name = Column(String(128),
                  nullable=False)

    state_id = Column(Integer,
                      ForeignKey('states.id'),
                      nullable=False)
