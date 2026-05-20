from fastapi import FastAPI
from app.queue import add_job

app = FastAPI()

# Health Check Endpoint 
@app.get("/")
def health():
    return {"status": "running"}

# Scrape Endpoint
@app.post("/scrape")
def scrape_url(url: str):
    add_job(url)
    return {
        "message": "URL added to queue",
        "url": url,
        "status": "processing"
    }
