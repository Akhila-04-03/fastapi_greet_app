from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/greet", response_class=HTMLResponse)
def greet_user(request: Request, name: str = Form(...)):
    return templates.TemplateResponse("index.html", {"request": request, "message": f"Hello, {name}!"})