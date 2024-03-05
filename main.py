from fastapi import FastAPI, File, UploadFile
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse
from app import speech_recognition
import tempfile

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/lenfile")
async def lenfile(file: bytes = File(...)):
    return {"file_size": len(file)}


@app.post("/transcribe/")
async def transcribe_audio(file: UploadFile = File(...)):
    if not file:
        raise HTTPException(status_code=400, detail="No file provided")

    results = []

    with tempfile.NamedTemporaryFile(delete=True) as temp_audio:
        with open(temp_audio.name, "wb") as audio_file:
            audio_file.write(file.file.read())

        # Load the Whisper model
        result = speech_recognition.transcribe(speech_recognition.load_model(), temp_audio.name)
        results.append(
            {
                "file_name": file.filename,
                "transcription": result,
            }
        )

    return JSONResponse(content={"results": results})
