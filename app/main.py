from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/ui", StaticFiles(directory="ui"), name="ui")


@app.get("/")
def get_home():
    return "Hello World"


@app.get("/favicon.ico")
def get_favicon():
    return FileResponse("ui/images/favicon.ico")
