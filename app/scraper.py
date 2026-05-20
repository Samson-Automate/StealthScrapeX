from playwright.sync_api import sync_playwright
import time
import random
from app.utils import get_random_proxy, logger


def scrape(url, retries=3):
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

                return {
                    "url": url,
                    "title": title,
                    "proxy": proxy
                }

        except Exception as e:
            logger.error(f"Error: {e}")
            logger.info("Retrying...\n")
            time.sleep(2)

    # If all retries fail
    return {
        "url": url,
        "error": "Failed after retries"
    }