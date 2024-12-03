from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from api import init_db, info, get_all, get_new, get_known, search
from pathlib import Path



templates = Jinja2Templates(directory=Path(__file__).parent / "templates")

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(init_db.router)
app.include_router(info.router)
app.include_router(get_all.router)
app.include_router(get_new.router)
app.include_router(get_known.router)
app.include_router(search.router)



#Головна сторінка
@app.get("/", response_class=HTMLResponse)
def show_start(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})





