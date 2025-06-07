from fastapi import FastAPI
from typing import List

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Narrative Watcher API is live"}

@app.get("/headlines")
def get_headlines():
    return [
        {"title": "Economic Crisis Worsens", "category": "Economy"},
        {"title": "New AI Regulation Passed", "category": "Tech"}
    ]

@app.get("/category/{name}")
def get_by_category(name: str):
    return {
        "category": name,
        "headlines": [f"Sample headline in {name}", f"Another example in {name}"]
    }
