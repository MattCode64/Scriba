import whisper
from pydub import AudioSegment


def load_audio_file(audio_path):
    audio = AudioSegment.from_mp3(audio_path)
    return audio.raw_data


def transcribe(model, audio):
    options = {
        "language": "fr",  # Specify the French language
    }
    print("Transcribing audio...")
    text_transcribe = model.transcribe(audio, **options, fp16=False, verbose=True)
    return text_transcribe["text"]


def save_transcription(transcription, file_path="../transcription.txt"):
    print("Saving transcription...")
    with open(file_path, "w", encoding='utf-8') as txt_file:
        txt_file.write(transcription)


def main():
    whisper_model = whisper.load_model("base")
    audio_path = "../audiotest.mp3"
    load_audio_file(audio_path)
    save_transcription(transcribe(whisper_model, audio_path))


if __name__ == '__main__':
    main()
