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
