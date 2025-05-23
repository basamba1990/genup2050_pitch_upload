import streamlit as st
from supabase import create_client, Client

# Chargement sécurisé des secrets ou fallback local
try:
    supabase_url = st.secrets["supabase_url"]
    supabase_key = st.secrets["supabase_key"]
    bucket_name = st.secrets.get("bucket_name", "genup2050-pitch")
except Exception as e:
    # Valeurs par défaut pour le développement local (à adapter)
    supabase_url = "https://sjlpeqfchvmuxxmqtkvx.supabase.co"
    supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNqbHBlcWZjaHZtdXh4bXF0a3Z4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDYwMTg3MjgsImV4cCI6MjA2MTU5NDcyOH0.7veB6GdaZodCfxjUbq8m3KphYXBBM1X1bERZV-Mp6h4"
    bucket_name = "genup2050-pitch"
    st.warning("Secrets non trouvés. Utilisation des valeurs par défaut. Erreur : {}".format(e))

supabase: Client = create_client(supabase_url, supabase_key)

def get_rag_context():
    return {"source": "genup2050"}
