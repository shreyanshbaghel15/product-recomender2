from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class ProductBase(BaseModel):
    name: str
    description: str
    category: str
    price: float
    image_url: str
    rating: Optional[float] = 0.0
    tags: Optional[str] = ""

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    
    class Config:
        from_attributes = True

class UserBase(BaseModel):
    username: str
    email: str
    preferences: Optional[str] = ""

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    
    class Config:
        from_attributes = True

class UserInteractionBase(BaseModel):
    user_id: int
    product_id: int
    interaction_type: str
    rating: Optional[float] = None

class UserInteractionCreate(UserInteractionBase):
    pass

class UserInteraction(UserInteractionBase):
    id: int
    timestamp: datetime
    
    class Config:
        from_attributes = True

class RecommendationResponse(BaseModel):
    product: Product
    score: float
    explanation: str

class RecommendationRequest(BaseModel):
    user_id: int
    num_recommendations: Optional[int] = 5
