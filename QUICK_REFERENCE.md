# ⚡ Quick Reference Card

One-page reference for the E-commerce Product Recommender.

## 🚀 Quick Start Commands

### Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate          # Windows
pip install -r requirements.txt
copy .env.example .env
python seed_data.py
python main.py
```

### Frontend
```bash
cd frontend
npm install
npm start
```

### Windows Shortcuts
```bash
backend\run.bat    # Start backend
frontend\run.bat   # Start frontend
```

## 📡 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/products` | GET | List all products |
| `/products/{id}` | GET | Get product details |
| `/users` | GET | List all users |
| `/recommendations/{user_id}` | GET | Get recommendations |
| `/interactions` | POST | Record interaction |

**API Docs**: `http://localhost:8000/docs`

## 🗄️ Database Models

### Product
- id, name, description, category, price, image_url, rating, tags

### User
- id, username, email, preferences

### UserInteraction
- id, user_id, product_id, interaction_type, rating, timestamp

## 🤖 Recommendation Algorithm

```
Hybrid Score = (Collaborative × 0.6) + (Content-Based × 0.4)
```

**Interaction Weights**:
- View: 1
- Click: 2
- Cart: 3
- Wishlist: 4
- Purchase: 5

## 🔑 Environment Variables

```env
OPENAI_API_KEY=sk-your-key-here
DATABASE_URL=sqlite:///./ecommerce.db
```

## 📂 Project Structure

```
ecommerce-recommender/
├── backend/
│   ├── main.py              # API endpoints
│   ├── recommender.py       # ML algorithms
│   ├── llm_service.py       # AI explanations
│   ├── models.py            # Database models
│   └── seed_data.py         # Sample data
├── frontend/
│   └── src/
│       ├── App.js           # Main component
│       └── App.css          # Styles
└── README.md
```

## 🎨 Sample Users

| ID | Username | Preferences |
|----|----------|-------------|
| 1 | john_doe | fitness, electronics |
| 2 | jane_smith | wellness, food |
| 3 | mike_wilson | sports, electronics |

## 🛠️ Common Tasks

### Add New Product
```python
# Via API or seed_data.py
{
  "name": "Product Name",
  "description": "Description",
  "category": "Category",
  "price": 99.99,
  "image_url": "https://...",
  "rating": 4.5,
  "tags": "tag1,tag2"
}
```

### Record Interaction
```javascript
axios.post('http://localhost:8000/interactions', {
  user_id: 1,
  product_id: 5,
  interaction_type: 'cart'
});
```

### Get Recommendations
```javascript
axios.get('http://localhost:8000/recommendations/1?num_recommendations=5');
```

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| Port 8000 in use | `taskkill /F /IM python.exe` |
| Port 3000 in use | Type 'Y' when prompted |
| Module not found | `pip install -r requirements.txt` |
| No recommendations | Run `python seed_data.py` |
| CORS error | Restart both servers |

## 📊 URLs

- **Frontend**: `http://localhost:3000`
- **Backend**: `http://localhost:8000`
- **API Docs**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## 🔧 Configuration

### Recommendation Weights (recommender.py)
```python
# Line ~95
combined_scores[product_id] = score * 0.6  # Collaborative
combined_scores[product_id] = score * 0.4  # Content-based
```

### Number of Recommendations (main.py)
```python
# Default: 5
def get_recommendations(user_id: int, num_recommendations: int = 5)
```

## 📝 File Locations

| File | Purpose |
|------|---------|
| `backend/.env` | API keys |
| `backend/ecommerce.db` | Database |
| `backend/seed_data.py` | Sample data |
| `frontend/src/App.js` | UI logic |
| `frontend/src/App.css` | Styles |

## 🎯 Testing Workflow

1. Start backend → Start frontend
2. Select user from dropdown
3. View recommendations tab
4. Interact with products (view/cart/wishlist)
5. Click refresh to see updated recommendations
6. Switch users to compare

## 💡 Tips

- ✅ Keep both terminals open
- ✅ Check browser console (F12) for errors
- ✅ Use API docs for testing
- ✅ Activate venv before running backend
- ✅ Clear browser cache if issues

## 📚 Documentation Files

- `README.md` - Main documentation
- `SETUP_GUIDE.md` - Detailed setup
- `START_HERE.md` - Quick start
- `API_DOCUMENTATION.md` - API reference
- `TROUBLESHOOTING.md` - Common issues
- `FEATURES.md` - Feature list
- `PROJECT_STRUCTURE.md` - Architecture

## 🔄 Update Recommendations

```python
# After adding interactions
recommender = ProductRecommender(db)
recommendations = recommender.hybrid_recommendations(user_id, 5)
```

## 🎨 Customize UI

**Colors** (App.css):
```css
/* Line ~15 - Header gradient */
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);

/* Change to your colors */
background: linear-gradient(135deg, #your-color1 0%, #your-color2 100%);
```

## 📦 Dependencies

**Backend**: FastAPI, SQLAlchemy, OpenAI, Scikit-learn
**Frontend**: React, Axios

## 🚀 Deployment

**Backend**: Heroku, Railway, Render
**Frontend**: Netlify, Vercel, GitHub Pages

## ⚙️ Advanced

### Custom Algorithm
Edit `recommender.py` → `hybrid_recommendations()`

### Custom LLM
Edit `llm_service.py` → `generate_explanation()`

### Add Authentication
Implement JWT in `main.py`

---

**Print this page for quick reference! 📄**
