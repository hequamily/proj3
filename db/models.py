from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    score = Column(Integer())

    def __repr__(self):
        return f'Player id: {self.id}, name: {self.name}, score: {self.score}'