from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

from datetime import datetime, timedelta

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
        }

class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'))
    item_category = relationship(Category)
    creator_id = Column(Integer, ForeignKey('user.id'))
    item_creator = relationship(User)
    date = Column(DateTime, default=datetime.utcnow)
    
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'category id': self.category_id,
            'name': self.name,
            'description': self.description,

        }

engine = create_engine('sqlite:///catalog.db')
Base.metadata.create_all(engine)
