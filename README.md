# Sachin Gate — Portfolio (FastAPI)

A production-ready FastAPI web app serving your portfolio page with a live contact form endpoint.

## Project Structure

```
sachin-portfolio/
├── main.py              ← FastAPI app (routes, contact handler)
├── templates/
│   └── index.html       ← Your portfolio page (Jinja2 template)
├── static/              ← Place CSS/JS/images here if needed
├── requirements.txt     ← Python dependencies
├── Procfile             ← Heroku start command
├── render.yaml          ← Render.com auto-deploy config
├── runtime.txt          ← Python version pin (Heroku)
└── .gitignore
```

---

## Run Locally

```bash
# 1. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start the dev server
python main.py
# → Open http://localhost:8000
```

---

## Deploy to Render.com (recommended — free tier)

1. Push this folder to a **GitHub repository**
2. Go to [render.com](https://render.com) → **New → Web Service**
3. Connect your GitHub repo
4. Render auto-detects `render.yaml` — click **Deploy**
5. Your live URL will be `https://sachin-portfolio.onrender.com`

---

## Deploy to Heroku

```bash
# Install Heroku CLI, then:
heroku login
heroku create sachin-portfolio

git init
git add .
git commit -m "initial deploy"

heroku git:remote -a sachin-portfolio
git push heroku main

heroku open
```

---

## Wiring up the Contact Form (Email)

The `/contact` route in `main.py` currently logs form submissions to the console.
To actually send emails, add this to `main.py`:  

```python
import smtplib
from email.mime.text import MIMEText

def send_email(name, email, subject, message):
    msg = MIMEText(f"From: {name} <{email}>\n\n{message}")
    msg["Subject"] = subject or "Portfolio Contact"
    msg["From"]    = "your@gmail.com"
    msg["To"]      = "your@gmail.com"

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login("your@gmail.com", os.environ["GMAIL_APP_PASSWORD"])
        server.send_message(msg)
```

Then set the `GMAIL_APP_PASSWORD` environment variable in Render/Heroku dashboard.

---

## API Endpoints

| Method | Path       | Description                  |
|--------|------------|------------------------------|
| GET    | `/`        | Serves the portfolio page    |
| GET    | `/health`  | Health check (returns JSON)  |
| POST   | `/contact` | Handles contact form submit  |
