from sqlalchemy.orm import Session
from models import Product, User, UserInteraction
from database import SessionLocal, engine, Base
from datetime import datetime, timedelta
import random

def seed_database():
    """Seed the database with sample data"""
    
    # Create tables
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    
    # Clear existing data
    db.query(UserInteraction).delete()
    db.query(Product).delete()
    db.query(User).delete()
    
    # Sample products
    products_data = [
        {
            "name": "Wireless Bluetooth Headphones",
            "description": "Premium noise-cancelling headphones with 30-hour battery life and superior sound quality",
            "category": "Electronics",
            "price": 129.99,
            "image_url": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400",
            "rating": 4.5,
            "tags": "audio,wireless,bluetooth,music"
        },
        {
            "name": "Smart Fitness Watch",
            "description": "Track your health with heart rate monitoring, GPS, and sleep tracking",
            "category": "Electronics",
            "price": 199.99,
            "image_url": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400",
            "rating": 4.7,
            "tags": "fitness,health,smartwatch,wearable"
        },
        {
            "name": "Yoga Mat Premium",
            "description": "Eco-friendly non-slip yoga mat with extra cushioning for comfort",
            "category": "Sports",
            "price": 39.99,
            "image_url": "https://images.unsplash.com/photo-1601925260368-ae2f83cf8b7f?w=400",
            "rating": 4.3,
            "tags": "yoga,fitness,exercise,wellness"
        },
        {
            "name": "Organic Green Tea",
            "description": "Premium organic green tea leaves, rich in antioxidants",
            "category": "Food",
            "price": 24.99,
            "image_url": "https://images.unsplash.com/photo-1564890369478-c89ca6d9cde9?w=400",
            "rating": 4.6,
            "tags": "tea,organic,health,beverage"
        },
        {
            "name": "Running Shoes Pro",
            "description": "Lightweight running shoes with advanced cushioning technology",
            "category": "Sports",
            "price": 89.99,
            "image_url": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400",
            "rating": 4.8,
            "tags": "running,shoes,sports,fitness"
        },
        {
            "name": "Laptop Stand Aluminum",
            "description": "Ergonomic laptop stand for better posture and cooling",
            "category": "Electronics",
            "price": 49.99,
            "image_url": "https://images.unsplash.com/photo-1527864550417-7fd91fc51a46?w=400",
            "rating": 4.4,
            "tags": "laptop,desk,ergonomic,office"
        },
        {
            "name": "Protein Powder Vanilla",
            "description": "Whey protein isolate for muscle recovery and growth",
            "category": "Food",
            "price": 54.99,
            "image_url": "https://images.unsplash.com/photo-1579722821273-0f6c7d44362f?w=400",
            "rating": 4.5,
            "tags": "protein,fitness,nutrition,supplement"
        },
        {
            "name": "Meditation Cushion",
            "description": "Comfortable meditation cushion for mindfulness practice",
            "category": "Wellness",
            "price": 34.99,
            "image_url": "https://images.unsplash.com/photo-1545389336-cf090694435e?w=400",
            "rating": 4.2,
            "tags": "meditation,wellness,mindfulness,cushion"
        },
        {
            "name": "Water Bottle Insulated",
            "description": "Stainless steel water bottle keeps drinks cold for 24 hours",
            "category": "Sports",
            "price": 29.99,
            "image_url": "https://images.unsplash.com/photo-1602143407151-7111542de6e8?w=400",
            "rating": 4.6,
            "tags": "water,bottle,hydration,sports"
        },
        {
            "name": "Resistance Bands Set",
            "description": "Complete set of resistance bands for home workouts",
            "category": "Sports",
            "price": 24.99,
            "image_url": "https://images.unsplash.com/photo-1598289431512-b97b0917affc?w=400",
            "rating": 4.4,
            "tags": "fitness,exercise,resistance,workout"
        }
    ]
    
    products = []
    for p_data in products_data:
        product = Product(**p_data)
        db.add(product)
        products.append(product)
    
    db.commit()
    
    # Sample users
    users_data = [
        {"username": "john_doe", "email": "john@example.com", "preferences": "fitness,electronics"},
        {"username": "jane_smith", "email": "jane@example.com", "preferences": "wellness,food"},
        {"username": "mike_wilson", "email": "mike@example.com", "preferences": "sports,electronics"}
    ]
    
    users = []
    for u_data in users_data:
        user = User(**u_data)
        db.add(user)
        users.append(user)
    
    db.commit()
    
    # Sample interactions
    interaction_types = ["view", "click", "cart", "purchase", "wishlist"]
    
    for user in users:
        # Each user interacts with 3-7 random products
        num_interactions = random.randint(3, 7)
        selected_products = random.sample(products, num_interactions)
        
        for i, product in enumerate(selected_products):
            interaction = UserInteraction(
                user_id=user.id,
                product_id=product.id,
                interaction_type=random.choice(interaction_types),
                rating=random.uniform(3.5, 5.0) if random.random() > 0.5 else None,
                timestamp=datetime.utcnow() - timedelta(days=random.randint(0, 30))
            )
            db.add(interaction)
    
    db.commit()
    db.close()
    
    print("Database seeded successfully!")

if __name__ == "__main__":
    seed_database()
