import streamlit as st
from supabase import create_client, Client

# Chargement sécurisé des secrets ou fallback local
try:
    SUPABASE_URL = st.secrets["SUPABASE_URL"]
    SUPABASE_KEY = st.secrets["SUPABASE_KEY"]
    BUCKET_NAME = st.secrets.get("BUCKET_NAME", "genup2050-pitch")
except Exception as e:
    # Valeurs par défaut pour le développement local (à adapter)
    SUPABASE_URL = "https://sjlpeqfchvmuxxmqtkvx.supabase.co"
    SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNqbHBlcWZjaHZtdXh4bXF0a3Z4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDYwMTg3MjgsImV4cCI6MjA2MTU5NDcyOH0.7veB6GdaZodCfxjUbq8m3KphYXBBM1X1bERZV-Mp6h4"
    BUCKET_NAME = "genup2050-pitch"
    st.warning("Secrets non trouvés. Utilisation des valeurs par défaut. Erreur : {}".format(e))

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def get_rag_context():
    return {"source": "genup2050"}
