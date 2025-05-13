import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

templates=Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))


@app.get("/",response_class=HTMLResponse)
def read_root(request: Request):
    print(request.headers)
    return templates.TemplateResponse("home.html", {"request": request, "name": "Daarin!"})
        


@app.post("/")
def root_post():
    return {"Hello": "World"}