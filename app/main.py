from fastapi import FastAPI
from fastapi.responses import FileResponse # 1. Import FileResponse
from app.routes import router
from scheduler import start_scheduler
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(
    title="Healthcare Analytics API",
    description="Predicts patient test results: Normal, Abnormal, or Inconclusive",
    version="1.0.0",
)

# Register routes
app.include_router(router, prefix="/api/v1")

# Start weekly retraining scheduler on startup
@app.on_event("startup")
def startup_event():
    start_scheduler()

# 2. Update the root route to return your HTML file
@app.get("/")
def root():
    html_path = "frontend/index.html"
    
    # Best practice -> checking to ensure the file exists (It does)
    if os.path.exists(html_path):
        return FileResponse(html_path)
    return {"error": "UI file not found. Check your file paths!"}