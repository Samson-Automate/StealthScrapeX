# 🚀 StealthScrapeX — Advanced Stealth Web Scraper

![Banner](assets/banner.png)

A powerful, production-ready web scraping system built with **FastAPI, Playwright, and Redis**.

---

## 🧠 Features

✅ Headless browser scraping (Playwright)  
✅ Background job processing (Redis + Worker)  
✅ Retry system (auto-retry on failure)  
✅ Proxy support (optional)  
✅ Logging system (file-based logs)  
✅ Scalable architecture (multiple workers)  

---

# 🏗️ System Architecture

![Architecture](assets/architecture.png)

👉 High-level workflow showing how requests move through FastAPI → Redis → Worker → Scraper → Output.

---

# 📸 API (FastAPI Swagger UI)

![API Docs](assets/api-docs.png)

👉 Interactive API where users can send scraping requests easily.

---

# 💻 Worker Execution (Terminal)

![Worker](assets/worker-terminal.png)

👉 Worker continuously listens to Redis queue and processes scraping jobs.

---

# ⚙️ Backend Running (Server Logs)

![Server](assets/server-terminal.png)

👉 FastAPI server handling requests and pushing jobs to Redis queue.

---

# 📁 Project Structure

StealthScrapeX/
│
├── app/
├── workers/
├── data/
├── assets/
├── requirements.txt
└── README.md

---

# ⚙️ Installation

## 1️⃣ Clone Repository

git clone https://github.com/YOUR-USERNAME/StealthScrapeX.git
cd StealthScrapeX

---

## 2️⃣ Install Dependencies

py -m pip install -r requirements.txt

---

## 3️⃣ Install Playwright (IMPORTANT)

py -m playwright install

👉 Without this step, scraper will NOT work ❌

---

## 4️⃣ Run Redis

redis-server

---

# ▶️ Run Project

## 🟢 Start API

py -m uvicorn app.main:app --reload

---

## 🔵 Start Worker

Open another terminal:

py -m workers.worker

---

## 🌐 Open API Docs

http://127.0.0.1:8000/docs

---

## 🚀 Run Scraper

1. Open /scrape  
2. Click "Try it out"  
3. Enter URL:

https://example.com

4. Click Execute  

---

# 📊 Output

Saved in:

data/output.json

---

# 🧾 Logs

Saved in:

data/logs.txt

---

# 🌐 Proxy Support (Optional)

You can add proxies using a .env file:

PROXIES=http://user:pass@proxy1:port,http://user:pass@proxy2:port

If not provided, the scraper will run without proxies.

---

# ⚡ Scaling

py -m workers.worker  
py -m workers.worker  
py -m workers.worker  

---

# ⚠️ Notes

- Redis must be running  
- Do NOT upload .env to GitHub  
- Free proxies may fail  
- Use paid proxies for production  

---

# 🏆 Conclusion

This project demonstrates:

- Real-world backend system  
- Distributed job processing  
- Scalable scraping architecture  

---

## 📬 Contact

- 💼 GitHub: https://github.com/Samson-Automate  
- 💰 Hire Me on Fiverr: https://www.fiverr.com/s/LdrLlwY

---

# ⭐ Support

If you like this project:

👉 Star the repo  
👉 Share on LinkedIn 🚀
