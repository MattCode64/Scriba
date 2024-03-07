# SCRIBA

## Description

SCRIBA is a web application that transcribes audio files. It supports .mp3 files and provides the transcription results in a user-friendly interface.

## Technologies Used

- Python
- Whisper (OpenAI's Speech-to-Text API)
- FastAPI
- Vue.js

## Installation

### Backend

1. Navigate to the backend directory.
2. Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

3. Run the FastAPI server:

```bash
uvicorn main:app --reload
```

### Frontend

1. Navigate to the frontend directory.
2. Install the required Node.js packages using npm:

```bash
npm install
```

3. Run the Vue.js server:

```bash
npm run serve
```

## Usage

1. Open the web application in your browser.
2. Upload an audio file.
3. Wait for the transcription to complete.

## Authors

- [Matthieu F](https://www.linkedin.com/in/matthieu-freire/)