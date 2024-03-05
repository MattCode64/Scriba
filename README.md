# SCRIBA

This is a backend API developed using FastAPI and Python. It includes an endpoint for transcribing audio files.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python
- pip
- FastAPI

### Installing

A step by step series of examples that tell you how to get a development environment running.

```bash
pip install fastapi
pip install uvicorn[standard]
```

### Running the Application

To run the application, execute the following command:

```bash
uvicorn main:app --reload
```

## API Endpoints

- GET /: Returns a welcome message
- POST /transcribe: Transcribes an audio file and returns the text

## Built With

- [FastAPI](https://fastapi.tiangolo.com/) - The web framework used
- [Python](https://www.python.org/) - The programming language used

## Authors

- **Matthieu F**