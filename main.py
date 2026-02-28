from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI(title="Sachin Gate — Portfolio")

# Mount static files only if the directory exists (avoids crash on Render)
static_dir = "static"
if os.path.isdir(static_dir):
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Jinja2 templates
templates = Jinja2Templates(directory="templates")


# ── Routes ────────────────────────────────────────────────────────────────────

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Serve the portfolio homepage."""
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/health")
async def health():
    """Health check — used by Render/Heroku to verify the app is running."""
    return {"status": "ok", "service": "sachin-portfolio"}


@app.post("/contact")
async def contact(
    request: Request,
    first_name: str = Form(...),
    last_name: str = Form(""),
    email: str = Form(...),
    subject: str = Form(""),
    message: str = Form(...),
):
    """
    Handle contact form submissions.
    Currently logs the submission — plug in SendGrid / SMTP / Slack webhook here.
    """
    print(f"[Contact Form] From: {first_name} {last_name} <{email}>")
    print(f"  Subject : {subject}")
    print(f"  Message : {message}")

    return JSONResponse({"success": True, "message": "Thanks! I'll be in touch soon."})


# ── Entry point (local dev) ───────────────────────────────────────────────────

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)