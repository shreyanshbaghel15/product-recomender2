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

```
┌─────────────────┐
│  React Frontend │
│   (Dashboard)   │
└────────┬────────┘
         │
         │ HTTP/REST
         │
┌────────▼────────┐
│  FastAPI Backend│
│                 │
├─────────────────┤
│  Recommender    │
│  Engine         │
│  - Collaborative│
│  - Content-Based│
│  - Hybrid       │
├─────────────────┤
│  LLM Service    │
│  (OpenAI GPT)   │
└────────┬────────┘
         │
┌────────▼────────┐
│ SQLite Database │
│  - Products     │
│  - Users        │
│  - Interactions │
└─────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Node.js 14 or higher
- OpenAI API key (optional, but recommended for LLM explanations)

### Backend Setup

1. **Navigate to backend directory**:
   ```bash
   cd backend
   ```

2. **Create virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment**:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables**:
   ```bash
   cp .env.example .env
   ```
   Edit `.env` and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   DATABASE_URL=sqlite:///./ecommerce.db
   ```

6. **Seed the database**:
   ```bash
   python seed_data.py
   ```

7. **Run the backend server**:
   ```bash
   python main.py
   ```
   
   The API will be available at `http://localhost:8000`

### Frontend Setup

1. **Navigate to frontend directory**:
   ```bash
   cd frontend
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Start the development server**:
   ```bash
   npm start
   ```
   
   The application will open at `http://localhost:3000`

## 📊 How It Works

### 1. Recommendation Algorithm

The system uses a **hybrid approach** combining:

#### Collaborative Filtering
- Analyzes user-item interaction patterns
- Finds similar users based on behavior
- Recommends products liked by similar users
- Uses cosine similarity for user comparison

#### Content-Based Filtering
- Analyzes product features (name, description, category, tags)
- Uses TF-IDF vectorization for text features
- Recommends products similar to user's history
- Calculates similarity between product features

#### Hybrid Score
```
Final Score = (Collaborative Score × 0.6) + (Content-Based Score × 0.4)
```

### 2. LLM Explanation Generation

For each recommendation, the system:
1. Gathers user behavior context
2. Extracts product details
3. Sends a prompt to OpenAI's GPT model
4. Receives a personalized explanation

**Example Prompt**:
```
Explain why we're recommending this product to the user:

Product: Wireless Bluetooth Headphones
Category: Electronics
Description: Premium noise-cancelling headphones...

User Behavior:
- Recently viewed: Smart Fitness Watch, Laptop Stand
- Favorite categories: Electronics, Sports
- Total interactions: 15

Generate a personalized explanation (2-3 sentences).
```

### 3. User Interaction Tracking

The system tracks five types of interactions:
- **View**: User views product details (weight: 1)
- **Click**: User clicks on product (weight: 2)
- **Cart**: User adds to cart (weight: 3)
- **Wishlist**: User adds to wishlist (weight: 4)
- **Purchase**: User purchases product (weight: 5)

## 📡 API Endpoints

### Products
- `GET /products` - Get all products
- `GET /products/{product_id}` - Get specific product
- `POST /products` - Create new product

### Users
- `GET /users` - Get all users
- `GET /users/{user_id}` - Get specific user
- `POST /users` - Create new user

### Interactions
- `GET /interactions` - Get all interactions
- `POST /interactions` - Create new interaction
- `GET /interactions/user/{user_id}` - Get user's interactions

### Recommendations
- `GET /recommendations/{user_id}` - Get personalized recommendations
- `POST /recommendations/request` - Request recommendations with parameters

### API Documentation
Visit `http://localhost:8000/docs` for interactive API documentation (Swagger UI)

## 🎨 Frontend Features

- **User Selection**: Switch between different users to see personalized recommendations
- **Recommendations Tab**: View AI-powered recommendations with explanations
- **All Products Tab**: Browse complete product catalog
- **Interactive Actions**: View, add to cart, or wishlist products
- **Real-time Updates**: Recommendations update based on user interactions
- **Responsive Design**: Works on desktop, tablet, and mobile devices

## 🗄️ Database Schema

### Products Table
```sql
- id: Integer (Primary Key)
- name: String
- description: Text
- category: String
- price: Float
- image_url: String
- rating: Float
- tags: String (comma-separated)
```

### Users Table
```sql
- id: Integer (Primary Key)
- username: String (Unique)
- email: String (Unique)
- preferences: String (JSON)
```

### UserInteractions Table
```sql
- id: Integer (Primary Key)
- user_id: Integer (Foreign Key)
- product_id: Integer (Foreign Key)
- interaction_type: String
- rating: Float (Optional)
- timestamp: DateTime
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `OPENAI_API_KEY` | OpenAI API key for LLM | None (optional) |
| `DATABASE_URL` | Database connection string | `sqlite:///./ecommerce.db` |

### Recommendation Parameters

You can adjust these in `recommender.py`:
- **Collaborative weight**: 0.6 (60%)
- **Content-based weight**: 0.4 (40%)
- **Number of recommendations**: 5 (default)
- **Interaction weights**: Customizable in `get_user_interaction_matrix()`

## 📈 Sample Data

The system comes with pre-seeded data:
- **10 Products** across categories (Electronics, Sports, Food, Wellness)
- **3 Sample Users** with different preferences
- **Random Interactions** to demonstrate the recommendation engine

## 🧪 Testing the System

1. **Start both backend and frontend servers**
2. **Select a user** from the dropdown
3. **View recommendations** - See personalized products with AI explanations
4. **Interact with products** - Click view, cart, or wishlist buttons
5. **Refresh recommendations** - See how they update based on your interactions
6. **Switch users** - Compare different recommendation profiles

## 🚀 Deployment

### Backend Deployment (Example: Heroku)
```bash
# Install Heroku CLI
# Login to Heroku
heroku login

# Create new app
heroku create your-app-name

# Set environment variables
heroku config:set OPENAI_API_KEY=your_key

# Deploy
git push heroku main
```

### Frontend Deployment (Example: Netlify)
```bash
# Build the app
npm run build

# Deploy to Netlify
# Upload the 'build' folder to Netlify
```

## 🛠️ Tech Stack

### Backend
- **FastAPI**: Modern, fast web framework
- **SQLAlchemy**: SQL toolkit and ORM
- **Scikit-learn**: Machine learning algorithms
- **Pandas & NumPy**: Data manipulation
- **OpenAI**: LLM integration
- **Uvicorn**: ASGI server

### Frontend
- **React**: UI library
- **Axios**: HTTP client
- **CSS3**: Styling with gradients and animations

## 📝 Future Enhancements

- [ ] Add user authentication and authorization
- [ ] Implement real-time notifications
- [ ] Add product search and filtering
- [ ] Include product reviews and ratings
- [ ] Implement A/B testing for recommendations
- [ ] Add more recommendation algorithms (Matrix Factorization, Deep Learning)
- [ ] Create admin dashboard for analytics
- [ ] Add email notifications for recommendations
- [ ] Implement caching for better performance
- [ ] Add multi-language support

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

Built with ❤️ for demonstrating AI-powered recommendation systems

## 🙏 Acknowledgments

- OpenAI for GPT API
- FastAPI community
- React community
- Scikit-learn contributors

## 📞 Support

For questions or issues, please open an issue on GitHub.

---

**Happy Recommending! 🎉**
