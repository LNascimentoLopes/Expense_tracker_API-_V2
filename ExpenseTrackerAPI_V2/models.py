from sqlalchemy import Column, Integer, String, ForeignKey, Float
from base import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)

class Expense(Base):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, unique=True, index=True, nullable=False)
    value = Column(Float, nullable=False)
    date = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))