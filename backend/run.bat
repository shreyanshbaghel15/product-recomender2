@echo off
echo Starting E-commerce Recommender Backend...
echo.

REM Check if virtual environment exists
if not exist "venv\" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
call venv\Scripts\activate

REM Install requirements
echo Installing dependencies...
pip install -r requirements.txt

REM Check if .env exists
if not exist ".env" (
    echo Creating .env file from .env.example...
    copy .env.example .env
    echo.
    echo IMPORTANT: Please edit .env file and add your OPENAI_API_KEY
    echo.
    pause
)

REM Check if database exists
if not exist "ecommerce.db" (
    echo Seeding database...
    python seed_data.py
)

REM Run the server
echo.
echo Starting FastAPI server...
echo API will be available at http://localhost:8000
echo API Documentation at http://localhost:8000/docs
echo.
python main.py
