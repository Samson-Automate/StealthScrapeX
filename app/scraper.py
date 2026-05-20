from playwright.sync_api import sync_playwright
import time
from datetime import datetime
import random
import os
from app.utils import get_random_proxy, logger

# Auto-create data folder if it doesn't exist
os.makedirs("data", exist_ok=True)
open("data/output.json", "a").close()

def scrape(url, retries=3):
    proxy = None  # safe default

    for attempt in range(retries):
        try:
            proxy = get_random_proxy()

            with sync_playwright() as p:
                launch_options = {
                    "headless": True
                }

                # Apply proxy if available
                if proxy:
                    launch_options["proxy"] = {"server": proxy}

                logger.info(f"[Attempt {attempt+1}] Using proxy: {proxy}")
                logger.info(f"Opening: {url}")

                browser = p.chromium.launch(**launch_options)
                page = browser.new_page()

                page.goto(url, timeout=60000)

                # Human-like delay
                time.sleep(random.uniform(2, 5))

                title = page.title()

                logger.info(f"Scraped Title: {title}")

                browser.close()

                # SUCCESS RETURN
                return {
                    "url": url,
                    "title": title,
                    "timestamp": datetime.now().isoformat(),
                    "proxy": proxy,
                    "status": "success"
                }

        except Exception as e:
            logger.exception("Scraping failed")
            logger.info("Retrying...\n")
            time.sleep(2)

    # FAILED CASE (after retries)
    return {
        "url": url,
        "title": None,
        "timestamp": datetime.now().isoformat(),
        "proxy": proxy,
        "status": "failed"
    }
