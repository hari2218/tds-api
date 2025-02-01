from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from fastapi.responses import JSONResponse
import json

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from any origin
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)


def load_marks():
    with open("q-vercel-python.json", "r") as file:
        return json.load(file)


@app.get("/api")
async def get_marks(name: List[str]):
    student_marks = load_marks()
    marks = [student_marks[n] for n in name]
    return JSONResponse(content={"marks": marks})
