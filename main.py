from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="src/"))



@app.get("/")
def root():
    return FileResponse("src/html/index.html")

#
@app.post("/file/upload-file")
def upload_file(file: bytes = File()):
    print(file)
    return file