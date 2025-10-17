# 🚀 Setup Guide - E-commerce Product Recommender

This guide will walk you through setting up the E-commerce Product Recommender system step by step.

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8+**: [Download Python](https://www.python.org/downloads/)
- **Node.js 14+**: [Download Node.js](https://nodejs.org/)
- **Git**: [Download Git](https://git-scm.com/downloads)
- **OpenAI API Key** (Optional but recommended): [Get API Key](https://platform.openai.com/api-keys)

## 🎯 Step-by-Step Setup

### Step 1: Clone or Download the Repository

If you have the project folder, navigate to it:
```bash
cd ecommerce-recommender
```

### Step 2: Backend Setup

#### 2.1 Navigate to Backend Directory
```bash
cd backend
```

#### 2.2 Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt.

#### 2.3 Install Python Dependencies
```bash
pip install -r requirements.txt
```

This will install:
- FastAPI (Web framework)
- SQLAlchemy (Database ORM)
- OpenAI (LLM integration)
- Scikit-learn (ML algorithms)
- And other dependencies

#### 2.4 Configure Environment Variables

1. Copy the example environment file:
   ```bash
   copy .env.example .env
   ```
   (On macOS/Linux: `cp .env.example .env`)

2. Edit `.env` file and add your OpenAI API key:
   ```
   OPENAI_API_KEY=sk-your-actual-api-key-here
   DATABASE_URL=sqlite:///./ecommerce.db
   ```

   **Note**: If you don't have an OpenAI API key, the system will still work but will use fallback explanations instead of AI-generated ones.

#### 2.5 Seed the Database
```bash
python seed_data.py
```

This creates:
- 10 sample products
- 3 sample users
- Random user interactions

You should see: `Database seeded successfully!`

#### 2.6 Start the Backend Server
```bash
python main.py
```

You should see:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
```

✅ **Backend is now running!**

Open `http://localhost:8000/docs` to see the API documentation.

### Step 3: Frontend Setup

Open a **new terminal window** (keep the backend running).

#### 3.1 Navigate to Frontend Directory
```bash
cd frontend
```

#### 3.2 Install Node Dependencies
```bash
npm install
```

This will install:
- React
- Axios
- React Router
- And other dependencies

#### 3.3 Start the Development Server
```bash
npm start
```

The application will automatically open in your browser at `http://localhost:3000`

✅ **Frontend is now running!**

## 🎉 You're All Set!

You should now have:
- ✅ Backend API running on `http://localhost:8000`
- ✅ Frontend application running on `http://localhost:3000`
- ✅ Database with sample data

## 🧪 Testing the Application

1. **Select a User**: Choose a user from the dropdown (e.g., "john_doe")
2. **View Recommendations**: Click on "Recommendations" tab
3. **See AI Explanations**: Read why each product is recommended
4. **Interact with Products**: Click "View", "Add to Cart", or "Wishlist"
5. **Refresh**: Click the refresh button to see updated recommendations
6. **Browse All Products**: Switch to "All Products" tab

## 🔧 Troubleshooting

### Backend Issues

**Problem**: `ModuleNotFoundError: No module named 'fastapi'`
- **Solution**: Make sure virtual environment is activated and run `pip install -r requirements.txt`

**Problem**: Database errors
- **Solution**: Delete `ecommerce.db` and run `python seed_data.py` again

**Problem**: Port 8000 already in use
- **Solution**: Kill the process using port 8000 or change the port in `main.py`

### Frontend Issues

**Problem**: `npm: command not found`
- **Solution**: Install Node.js from [nodejs.org](https://nodejs.org/)

**Problem**: Port 3000 already in use
- **Solution**: The app will ask if you want to use another port. Type 'Y' and press Enter

**Problem**: Cannot connect to backend
- **Solution**: Make sure backend is running on `http://localhost:8000`

### OpenAI API Issues

**Problem**: OpenAI API errors
- **Solution**: Check your API key in `.env` file and ensure you have credits

**Problem**: No API key
- **Solution**: The system will work with fallback explanations (no AI)

## 🚀 Quick Start (Windows)

For Windows users, you can use the batch files:

**Backend:**
```bash
cd backend
run.bat
```

**Frontend (in new terminal):**
```bash
cd frontend
run.bat
```

## 📊 Understanding the Data

### Sample Users
1. **john_doe** - Interested in fitness and electronics
2. **jane_smith** - Interested in wellness and food
3. **mike_wilson** - Interested in sports and electronics

### Sample Products
- Electronics: Headphones, Smart Watch, Laptop Stand
- Sports: Yoga Mat, Running Shoes, Water Bottle, Resistance Bands
- Food: Organic Tea, Protein Powder
- Wellness: Meditation Cushion

## 🎓 Next Steps

1. **Explore the API**: Visit `http://localhost:8000/docs`
2. **Add Your Own Products**: Use the API or modify `seed_data.py`
3. **Create New Users**: Add users through the API
4. **Customize Recommendations**: Modify weights in `recommender.py`
5. **Enhance UI**: Update styles in `App.css`

## 📚 Additional Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://react.dev/)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Scikit-learn Documentation](https://scikit-learn.org/)

## 💡 Tips

- Keep both terminal windows open (backend and frontend)
- Check browser console for any errors (F12)
- Use the API documentation to test endpoints
- Monitor backend terminal for request logs

## 🆘 Need Help?

If you encounter any issues:
1. Check the error messages in terminal
2. Review this setup guide
3. Check the main README.md
4. Open an issue on GitHub

---

**Happy Coding! 🎉**
