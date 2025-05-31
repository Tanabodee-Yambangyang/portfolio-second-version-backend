from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import schemas
import json

app = FastAPI()

# CORS settings (allow frontend requests)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # replace with your frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load data from JSON files
def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)

# Routes
@app.get("/")
def read_root():
    return {"message": "Portfolio API is running!"}

@app.get("/profile", response_model=list[schemas.Profile])
def get_experiences():
    return load_json("data.json")