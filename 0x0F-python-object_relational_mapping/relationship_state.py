#!/usr/bin/python3

'''
This module contains the class definition of a state
and an instance Base = declarative_base():
'''
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class State (Base):
    '''
    this is the state class that maps to the
    states table
    '''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship('City', back_populates='state',
                          cascade='all, delete-orphan')
