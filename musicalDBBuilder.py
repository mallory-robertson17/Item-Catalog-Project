import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base= declarative_base()

class Actor(Base):
    __tablename__='actor'

    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False)


class Musical(Base):
    __tablename__='musical'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    summary = Column(String(500))
    year = Column(String(8), nullable=False)


class Character(Base):
    __tablename__='character'

    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False)
    actor_id = Column(Integer, ForeignKey('actor.id'))
    actor = relationship(Actor)
    musical_id = Column(Integer, ForeignKey('musical.id'))
    musical = relationship(Musical)


engine = create_engine('sqlite:///broadwaymusicals.db')

Base.metadata.create_all(engine)
