from fastapi import FastAPI , Request
import pathlib # like os
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


Base_Dir = pathlib.Path(__file__).parent

app = FastAPI()
templates = Jinja2Templates(directory=str(Base_Dir / "templates"))

@app.get("/", response_class=HTMLResponse)#
def home_view(request :Request):
    print(request)
    return  templates.TemplateResponse({"request":request ,"yassine":2004},"home.html")#<"<h1>Hello world</h1>" # in case you put a json file an error willpop up cue he expecting string html header
"""
    a error that i've faced is :
     Replace `TemplateResponse(name, {"request": request})` by `TemplateResponse(request, name)`.
    warnings.warn()
    and thefix just change the  home.html the secand params
"""
@app.post("/")
def home_detaal_view():
    return {"hello":"world"}
