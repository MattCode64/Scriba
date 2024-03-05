import whisper
import numpy as np
from pydub import AudioSegment


def load_audio_file(audio_path):
    audio = AudioSegment.from_mp3(audio_path)
    samples = np.array(audio.get_array_of_samples())
    if audio.channels == 2:
        samples = samples.reshape((-1, 2))
    return samples.astype(np.float32), audio.frame_rate


def load_model(model_name="base"):
    return whisper.load_model(model_name)


def transcribe(model, audio) -> str:
    options = {
        "language": "fr",  # Specify the French language
    }
    print("Transcribing audio...")
    print(f"Audio type: {type(audio)}")
    text_transcribe = model.transcribe(audio, **options, fp16=False, verbose=True)
    return text_transcribe["text"]


def save_transcription(transcription, file_path="../transcription.txt"):
    print("Saving transcription...")
    with open(file_path, "w", encoding='utf-8') as txt_file:
        txt_file.write(transcription)


def main():
    audio_path = "../audiotest.mp3"
    load_audio_file(audio_path)
    whisper_model = load_model()
    save_transcription(transcribe(whisper_model, audio_path))


if __name__ == '__main__':
    main()
