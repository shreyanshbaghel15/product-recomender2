# 🛍️ E-commerce Product Recommender

An AI-powered product recommendation system that combines collaborative filtering and content-based algorithms with LLM-generated explanations to provide personalized product recommendations.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)
![React](https://img.shields.io/badge/React-18.2+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🎯 Objective

Combine recommendation logic with LLM-powered explanations to help users understand why specific products are recommended to them based on their behavior and preferences.

## ✨ Features

- **Hybrid Recommendation System**: Combines collaborative filtering and content-based filtering
- **LLM-Powered Explanations**: Uses OpenAI's GPT to generate personalized explanations
- **Real-time Interactions**: Track user behavior (views, clicks, cart additions, purchases, wishlists)
- **Beautiful Dashboard**: Modern, responsive React frontend
- **RESTful API**: FastAPI backend with comprehensive endpoints
- **SQLite Database**: Stores products, users, and interaction data
- **Cold Start Handling**: Provides popular products for new users

## 🏗️ Architecture

┌─────────────────┐
│ React Frontend │
│ (Dashboard) │
└────────┬────────┘
│
│ HTTP/REST
│
┌────────▼────────┐
│ FastAPI Backend│
│ │
├─────────────────┤
│ Recommender │
│ Engine │
│ - Collaborative│
│ - Content-Based│
│ - Hybrid │
├─────────────────┤
│ LLM Service │
│ (OpenAI GPT) │
└────────┬────────┘
│
┌────────▼────────┐
│ SQLite Database │
│ - Products │
│ - Users │
│ - Interactions │
└─────────────────┘

markdown
Copy code

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher  
- Node.js 14 or higher  
- OpenAI API key (optional, but recommended for LLM explanations)

### Backend Setup

1. Navigate to backend directory:
   ```bash
   cd backend
Create virtual environment:

bash
Copy code
python -m venv venv
Activate virtual environment:

Windows:

bash
Copy code
venv\Scripts\activate
macOS/Linux:

bash
Copy code
source venv/bin/activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Set up environment variables:

bash
Copy code
cp .env.example .env
Edit .env and add your OpenAI API key:

ini
Copy code
OPENAI_API_KEY=your_openai_api_key_here
DATABASE_URL=sqlite:///./ecommerce.db
Seed the database:

bash
Copy code
python seed_data.py
Run the backend server:

bash
Copy code
python main.py
The API will be available at http://localhost:8000

Frontend Setup
Navigate to frontend directory:

bash
Copy code
cd frontend
Install dependencies:

bash
Copy code
npm install
Start the development server:

bash
Copy code
npm start
The application will open at http://localhost:3000

📊 How It Works
1. Recommendation Algorithm
The system uses a hybrid approach combining:

Collaborative Filtering
Analyzes user-item interaction patterns

Finds similar users based on behavior

Recommends products liked by similar users

Uses cosine similarity for user comparison

Content-Based Filtering
Analyzes product features (name, description, category, tags)

Uses TF-IDF vectorization for text features

Recommends products similar to user's history

Calculates similarity between product features

Hybrid Score
java
Copy code
Final Score = (Collaborative Score × 0.6) + (Content-Based Score × 0.4)
2. LLM Explanation Generation
For each recommendation, the system:

Gathers user behavior context

Extracts product details

Sends a prompt to OpenAI's GPT model

Receives a personalized explanation

Example Prompt:

yaml
Copy code
Explain why we're recommending this product to the user:

Product: Wireless Bluetooth Headphones
Category: Electronics
Description: Premium noise-cancelling headphones...

User Behavior:
- Recently viewed: Smart Fitness Watch, Laptop Stand
- Favorite categories: Electronics, Sports
- Total interactions: 15

Generate a personalized explanation (2-3 sentences).
3. User Interaction Tracking
The system tracks five types of interactions:

View: User views product details (weight: 1)

Click: User clicks on product (weight: 2)

Cart: User adds to cart (weight: 3)

Wishlist: User adds to wishlist (weight: 4)

Purchase: User purchases product (weight: 5)

📡 API Endpoints
Products
GET /products - Get all products

GET /products/{product_id} - Get specific product

POST /products - Create new product

Users
GET /users - Get all users

GET /users/{user_id} - Get specific user

POST /users - Create new user

Interactions
GET /interactions - Get all interactions

POST /interactions - Create new interaction

GET /interactions/user/{user_id} - Get user's interactions

Recommendations
GET /recommendations/{user_id} - Get personalized recommendations

POST /recommendations/request - Request recommendations with parameters

API Documentation
Visit http://localhost:8000/docs for interactive API documentation (Swagger UI)

🎨 Frontend Features
Switch between different users to see personalized recommendations

Recommendations tab shows AI-powered explanations

Browse all products in catalog

Interact with products: view, add to cart, wishlist

Real-time updates of recommendations

Responsive design for desktop, tablet, mobile

🗄️ Database Schema
Products Table
sql
Copy code
- id: Integer (Primary Key)
- name: String
- description: Text
- category: String
- price: Float
- image_url: String
- rating: Float
- tags: String (comma-separated)
Users Table
sql
Copy code
- id: Integer (Primary Key)
- username: String (Unique)
- email: String (Unique)
- preferences: String (JSON)
UserInteractions Table
sql
Copy code
- id: Integer (Primary Key)
- user_id: Integer (Foreign Key)
- product_id: Integer (Foreign Key)
- interaction_type: String
- rating: Float (Optional)