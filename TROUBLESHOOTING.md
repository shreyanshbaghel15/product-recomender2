# 🔧 Troubleshooting Guide

Common issues and solutions for the E-commerce Product Recommender.

## 🐍 Backend Issues

### Issue: "python: command not found"

**Problem**: Python is not installed or not in PATH

**Solutions**:
1. Install Python 3.8+ from [python.org](https://python.org)
2. During installation, check "Add Python to PATH"
3. Verify installation: `python --version`

---

### Issue: "No module named 'fastapi'"

**Problem**: Dependencies not installed or virtual environment not activated

**Solutions**:
1. Activate virtual environment:
   ```bash
   cd backend
   venv\Scripts\activate  # Windows
   source venv/bin/activate  # macOS/Linux
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

### Issue: "Address already in use" (Port 8000)

**Problem**: Another process is using port 8000

**Solutions**:

**Windows**:
```bash
# Find process using port 8000
netstat -ano | findstr :8000

# Kill the process (replace PID with actual process ID)
taskkill /PID <PID> /F
```

**macOS/Linux**:
```bash
# Find and kill process
lsof -ti:8000 | xargs kill -9
```

**Alternative**: Change port in `main.py`:
```python
uvicorn.run(app, host="0.0.0.0", port=8001)  # Use different port
```

---

### Issue: "OpenAI API Error"

**Problem**: Invalid or missing API key

**Solutions**:
1. Check `.env` file exists in backend folder
2. Verify API key format: `OPENAI_API_KEY=sk-...`
3. Ensure you have OpenAI credits
4. The system works without API key (uses fallback explanations)

---

### Issue: "Database locked" or "Database error"

**Problem**: Database file is corrupted or locked

**Solutions**:
1. Close all terminals running the backend
2. Delete `ecommerce.db` file
3. Run seed script again:
   ```bash
   python seed_data.py
   ```

---

### Issue: "CORS error" in browser console

**Problem**: Frontend can't connect to backend

**Solutions**:
1. Verify backend is running on `http://localhost:8000`
2. Check CORS settings in `main.py`
3. Clear browser cache
4. Try different browser

---

## ⚛️ Frontend Issues

### Issue: "npm: command not found"

**Problem**: Node.js is not installed

**Solutions**:
1. Install Node.js 14+ from [nodejs.org](https://nodejs.org)
2. Verify installation: `node --version` and `npm --version`
3. Restart terminal after installation

---

### Issue: "Port 3000 already in use"

**Problem**: Another app is using port 3000

**Solutions**:
1. When prompted, type 'Y' to use different port
2. Or kill the process:
   ```bash
   # Windows
   netstat -ano | findstr :3000
   taskkill /PID <PID> /F
   
   # macOS/Linux
   lsof -ti:3000 | xargs kill -9
   ```

---

### Issue: "Module not found" errors

**Problem**: Dependencies not installed

**Solutions**:
1. Delete `node_modules` folder
2. Delete `package-lock.json`
3. Reinstall:
   ```bash
   npm install
   ```

---

### Issue: "Failed to fetch" or "Network Error"

**Problem**: Can't connect to backend API

**Solutions**:
1. Verify backend is running: `http://localhost:8000`
2. Check backend terminal for errors
3. Verify API_URL in `App.js`: `const API_URL = 'http://localhost:8000';`
4. Check browser console (F12) for detailed errors

---

### Issue: Blank page or white screen

**Problem**: JavaScript error or build issue

**Solutions**:
1. Open browser console (F12) and check for errors
2. Clear browser cache (Ctrl+Shift+Delete)
3. Rebuild the app:
   ```bash
   npm start
   ```
4. Try incognito/private browsing mode

---

## 🗄️ Database Issues

### Issue: "No recommendations showing"

**Problem**: Database not seeded or no user interactions

**Solutions**:
1. Verify database exists: Look for `ecommerce.db` in backend folder
2. Reseed database:
   ```bash
   cd backend
   python seed_data.py
   ```
3. Select a different user from dropdown
4. Add some interactions first (view/cart/wishlist products)

---

### Issue: "User not found" error

**Problem**: Database is empty or user doesn't exist

**Solutions**:
1. Run seed script: `python seed_data.py`
2. Check if database file exists
3. Verify users exist: Visit `http://localhost:8000/users`

---

## 🔐 Environment Issues

### Issue: ".env file not found"

**Problem**: Environment file doesn't exist

**Solutions**:
1. Copy example file:
   ```bash
   cd backend
   copy .env.example .env  # Windows
   cp .env.example .env    # macOS/Linux
   ```
2. Edit `.env` and add your API key (optional)

---

### Issue: "Environment variables not loading"

**Problem**: .env file not being read

**Solutions**:
1. Verify `.env` file is in `backend/` directory
2. Check file format (no spaces around =):
   ```
   OPENAI_API_KEY=sk-your-key
   DATABASE_URL=sqlite:///./ecommerce.db
   ```
3. Restart backend server

---

## 🌐 Browser Issues

### Issue: "CORS policy blocked"

**Problem**: Browser security blocking requests

**Solutions**:
1. Ensure backend has CORS enabled (check `main.py`)
2. Use same protocol (both http, not mixing http/https)
3. Clear browser cache
4. Try different browser

---

### Issue: Images not loading

**Problem**: External image URLs blocked or unavailable

**Solutions**:
1. Check internet connection
2. Verify image URLs in database
3. Some URLs may require HTTPS
4. Replace with local images if needed

---

## 💻 General Issues

### Issue: "Permission denied"

**Problem**: Insufficient permissions

**Solutions**:
1. Run terminal as administrator (Windows)
2. Use `sudo` for macOS/Linux (if needed)
3. Check file permissions
4. Ensure you own the project directory

---

### Issue: Slow recommendations

**Problem**: Large dataset or slow LLM API

**Solutions**:
1. Reduce number of recommendations
2. Disable LLM (remove API key for faster fallback)
3. Add caching (future enhancement)
4. Optimize database queries

---

### Issue: "Virtual environment not activating"

**Problem**: Virtual environment setup issue

**Solutions**:

**Windows**:
```bash
# PowerShell execution policy
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Then activate
venv\Scripts\activate
```

**macOS/Linux**:
```bash
# Ensure script is executable
chmod +x venv/bin/activate

# Then activate
source venv/bin/activate
```

---

## 🧪 Testing Issues

### Issue: "Can't test recommendations"

**Problem**: Need user interactions first

**Solutions**:
1. Go to "All Products" tab
2. Click "View", "Cart", or "Wishlist" on several products
3. Go back to "Recommendations" tab
4. Click refresh button

---

### Issue: "Same recommendations every time"

**Problem**: Not enough interaction diversity

**Solutions**:
1. Interact with different product categories
2. Try different interaction types
3. Switch users to see different profiles
4. Add more products to database

---

## 📊 Performance Issues

### Issue: Slow API responses

**Problem**: Inefficient queries or large dataset

**Solutions**:
1. Check backend terminal for slow queries
2. Reduce `num_recommendations` parameter
3. Add database indexes (future enhancement)
4. Use caching

---

### Issue: High memory usage

**Problem**: Large data processing

**Solutions**:
1. Limit number of products/users
2. Optimize recommendation algorithms
3. Clear browser cache
4. Restart servers

---

## 🔍 Debugging Tips

### Enable Debug Mode

**Backend**:
Add to `main.py`:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

**Frontend**:
Check browser console (F12) for:
- Network requests
- JavaScript errors
- API responses

### Check Logs

**Backend logs**: Look at terminal running `python main.py`
**Frontend logs**: Browser console (F12)
**Network logs**: Browser DevTools > Network tab

### Test API Directly

Visit `http://localhost:8000/docs` to test endpoints without frontend

### Verify Data

Check database contents:
```bash
cd backend
python
>>> from database import SessionLocal
>>> from models import Product, User
>>> db = SessionLocal()
>>> products = db.query(Product).all()
>>> print(len(products))
>>> users = db.query(User).all()
>>> print(len(users))
```

---

## 🆘 Still Having Issues?

1. **Read error messages carefully** - They often tell you exactly what's wrong
2. **Check all terminals** - Backend and frontend logs
3. **Verify prerequisites** - Python 3.8+, Node.js 14+
4. **Start fresh** - Delete venv, node_modules, and reinstall
5. **Review setup guide** - Follow `SETUP_GUIDE.md` step by step

## 📝 Common Error Messages

| Error | Likely Cause | Quick Fix |
|-------|--------------|-----------|
| `ModuleNotFoundError` | Missing dependency | `pip install -r requirements.txt` |
| `EADDRINUSE` | Port in use | Kill process or use different port |
| `404 Not Found` | Backend not running | Start backend server |
| `CORS error` | Backend/frontend mismatch | Check both servers running |
| `Database locked` | Multiple connections | Restart backend |
| `Invalid API key` | Wrong OpenAI key | Check `.env` file |

---

## 💡 Prevention Tips

1. **Always activate virtual environment** before running backend
2. **Keep both servers running** while using the app
3. **Check both terminals** for errors
4. **Use the batch files** (`run.bat`) for easier startup
5. **Read documentation** before making changes

---

**Most issues can be solved by restarting both servers! 🔄**
