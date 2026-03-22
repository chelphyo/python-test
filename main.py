from fastapi import FastAPI
from pydantic import BaseModel
from personal_details_service import read_people, create_person

app = FastAPI()

class PersonalDetailsCreate(BaseModel):
    first_name: str
    last_name: str
    email: str

@app.get("/")
def home():
    return {"message": "API is running"}

@app.get("/personal-details")
def get_personal_details():
    rows = read_people()
    
    result = []
    for row in rows:
        result.append({
            "id": row[0],
            "first_name": row[1],
            "last_name": row[2],
            "email": row[3]
        })
    return result

@app.post("/personal-details")
def add_person(person: PersonalDetailsCreate):
    new_id = create_person(person.first_name, person.last_name, person.email)

    return {
        "message": "Record created successfully",
        "id": new_id
    }