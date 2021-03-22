# from pickle import load
from os import read
from fastapi import FastAPI, File, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
from fastai.vision.all import Path
import uvicorn

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory='templates')

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse('index.html', context={'request': request})


# @app.post("/files/")
# async def create_file(file: bytes = File(...)):
#     return {"file_size": len(file)}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    print(file.filename)
    
    if 'image' in file.content_type:
        contents = await file.read()

        with open(Path.cwd()/f"static/images/{file.filename}", 'wb') as f:
            f.write(contents)
        
    return {"File": file.filename}
