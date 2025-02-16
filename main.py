from fastapi import FastAPI, Request, Query
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse

app = FastAPI()

# Подключаем шаблоны и статику
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "D&D Assistant"})

@app.get("/pers")
async def home(request: Request):
    return templates.TemplateResponse("pers.html", {"request": request, "title": "D&D pers create"})

@app.get("/saved")
async def home(request: Request):
    return templates.TemplateResponse("saved.html", {"request": request, "title": "D&D pers saved"})

@app.get("/adventure")
async def home(request: Request):
    return templates.TemplateResponse("adventure.html", {"request": request, "title": "D&D adventure"})

@app.get("/dice")
async def home(request: Request):
    return templates.TemplateResponse("dice.html", {"request": request, "title": "D&D dice"})
