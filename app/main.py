from fastapi import FastAPI
from app.queue import add_job

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Scraper running"}

@app.post("/scrape")
def scrape_url(url: str):
    add_job(url)
    return {"status": "added to queue"}