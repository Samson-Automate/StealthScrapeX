import random
import os
from dotenv import load_dotenv

load_dotenv()

proxy_env = os.getenv("PROXIES")

if proxy_env:
    PROXIES = proxy_env.split(",")
else:
    PROXIES = [None]

def get_random_proxy():
    return random.choice(PROXIES)
import logging

logging.basicConfig(
    filename="data/logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger()