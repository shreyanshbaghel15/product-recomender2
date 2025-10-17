@echo off
echo Starting E-commerce Recommender Frontend...
echo.

REM Check if node_modules exists
if not exist "node_modules\" (
    echo Installing dependencies...
    call npm install
)

REM Start the development server
echo.
echo Starting React development server...
echo Application will be available at http://localhost:3000
echo.
call npm start
