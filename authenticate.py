import sqlite3
import numpy as np
from sentence_transformers import SentenceTransformer
from scipy.spatial.distance import cosine

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def text_to_vector(text):
    return model.encode(text)

def cosine_similarity(vec1, vec2):
    return 1 - cosine(vec1, vec2)

def get_stored_password_vector():
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username = 'user1'")
    stored_password = cursor.fetchone()[0]
    conn.close()
    return text_to_vector(stored_password)

def authenticate(predicted_text):
    predicted_vector = text_to_vector(predicted_text)
    stored_vector = get_stored_password_vector()
    similarity = cosine_similarity(predicted_vector, stored_vector)
    print(f"Cosine Similarity: {similarity}")
    if similarity > 0.8: 
        print("Authentication Successful")
    else:
        print("Authentication Failed")

if __name__ == "__main__":
    from predictor import main as predict_video

    predicted_text = predict_video()
    authenticate(predicted_text)
