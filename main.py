from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi import Form
from typing import Annotated
from app.geocomvert import geo_convert

import os




app = FastAPI()
app.mount("/static", StaticFiles(directory="src/"))



@app.get("/")
def root():
    return FileResponse("src/html/index.html")

#
@app.post("/geoconvert")
def geo_convert_url(key: str = None, file: bytes = File()):
    file_path = geo_convert(api_key=key, file=file)
    return {'file_path': file_path}

@app.get("/file/geoconvert/{file}")
def get_geoconvert_file(file: str):
    return FileResponse(f"src/result_files/{file}")