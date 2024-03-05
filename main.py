from fastapi import FastAPI, File, UploadFile
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse, RedirectResponse
from app import speech_recognition
import tempfile

app = FastAPI()


@app.get("/", response_class=RedirectResponse)
async def redirect_to_docs():
    return "/docs"


@app.post("/transcribe/")
async def transcribe_audio(file: UploadFile = File(...)):
    if not file:
        raise HTTPException(status_code=400, detail="No file provided")

    if not file.filename.endswith(".mp3"):
        raise HTTPException(status_code=400, detail="Only .mp3 files are supported")

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
