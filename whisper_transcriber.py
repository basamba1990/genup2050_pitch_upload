import whisper

def transcribe_audio_local(file_path):
    model = whisper.load_model("base")
    result = model.transcribe(file_path)
    return result["text"]