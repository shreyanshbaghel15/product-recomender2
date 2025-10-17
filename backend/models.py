from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text)
    category = Column(String, index=True)
    price = Column(Float)
    image_url = Column(String)
    rating = Column(Float, default=0.0)
    tags = Column(String)  # Comma-separated tags
    
    interactions = relationship("UserInteraction", back_populates="product")

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    preferences = Column(String)  # JSON string of user preferences
    
    interactions = relationship("UserInteraction", back_populates="user")

class UserInteraction(Base):
    __tablename__ = "user_interactions"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    interaction_type = Column(String)  # view, click, purchase, cart, wishlist
    rating = Column(Float, nullable=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", back_populates="interactions")
    product = relationship("Product", back_populates="interactions")
