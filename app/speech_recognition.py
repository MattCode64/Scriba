import whisper
import numpy as np
from pydub import AudioSegment


def load_audio_file(audio_path):
    audio = AudioSegment.from_mp3(audio_path)
    # Convertir les données audio en un tableau numpy avec le type float32
    audio_data = np.array(audio.get_array_of_samples(), dtype=np.float32)
    # Normaliser les données audio pour qu'elles soient entre -1.0 et 1.0
    audio_data = audio_data / (2**15)
    # Reshape l'audio pour avoir 1 canal car Whisper s'attend à ce format
    audio_data = audio_data.reshape((-1, 1))
    return audio_data


def load_model(model_name="base"):
    return whisper.load_model(model_name)


def transcribe(model, audio):
    options = {
        "language": "fr",  # Specify the French language
    }
    print("Transcribing audio...")
    text_transcribe = model.transcribe(audio, **options, fp16=False)
    print("Transcription completed!")
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
