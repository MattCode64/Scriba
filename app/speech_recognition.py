import whisper
from pydub import AudioSegment


# Load audio file
def load_audio_file(audio_path):
    audio = AudioSegment.from_mp3(audio_path)
    return audio


# Function to convert the audio format mp4 or mp3 to wav depending on the user's input
def convert_to_wav(source_path, destination_path):
    if source_path.endswith('.mp3'):
        audio = AudioSegment.from_mp3(source_path)
    elif source_path.endswith('.mp4'):
        audio = AudioSegment.from_file(source_path, 'mp4')
    else:
        raise ValueError("Le format du fichier source n'est pas supporté.")
    audio.export(destination_path, format='wav')


def transcribe(model, audio):
    options = {
        "language": "fr",  # Specify the French language
    }
    print("Transcribing audio...")
    text_transcribe = model.transcribe(audio, **options, fp16=False, verbose=True)
    return text_transcribe["text"]


def save_transcription(transcription, file_path="transcription.txt"):
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
