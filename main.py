from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import json
from typing import List

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
async def get_marks(name: List[str] = Query(...)):
    student_marks = load_marks()
    # Create a lookup dictionary for faster search
    marks_lookup = {entry["name"]: entry["marks"] for entry in student_marks}

    # Retrieve marks for requested names
    marks = [marks_lookup.get(n, 0) for n in name]

    return JSONResponse(content={"marks": marks})
