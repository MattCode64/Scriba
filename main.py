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


@app.post("/transcribe")
def transcribe_audio(file: UploadFile = File(...)):
    with NamedTemporaryFile(delete=False) as temp_audio:
        shutil.copyfileobj(file.file, temp_audio)

    audio = speech_recognition.load_audio_file(temp_audio.name)

    transcription = speech_recognition.transcribe(audio)

    transcript_file_path = NamedTemporaryFile(delete=False, suffix=".txt").name

    speech_recognition.save_transcription(transcription, transcript_file_path)

    return FileResponse(path=transcript_file_path, filename="transcription.txt", media_type='text/plain')
