import streamlit as st
import tempfile
from whisper_transcriber import transcribe_audio_local

st.set_page_config(page_title="Pitch Uploader - GENUP2050", layout="centered")
st.title("Pitch Uploader - GENUP2050 (Version Locale Gratuite)")
st.markdown("**Téléverse ta vidéo de pitch** (MP4, MP3, M4A, MOV – max 200MB)")

uploaded_file = st.file_uploader("Drag & drop ou clique pour choisir un fichier", type=["mp4", "mp3", "m4a", "mov"])

if uploaded_file is not None:
    st.success("Vidéo reçue. Transcription en cours...")
    with tempfile.NamedTemporaryFile(delete=False, suffix=uploaded_file.name[-4:]) as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name
    try:
        text = transcribe_audio_local(tmp_path)
        st.subheader("Transcription obtenue :")
        st.text_area("Texte transcrit :", value=text, height=300)
    except Exception as e:
        st.error(f"Une erreur est survenue lors de la transcription : {e}")