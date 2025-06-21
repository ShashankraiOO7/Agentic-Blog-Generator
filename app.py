import os
from dotenv import load_dotenv
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from src.ai_blog.crew import BlogCrew

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
model = os.getenv("MODEL")
if not api_key or not model:
    raise RuntimeError("⚠️ Ensure GEMINI_API_KEY and MODEL are defined in .env")
print("✅ Using Gemini model:", model)

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "generated": None})

@app.post("/generate", response_class=HTMLResponse)
async def generate_blog(request: Request, topic: str = Form(...)):
    try:
        result = BlogCrew().crew().kickoff(inputs={"topic": topic})
    except Exception as e:
        result = f"❌ Error: {e}"
    return templates.TemplateResponse("index.html", {
        "request": request,
        "generated": result,
        "topic": topic
    })
