
from fastapi import FastAPI, HTTPException
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

@app.delete("/volunteers/{volunteer_index}")
def delete_volunteer(volunteer_index: int):
    if volunteer_index < 0 or volunteer_index >= len(volunteers):
        raise HTTPException(status_code=404, detail="Volunteer not found")

    volunteers.pop(volunteer_index)
    return {"message": "Volunteer deleted!"}
