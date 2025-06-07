from fastapi import FastAPI, Query
from typing import Optional
import os
import json
app = FastAPI()

def load_headlines_by_category(category_filter=None):
    data_dir = "data/processed"
    headlines = []

    for filename in os.listdir(data_dir):
        if filename.endswith(".json"):
            file_path = os.path.join(data_dir, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                try:
                    items = json.load(f)
                    if category_filter:
                        items = [item for item in items if item.get("category") == category_filter]
                    headlines.extend(items)
                except json.JSONDecodeError as e:
                    print(f"⚠️ Error decoding {filename}: {e}")

    return headlines

@app.get("/")
def read_root():
    return {"message": "Narrative Watcher API is live"}

@app.get("/headlines")
def get_headlines(category: Optional[str] = Query(None)):
    return load_headlines_by_category(category)

@app.get("/category/{name}")
def get_by_category(name: str):
    return {
        "category": name,
        "headlines": [f"Sample headline in {name}", f"Another example in {name}"]
    }

LABELS = [
    # Core mainstream topics
    "Government & Policy", "Civil Rights & Liberties", "Geopolitical Affairs",
    "Economy", "Health", "Technology", "Environment",
    "War", "Crime", "Education", "Science", "Culture",
    "Business", "Entertainment", "Sports", "Opinion",

    # Power & Control themes
    "Surveillance", "Corporate Corruption", "Private Equity",
    "Financial Manipulation", "Wealth Inequality", "Media Bias", "Deep State",
    "Global Elites", "Military Industrial Complex", "Political Coverup",
    "Social Engineering", "BlackRock", "JP Morgan", "Warfare Profiteering",
    "Pharmaceutical Influence", "Censorship", "Disinformation"
]

@app.get("/categories")
def get_categories():
    return LABELS
