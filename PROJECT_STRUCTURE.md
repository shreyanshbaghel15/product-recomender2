# 📁 Project Structure

Complete overview of the E-commerce Product Recommender project structure.

```
ecommerce-recommender/
│
├── backend/                          # Backend API (FastAPI)
│   ├── venv/                        # Virtual environment (created after setup)
│   ├── __pycache__/                 # Python cache (auto-generated)
│   │
│   ├── main.py                      # 🚀 Main FastAPI application
│   ├── database.py                  # 💾 Database configuration & session
│   ├── models.py                    # 📊 SQLAlchemy database models
│   ├── schemas.py                   # 📋 Pydantic schemas for validation
│   ├── recommender.py               # 🤖 Recommendation engine logic
│   ├── llm_service.py               # 🧠 LLM integration (OpenAI)
│   ├── seed_data.py                 # 🌱 Database seeding script
│   │
│   ├── requirements.txt             # 📦 Python dependencies
│   ├── .env                         # 🔐 Environment variables (create from .env.example)
│   ├── .env.example                 # 📝 Example environment file
│   ├── .gitignore                   # 🚫 Git ignore patterns
│   ├── run.bat                      # ▶️ Windows startup script
│   └── ecommerce.db                 # 💿 SQLite database (created after seeding)
│
├── frontend/                         # Frontend Application (React)
│   ├── node_modules/                # Node packages (created after npm install)
│   ├── public/                      # Public static files
│   │   └── index.html               # 📄 HTML template
│   │
│   ├── src/                         # Source code
│   │   ├── App.js                   # 🎨 Main React component
│   │   ├── App.css                  # 💅 Application styles
│   │   ├── index.js                 # 🚀 React entry point
│   │   └── index.css                # 🎨 Global styles
│   │
│   ├── package.json                 # 📦 Node dependencies & scripts
│   ├── package-lock.json            # 🔒 Locked dependency versions
│   ├── run.bat                      # ▶️ Windows startup script
│   └── build/                       # Production build (created after npm run build)
│
├── README.md                         # 📖 Main documentation
├── SETUP_GUIDE.md                   # 🛠️ Detailed setup instructions
├── START_HERE.md                    # 🚀 Quick start guide
├── API_DOCUMENTATION.md             # 📡 API reference
├── PROJECT_STRUCTURE.md             # 📁 This file
├── LICENSE                          # ⚖️ MIT License
└── .gitignore                       # 🚫 Git ignore patterns
```

## 📂 Directory Breakdown

### Backend (`/backend`)

#### Core Application Files

| File | Purpose | Key Features |
|------|---------|--------------|
| `main.py` | FastAPI application | API endpoints, CORS, routing |
| `database.py` | Database setup | SQLAlchemy engine, session management |
| `models.py` | Database models | Product, User, UserInteraction tables |
| `schemas.py` | Data validation | Pydantic models for request/response |
| `recommender.py` | Recommendation engine | Collaborative & content-based filtering |
| `llm_service.py` | LLM integration | OpenAI API, explanation generation |
| `seed_data.py` | Data seeding | Sample products, users, interactions |

#### Configuration Files

| File | Purpose |
|------|---------|
| `requirements.txt` | Python package dependencies |
| `.env` | Environment variables (API keys, config) |
| `.env.example` | Template for environment variables |
| `run.bat` | Automated Windows startup script |

#### Generated Files

| File | Created By | Purpose |
|------|------------|---------|
| `ecommerce.db` | `seed_data.py` | SQLite database |
| `venv/` | `python -m venv venv` | Virtual environment |
| `__pycache__/` | Python | Compiled bytecode |

### Frontend (`/frontend`)

#### Source Files

| File | Purpose | Key Features |
|------|---------|--------------|
| `src/App.js` | Main component | UI logic, API calls, state management |
| `src/App.css` | Component styles | Modern design, responsive layout |
| `src/index.js` | Entry point | React initialization |
| `src/index.css` | Global styles | Base styles, gradients |

#### Configuration Files

| File | Purpose |
|------|---------|
| `package.json` | Node dependencies, scripts |
| `public/index.html` | HTML template |
| `run.bat` | Automated Windows startup script |

#### Generated Files

| Directory | Created By | Purpose |
|-----------|------------|---------|
| `node_modules/` | `npm install` | Node packages |
| `build/` | `npm run build` | Production build |

### Root Files

| File | Purpose |
|------|---------|
| `README.md` | Complete project documentation |
| `SETUP_GUIDE.md` | Step-by-step setup instructions |
| `START_HERE.md` | Quick start guide |
| `API_DOCUMENTATION.md` | API endpoint reference |
| `PROJECT_STRUCTURE.md` | This file - project overview |
| `LICENSE` | MIT License |
| `.gitignore` | Git ignore patterns |

## 🔄 Data Flow

```
┌─────────────┐
│   Browser   │
│  (React UI) │
└──────┬──────┘
       │
       │ HTTP Requests
       │
┌──────▼──────────────────────────────┐
│      FastAPI Backend (main.py)      │
├─────────────────────────────────────┤
│  ┌─────────────────────────────┐   │
│  │   API Endpoints             │   │
│  │  - /products                │   │
│  │  - /users                   │   │
│  │  - /interactions            │   │
│  │  - /recommendations         │   │
│  └────────┬────────────────────┘   │
│           │                         │
│  ┌────────▼────────────────────┐   │
│  │  Recommender Engine         │   │
│  │  (recommender.py)           │   │
│  │  - Collaborative Filtering  │   │
│  │  - Content-Based Filtering  │   │
│  │  - Hybrid Recommendations   │   │
│  └────────┬────────────────────┘   │
│           │                         │
│  ┌────────▼────────────────────┐   │
│  │  LLM Service                │   │
│  │  (llm_service.py)           │   │
│  │  - Generate Explanations    │   │
│  │  - OpenAI Integration       │   │
│  └────────┬────────────────────┘   │
│           │                         │
│  ┌────────▼────────────────────┐   │
│  │  Database Layer             │   │
│  │  (models.py, database.py)   │   │
│  └────────┬────────────────────┘   │
└───────────┼─────────────────────────┘
            │
    ┌───────▼────────┐
    │  SQLite DB     │
    │ (ecommerce.db) │
    └────────────────┘
```

## 🎯 Component Responsibilities

### Backend Components

#### `main.py` - API Layer
- Defines all HTTP endpoints
- Handles request/response
- CORS configuration
- Error handling

#### `recommender.py` - Business Logic
- Collaborative filtering algorithm
- Content-based filtering algorithm
- Hybrid recommendation strategy
- User behavior analysis

#### `llm_service.py` - AI Integration
- OpenAI API communication
- Prompt engineering
- Fallback explanations
- Error handling

#### `models.py` - Data Layer
- Database table definitions
- Relationships between tables
- Data constraints

#### `schemas.py` - Validation Layer
- Request validation
- Response serialization
- Type checking

### Frontend Components

#### `App.js` - UI Logic
- State management
- API integration
- User interactions
- Tab navigation

#### `App.css` - Styling
- Modern design system
- Responsive layout
- Animations
- Color scheme

## 📊 Database Schema

```sql
┌─────────────────┐
│    products     │
├─────────────────┤
│ id (PK)         │
│ name            │
│ description     │
│ category        │
│ price           │
│ image_url       │
│ rating          │
│ tags            │
└────────┬────────┘
         │
         │ 1:N
         │
┌────────▼────────────┐
│ user_interactions   │
├─────────────────────┤
│ id (PK)             │
│ user_id (FK)        │
│ product_id (FK)     │
│ interaction_type    │
│ rating              │
│ timestamp           │
└────────┬────────────┘
         │
         │ N:1
         │
┌────────▼────────┐
│     users       │
├─────────────────┤
│ id (PK)         │
│ username        │
│ email           │
│ preferences     │
└─────────────────┘
```

## 🚀 Startup Sequence

### Backend Startup
1. Load environment variables (`.env`)
2. Initialize database connection
3. Create tables if not exist
4. Start FastAPI application
5. Enable CORS
6. Initialize LLM service
7. Listen on port 8000

### Frontend Startup
1. Load React application
2. Initialize state
3. Fetch users from API
4. Fetch products from API
5. Render UI
6. Listen on port 3000

## 🔧 Configuration Files

### Backend Configuration
- `.env` - API keys, database URL
- `requirements.txt` - Python packages

### Frontend Configuration
- `package.json` - Node packages, scripts
- React environment variables (optional)

## 📦 Dependencies

### Backend (Python)
- **FastAPI**: Web framework
- **Uvicorn**: ASGI server
- **SQLAlchemy**: ORM
- **Pydantic**: Data validation
- **OpenAI**: LLM integration
- **Scikit-learn**: ML algorithms
- **Pandas/NumPy**: Data processing

### Frontend (JavaScript)
- **React**: UI library
- **Axios**: HTTP client
- **React Scripts**: Build tools

## 🎨 Design Patterns

### Backend
- **Repository Pattern**: Database access
- **Service Layer**: Business logic
- **Dependency Injection**: Database sessions
- **Factory Pattern**: LLM service initialization

### Frontend
- **Component-Based**: React components
- **State Management**: React hooks
- **Separation of Concerns**: Logic vs. presentation

## 🔐 Security Considerations

- API keys in environment variables
- CORS configuration
- Input validation with Pydantic
- SQL injection prevention (SQLAlchemy)

## 📈 Scalability

### Current Architecture
- Single server
- SQLite database
- Synchronous processing

### Future Improvements
- PostgreSQL/MySQL for production
- Redis for caching
- Async processing
- Load balancing
- Microservices architecture

---

This structure provides a solid foundation for an AI-powered e-commerce recommendation system!
