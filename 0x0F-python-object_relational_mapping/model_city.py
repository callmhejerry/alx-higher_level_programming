#!/usr/bin/python3

'''
This module contains the class definition of a state
and an instance Base = declarative_base():
'''
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City (Base):
    '''
    this is the City class that maps to the
    City table
    '''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
