# app/models/user.py
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    is_admin = Column(Boolean, default=False)
    profile = relationship("UserProfile", back_populates="user", uselist=False)
    wallets = relationship("Wallet", back_populates="owner", lazy="joined")  

class UserProfile(Base):
    __tablename__ = "user_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    is_seller = Column(Boolean, default=False)  
    is_buyer = Column(Boolean, default=True)  
    user = relationship("User", back_populates="profile")
