# 📡 API Documentation

Complete API reference for the E-commerce Product Recommender system.

**Base URL**: `http://localhost:8000`

## 🔍 Interactive Documentation

FastAPI provides automatic interactive API documentation:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## 📋 Endpoints Overview

### Products
- `GET /products` - List all products
- `GET /products/{product_id}` - Get product details
- `POST /products` - Create new product

### Users
- `GET /users` - List all users
- `GET /users/{user_id}` - Get user details
- `POST /users` - Create new user

### Interactions
- `GET /interactions` - List all interactions
- `POST /interactions` - Create new interaction
- `GET /interactions/user/{user_id}` - Get user's interactions

### Recommendations
- `GET /recommendations/{user_id}` - Get personalized recommendations
- `POST /recommendations/request` - Request recommendations with parameters

---

## 📦 Products API

### List All Products

```http
GET /products
```

**Query Parameters:**
- `skip` (integer, optional): Number of records to skip (default: 0)
- `limit` (integer, optional): Maximum number of records (default: 100)

**Response:**
```json
[
  {
    "id": 1,
    "name": "Wireless Bluetooth Headphones",
    "description": "Premium noise-cancelling headphones...",
    "category": "Electronics",
    "price": 129.99,
    "image_url": "https://images.unsplash.com/...",
    "rating": 4.5,
    "tags": "audio,wireless,bluetooth,music"
  }
]
```

### Get Product Details

```http
GET /products/{product_id}
```

**Path Parameters:**
- `product_id` (integer, required): Product ID

**Response:**
```json
{
  "id": 1,
  "name": "Wireless Bluetooth Headphones",
  "description": "Premium noise-cancelling headphones...",
  "category": "Electronics",
  "price": 129.99,
  "image_url": "https://images.unsplash.com/...",
  "rating": 4.5,
  "tags": "audio,wireless,bluetooth,music"
}
```

**Error Response (404):**
```json
{
  "detail": "Product not found"
}
```

### Create Product

```http
POST /products
```

**Request Body:**
```json
{
  "name": "Smart Watch Pro",
  "description": "Advanced fitness tracking smartwatch",
  "category": "Electronics",
  "price": 299.99,
  "image_url": "https://example.com/image.jpg",
  "rating": 4.7,
  "tags": "fitness,smartwatch,health"
}
```

**Response:**
```json
{
  "id": 11,
  "name": "Smart Watch Pro",
  "description": "Advanced fitness tracking smartwatch",
  "category": "Electronics",
  "price": 299.99,
  "image_url": "https://example.com/image.jpg",
  "rating": 4.7,
  "tags": "fitness,smartwatch,health"
}
```

---

## 👥 Users API

### List All Users

```http
GET /users
```

**Query Parameters:**
- `skip` (integer, optional): Number of records to skip (default: 0)
- `limit` (integer, optional): Maximum number of records (default: 100)

**Response:**
```json
[
  {
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com",
    "preferences": "fitness,electronics"
  }
]
```

### Get User Details

```http
GET /users/{user_id}
```

**Path Parameters:**
- `user_id` (integer, required): User ID

**Response:**
```json
{
  "id": 1,
  "username": "john_doe",
  "email": "john@example.com",
  "preferences": "fitness,electronics"
}
```

### Create User

```http
POST /users
```

**Request Body:**
```json
{
  "username": "alice_wonder",
  "email": "alice@example.com",
  "preferences": "books,technology"
}
```

**Response:**
```json
{
  "id": 4,
  "username": "alice_wonder",
  "email": "alice@example.com",
  "preferences": "books,technology"
}
```

---

## 🔄 Interactions API

### List All Interactions

```http
GET /interactions
```

**Query Parameters:**
- `skip` (integer, optional): Number of records to skip (default: 0)
- `limit` (integer, optional): Maximum number of records (default: 100)

**Response:**
```json
[
  {
    "id": 1,
    "user_id": 1,
    "product_id": 2,
    "interaction_type": "view",
    "rating": 4.5,
    "timestamp": "2024-01-15T10:30:00"
  }
]
```

### Create Interaction

```http
POST /interactions
```

**Request Body:**
```json
{
  "user_id": 1,
  "product_id": 5,
  "interaction_type": "purchase",
  "rating": 5.0
}
```

**Interaction Types:**
- `view` - User viewed the product
- `click` - User clicked on the product
- `cart` - User added to cart
- `wishlist` - User added to wishlist
- `purchase` - User purchased the product

**Response:**
```json
{
  "id": 25,
  "user_id": 1,
  "product_id": 5,
  "interaction_type": "purchase",
  "rating": 5.0,
  "timestamp": "2024-01-15T14:22:33"
}
```

### Get User's Interactions

```http
GET /interactions/user/{user_id}
```

**Path Parameters:**
- `user_id` (integer, required): User ID

**Response:**
```json
[
  {
    "id": 1,
    "user_id": 1,
    "product_id": 2,
    "interaction_type": "view",
    "rating": null,
    "timestamp": "2024-01-10T09:15:00"
  },
  {
    "id": 5,
    "user_id": 1,
    "product_id": 7,
    "interaction_type": "purchase",
    "rating": 5.0,
    "timestamp": "2024-01-12T16:45:00"
  }
]
```

---

## 🎯 Recommendations API

### Get Personalized Recommendations

```http
GET /recommendations/{user_id}
```

**Path Parameters:**
- `user_id` (integer, required): User ID

**Query Parameters:**
- `num_recommendations` (integer, optional): Number of recommendations (default: 5)

**Response:**
```json
[
  {
    "product": {
      "id": 3,
      "name": "Yoga Mat Premium",
      "description": "Eco-friendly non-slip yoga mat...",
      "category": "Sports",
      "price": 39.99,
      "image_url": "https://images.unsplash.com/...",
      "rating": 4.3,
      "tags": "yoga,fitness,exercise,wellness"
    },
    "score": 0.85,
    "explanation": "Based on your interest in fitness products and recent views of sports equipment, this premium yoga mat is perfect for your wellness journey. Users with similar preferences have highly rated this product!"
  }
]
```

**Error Response (404):**
```json
{
  "detail": "User not found"
}
```

### Request Recommendations (POST)

```http
POST /recommendations/request
```

**Request Body:**
```json
{
  "user_id": 1,
  "num_recommendations": 10
}
```

**Response:**
Same as GET endpoint above.

---

## 🔐 Authentication

Currently, the API does not require authentication. In production, you should implement:
- JWT tokens
- API keys
- OAuth 2.0

## 📊 Response Codes

| Code | Description |
|------|-------------|
| 200 | Success |
| 201 | Created |
| 400 | Bad Request |
| 404 | Not Found |
| 422 | Validation Error |
| 500 | Internal Server Error |

## 🧪 Example Usage

### Using cURL

**Get Recommendations:**
```bash
curl -X GET "http://localhost:8000/recommendations/1?num_recommendations=5"
```

**Create Interaction:**
```bash
curl -X POST "http://localhost:8000/interactions" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": 1,
    "product_id": 3,
    "interaction_type": "cart"
  }'
```

### Using Python

```python
import requests

# Get recommendations
response = requests.get('http://localhost:8000/recommendations/1')
recommendations = response.json()

for rec in recommendations:
    print(f"Product: {rec['product']['name']}")
    print(f"Score: {rec['score']}")
    print(f"Explanation: {rec['explanation']}\n")

# Create interaction
interaction_data = {
    "user_id": 1,
    "product_id": 5,
    "interaction_type": "purchase",
    "rating": 5.0
}
response = requests.post(
    'http://localhost:8000/interactions',
    json=interaction_data
)
print(response.json())
```

### Using JavaScript (Axios)

```javascript
import axios from 'axios';

// Get recommendations
const getRecommendations = async (userId) => {
  try {
    const response = await axios.get(
      `http://localhost:8000/recommendations/${userId}`
    );
    console.log(response.data);
  } catch (error) {
    console.error('Error:', error);
  }
};

// Create interaction
const createInteraction = async (userId, productId, type) => {
  try {
    const response = await axios.post(
      'http://localhost:8000/interactions',
      {
        user_id: userId,
        product_id: productId,
        interaction_type: type
      }
    );
    console.log(response.data);
  } catch (error) {
    console.error('Error:', error);
  }
};

getRecommendations(1);
createInteraction(1, 5, 'cart');
```

## 🎨 Data Models

### Product
```typescript
interface Product {
  id: number;
  name: string;
  description: string;
  category: string;
  price: number;
  image_url: string;
  rating: number;
  tags: string;
}
```

### User
```typescript
interface User {
  id: number;
  username: string;
  email: string;
  preferences: string;
}
```

### UserInteraction
```typescript
interface UserInteraction {
  id: number;
  user_id: number;
  product_id: number;
  interaction_type: 'view' | 'click' | 'cart' | 'wishlist' | 'purchase';
  rating?: number;
  timestamp: string;
}
```

### RecommendationResponse
```typescript
interface RecommendationResponse {
  product: Product;
  score: number;
  explanation: string;
}
```

## 🚀 Rate Limiting

Currently no rate limiting is implemented. For production:
- Implement rate limiting per IP/user
- Use Redis for distributed rate limiting
- Set appropriate limits (e.g., 100 requests/minute)

## 📝 Notes

- All timestamps are in UTC
- Prices are in USD
- Ratings are on a scale of 0-5
- The recommendation score is normalized between 0-1

---

For more details, visit the interactive documentation at `http://localhost:8000/docs`
