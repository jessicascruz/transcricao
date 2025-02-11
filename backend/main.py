from fastapi import FastAPI, HTTPException, Depends
from typing import Optional, List, Dict
from pydantic import BaseModel
from uuid import UUID, uuid4
from fastapi.middleware.cors import CORSMiddleware
from datetime import date

app = FastAPI()

# declare origin/s -> http://127.0.0.1:8000
origins = [
    "http://localhost:5173",
    "localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

d = [
    {"User": "a", "date": date.today(), "count": 1},
    {"User": "b", "date": date.today(), "count": 2},
]

@app.get("/teste")
async def root():
    return d