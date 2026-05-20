import redis
import json

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

def add_job(url):
    job = {"url": url}
    r.lpush("scrape_queue", json.dumps(job))

def get_job():
    job = r.rpop("scrape_queue")
    return json.loads(job) if job else None
