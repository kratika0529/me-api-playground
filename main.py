from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from database import USER_DATA

app = FastAPI(title="Kratika's Me-API")

# 1. CORS Configuration (CRUCIAL for Requirement 3b)
# This allows your frontend to talk to your backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. Schema Definition [Requirement 1a]
class ProfileUpdate(BaseModel):
    name: str
    email: str
    education: str
    skills: List[str]

# 3. Health Check [Requirement 1c / Acceptance Criteria]
@app.get("/health")
def health_check():
    return {"status": "healthy"} # Returns 200 status code

# 4. Profile Operations [Requirement 1a]
@app.get("/profile")
def get_profile():
    return USER_DATA["profile"]

@app.put("/profile")
def update_profile(updated_data: ProfileUpdate):
    # Changed .dict() to .model_dump() for Pydantic V2 compatibility
    USER_DATA["profile"].update(updated_data.model_dump())
    return {"message": "Profile updated successfully", "data": USER_DATA["profile"]}

# 5. Query & Search Endpoints [Requirement 1b]
@app.get("/projects")
def get_projects(skill: str = None):
    if skill:
        filtered = [p for p in USER_DATA["projects"] if skill.lower() in [s.lower() for s in p["skills"]]]
        return filtered
    return USER_DATA["projects"]

@app.get("/search")
def search(q: str):
    q = q.lower()
    results = [p for p in USER_DATA["projects"] if q in p["title"].lower() or q in p["description"].lower()]
    return {"results": results}

@app.get("/skills/top")
def get_top_skills():
    # Returns top 3 skills as a specialized query
    return {"top_skills": USER_DATA["profile"]["skills"][:3]}