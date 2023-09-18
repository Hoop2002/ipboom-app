from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi import Form
from typing import Annotated
from app.geocomvert import geo_convert





app = FastAPI()
app.mount("/static", StaticFiles(directory="src/"))



@app.get("/")
def root():
    return FileResponse("src/html/index.html")

#
@app.post("/geoconvert")
def geo_convert_url(key: str = None, file: bytes = File()):
    print(key)
    print(len(file))
    geo_convert(api_key=key, file=file)
    return {"status_1": "12"}