# 🚀 Advanced Stealth Web Scraper

![Banner](assets/banner.png)

A powerful, production-ready web scraping system built with **FastAPI, Playwright, and Redis**.

---

# 🧠 Features

✅ Headless browser scraping (Playwright)  
✅ Background job processing (Redis + Worker)  
✅ Retry system (auto-retry on failure)  
✅ Proxy support (optional)  
✅ Logging system (file-based logs)  
✅ Scalable architecture (multiple workers)  

---

# 📸 API Preview

![API Docs](assets/api-docs.png)

---

# 🏗️ Architecture

![Architecture](assets/architecture.png)

Flow:

```
Client → FastAPI → Redis Queue → Worker → Scraper → Output
```

---

# 📁 Project Structure

```
stealth_scraper/
│
├── app/
│   ├── main.py
│   ├── scraper.py
│   ├── queue.py
│   ├── utils.py
│
├── workers/
│   └── worker.py
│
├── data/
│   ├── output.json
│   └── logs.txt
│
├── assets/
│
├── .env
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone

```
git clone https://github.com/your-username/stealth_scraper.git
cd stealth_scraper
```

---

## 2️⃣ Install dependencies

```
py -m pip install -r requirements.txt
```

---

## 3️⃣ Install Playwright

```
py -m playwright install
```

---

## 4️⃣ Install & Run Redis

Run:

```
redis-server
```

---

# 🔐 Environment Setup

Create `.env` file:

```
PROXIES=
```

---

# ▶️ Run Project

## 🟢 Start API

```
py -m uvicorn app.main:app --reload
```

---

## 🔵 Start Worker

Open another terminal:

```
py -m workers.worker
```

---

## 🌐 Open Docs

```
http://127.0.0.1:8000/docs
```

---

## 🚀 Run Scraper

1. Open `/scrape`
2. Click "Try it out"
3. Enter URL:

```
https://example.com
```

4. Click Execute

---

# 📊 Output

Saved in:

```
data/output.json
```

Example:

```
{"url": "https://example.com", "title": "Example Domain", "proxy": null}
```

---

# 🧾 Logs

Saved in:

```
data/logs.txt
```

Example:

```
INFO - Opening: https://example.com
INFO - Scraped Title: Example Domain
```

---

# 🔁 Retry System

- Automatically retries on failure  
- Prevents crashes  
- Improves reliability  

---

# 🌐 Proxy Support (Optional)

You can add proxies using a `.env` file:

```
PROXIES=http://user:pass@proxy1:port,http://user:pass@proxy2:port
```

If not provided, the scraper will run without proxies.

---

# ⚡ Scaling

Run multiple workers:

```
py -m workers.worker
py -m workers.worker
py -m workers.worker
```

---

# ⚠️ Notes

- Redis must be running  
- Do not upload `.env` to GitHub  
- Free proxies may fail  
- Use paid proxies for production  

---

# 🏆 Conclusion

This project demonstrates:

- Real-world backend system  
- Distributed job processing  
- Scalable scraping architecture  

---

# 📬 Contact

Feel free to connect 🚀
