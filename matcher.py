from sentence_transformers import SentenceTransformer
import streamlit as st
from sklearn.metrics.pairwise import cosine_similarity

@st.cache_resource(show_spinner=False)
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")

model = load_model()

def embed_text(text):
    return model.encode([text], convert_to_tensor=True)

def rank_resumes(job_text, resume_texts):
    job_embed = embed_text(job_text)
    results = []

    for name, text in resume_texts:
        res_embed = embed_text(text)
        score = cosine_similarity(job_embed, res_embed)[0][0]
        results.append((name, score, text))

    return sorted(results, key=lambda x: x[1], reverse=True)