# 🚀 START HERE - Quick Launch Guide

Welcome to the E-commerce Product Recommender! This guide will get you up and running in 5 minutes.

## ⚡ Quick Start (Windows)

### Option 1: Automated Setup (Recommended)

1. **Start Backend** (in first terminal):
   ```bash
   cd backend
   run.bat
   ```
   Wait for "Uvicorn running on http://0.0.0.0:8000"

2. **Start Frontend** (in second terminal):
   ```bash
   cd frontend
   run.bat
   ```
   Your browser will open automatically!

### Option 2: Manual Setup

**Terminal 1 - Backend:**
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
python seed_data.py
python main.py
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm install
npm start
```

## 🎯 What You'll See

1. **Frontend Dashboard** (`http://localhost:3000`)
   - User selector dropdown
   - Personalized recommendations with AI explanations
   - Product catalog
   - Interactive buttons (View, Cart, Wishlist)

2. **Backend API** (`http://localhost:8000`)
   - RESTful API endpoints
   - Interactive documentation at `/docs`

## 🔑 Important Notes

### OpenAI API Key (Optional)

The system works WITHOUT an API key, but for AI-powered explanations:

1. Get a free API key: https://platform.openai.com/api-keys
2. Edit `backend/.env` file
3. Add: `OPENAI_API_KEY=sk-your-key-here`
4. Restart backend

**Without API key**: You'll get rule-based explanations (still works great!)
**With API key**: You'll get personalized AI-generated explanations

## 📱 How to Use

1. **Select a User**: Choose from dropdown (john_doe, jane_smith, or mike_wilson)
2. **View Recommendations**: See personalized products with explanations
3. **Interact**: Click View, Cart, or Wishlist on any product
4. **Refresh**: Click refresh to see updated recommendations
5. **Browse All**: Switch to "All Products" tab

## 🎨 Features to Try

- ✅ Switch between different users to see different recommendations
- ✅ Add products to cart/wishlist and see recommendations update
- ✅ Read AI-generated explanations for each recommendation
- ✅ Check the match score for each product
- ✅ Browse all products in the catalog

## 📚 Documentation

- **Full Setup Guide**: See `SETUP_GUIDE.md`
- **README**: See `README.md` for complete documentation
- **API Docs**: See `API_DOCUMENTATION.md` or visit `http://localhost:8000/docs`

## 🐛 Troubleshooting

**Backend won't start?**
- Make sure Python 3.8+ is installed: `python --version`
- Check if port 8000 is free

**Frontend won't start?**
- Make sure Node.js is installed: `node --version`
- Delete `node_modules` and run `npm install` again

**Can't see recommendations?**
- Make sure backend is running
- Check browser console (F12) for errors
- Verify database was seeded: look for `ecommerce.db` file

## 🎉 Next Steps

1. ✅ Get the system running
2. ✅ Try different users and interactions
3. ✅ Add your OpenAI API key for better explanations
4. ✅ Explore the API documentation
5. ✅ Customize products in `seed_data.py`
6. ✅ Modify recommendation weights in `recommender.py`

## 💡 Pro Tips

- Keep both terminals open while using the app
- Use the API docs (`/docs`) to test endpoints directly
- Check backend terminal for request logs
- Use browser DevTools to see network requests

## 🆘 Need Help?

1. Check `SETUP_GUIDE.md` for detailed instructions
2. Review error messages in terminal
3. Check browser console (F12)
4. See `README.md` for troubleshooting section

---

**Ready to start? Run the commands above and enjoy! 🚀**
