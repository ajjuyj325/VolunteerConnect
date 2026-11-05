
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

volunteers = []

class Volunteer(BaseModel):
    name: str
    email: str

@app.get("/")
def home():
    return {"message": "Volunteer API is running!"}

@app.get("/volunteers")
def get_volunteers():
    return volunteers

@app.post("/volunteers")
def add_volunteer(volunteer: Volunteer):
    volunteers.append(volunteer.model_dump())
    return {"message": "Volunteer registered!"}
