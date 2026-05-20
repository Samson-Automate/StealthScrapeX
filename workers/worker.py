from app.scraper import scrape
from app.queue import get_job
import json
import time

while True:
    job = get_job()

    if job:
        print("Processing:", job["url"])

        result = scrape(job["url"])

        with open("data/output.json", "a") as f:
            f.write(json.dumps(result) + "\n")

        print("Done:", result)

    else:
        time.sleep(2)