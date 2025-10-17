from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
import models
import schemas
from database import engine, get_db, Base
from recommender import ProductRecommender
from llm_service import LLMService

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="E-commerce Product Recommender API",
    description="AI-powered product recommendation system with LLM explanations",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize LLM service
llm_service = LLMService()

@app.get("/")
def read_root():
    return {
        "message": "E-commerce Product Recommender API",
        "version": "1.0.0",
        "endpoints": {
            "products": "/products",
            "users": "/users",
            "recommendations": "/recommendations/{user_id}",
            "interactions": "/interactions"
        }
    }

# Product endpoints
@app.get("/products", response_model=List[schemas.Product])
def get_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = db.query(models.Product).offset(skip).limit(limit).all()
    return products

@app.get("/products/{product_id}", response_model=schemas.Product)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.post("/products", response_model=schemas.Product)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

# User endpoints
@app.get("/users", response_model=List[schemas.User])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = db.query(models.User).offset(skip).limit(limit).all()
    return users

@app.get("/users/{user_id}", response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/users", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Interaction endpoints
@app.get("/interactions", response_model=List[schemas.UserInteraction])
def get_interactions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    interactions = db.query(models.UserInteraction).offset(skip).limit(limit).all()
    return interactions

@app.post("/interactions", response_model=schemas.UserInteraction)
def create_interaction(interaction: schemas.UserInteractionCreate, db: Session = Depends(get_db)):
    db_interaction = models.UserInteraction(**interaction.dict())
    db.add(db_interaction)
    db.commit()
    db.refresh(db_interaction)
    return db_interaction

@app.get("/interactions/user/{user_id}", response_model=List[schemas.UserInteraction])
def get_user_interactions(user_id: int, db: Session = Depends(get_db)):
    interactions = db.query(models.UserInteraction).filter(
        models.UserInteraction.user_id == user_id
    ).all()
    return interactions

# Recommendation endpoints
@app.get("/recommendations/{user_id}", response_model=List[schemas.RecommendationResponse])
def get_recommendations(user_id: int, num_recommendations: int = 5, db: Session = Depends(get_db)):
    # Check if user exists
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Get recommendations
    recommender = ProductRecommender(db)
    recommendations = recommender.hybrid_recommendations(user_id, num_recommendations)
    
    # Get user behavior for LLM context
    user_behavior = recommender.get_user_behavior_summary(user_id)
    
    # Build response with LLM explanations
    response = []
    for product_id, score, reason in recommendations:
        product = db.query(models.Product).filter(models.Product.id == product_id).first()
        if product:
            # Generate LLM explanation
            explanation = llm_service.generate_explanation(
                product_name=product.name,
                product_description=product.description,
                product_category=product.category,
                user_behavior=user_behavior,
                recommendation_reason=reason
            )
            
            response.append(schemas.RecommendationResponse(
                product=product,
                score=float(score),
                explanation=explanation
            ))
    
    return response

@app.post("/recommendations/request", response_model=List[schemas.RecommendationResponse])
def request_recommendations(request: schemas.RecommendationRequest, db: Session = Depends(get_db)):
    return get_recommendations(request.user_id, request.num_recommendations, db)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
