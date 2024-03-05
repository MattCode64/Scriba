from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from app import speech_recognition
import shutil
from tempfile import NamedTemporaryFile

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
