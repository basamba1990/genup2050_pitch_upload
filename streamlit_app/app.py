import streamlit as st
import tempfile
from supabase_client import supabase, BUCKET_NAME  # Importer bucket_name défini
from whisper_utils import transcribe_audio

# Configuration de la page
st.set_page_config(page_title="Pitch Uploader - GENUP2050", layout="centered")
st.title("Pitch Uploader - GENUP2050")

# Upload de la vidéo
video_file = st.file_uploader("Téléverse ta vidéo de pitch", type=["mp4", "mov", "m4a", "wav", "mp3"])

if video_file is not None:
    with tempfile.NamedTemporaryFile(delete=False, suffix=video_file.name) as temp_file:
        temp_file.write(video_file.read())
        temp_file_path = temp_file.name

    st.success("Vidéo reçue. Transcription en cours...")

    try:
        # Étape 1 : Transcription
        transcription = transcribe_audio(temp_file_path)
        st.text_area("Transcription :", transcription, height=200)

        # Étape 2 : Upload dans Supabase Storage (bucket = genup2050-pitch)
        # Supprimer un fichier existant avec le même nom (facultatif)
        try:
            supabase.storage.from_(bucket_name).remove([video_file.name])
        except Exception:
            pass  # Ignore s'il n'existait pas

        # Upload
        supabase.storage.from_(bucket_name).upload(video_file.name, temp_file_path)
        video_url = supabase.storage.from_(bucket_name).get_public_url(video_file.name)

        # Étape 3 : Formulaire utilisateur + Enregistrement
        user_name = st.text_input("Ton prénom / pseudo")
        if st.button("Enregistrer le pitch") and user_name:
            data = {
                "user_name": user_name,
                "video_url": video_url,
                "transcription": transcription
            }
            supabase.table("pitchs").insert(data).execute()
            st.success("Pitch sauvegardé avec succès !")
        elif st.button("Enregistrer le pitch") and not user_name:
            st.warning("Merci d’ajouter un prénom ou pseudo.")
    except Exception as e:
        st.error(f"Une erreur est survenue : {e}")
