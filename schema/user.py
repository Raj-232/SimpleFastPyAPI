from sqlalchemy import Column, Integer, String
from database import Base


class User(Base):
    __tablename__ = "user"
    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String(50), index=True)
    email: str = Column(String(50), unique=True, index=True)
    password: str = Column(String(50))