import streamlit as st
import joblib
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import seaborn as sns


svm_model = joblib.load("svm_model.pkl")
nb_model = joblib.load("naive_bayes_model.pkl")
lr_model = joblib.load("logistic_regression_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")
label_encoder = joblib.load("label_encoder.pkl")


# Make sure pipeline.py is in the same directory or provide the correct path
from pipeline import case_folding, clean_text, tokenize, normalized_term, stopwords_removal, get_stemmed_term

def preprocess_text(text):
    text = case_folding(text)
    text = clean_text(text)
    tokens = tokenize(text)
    tokens = normalized_term(tokens)
    tokens = stopwords_removal(tokens)
    tokens = get_stemmed_term(tokens)
    return ' '.join(tokens)

# --- 5. Antarmuka Streamlit ---
st.markdown("""
<h2 style='text-align: center; color: #926363;'>👋 Halo!  Selamat Datang di Web Analisis Sentimen Toner Eksfoliasi Sociolla! ✨</h2>
            
<p style='text-align: center; font-size: 15px'>
Aplikasi ini dirancang untuk menganalisis sentimen dari ulasan pengguna terhadap produk toner eksfoliasi pada platform Sociolla, menggunakan pendekatan berbasis Machine Learning.
    Aplikasi ini siap bantu kamu mengenali apakah ulasan tersebut termasuk <b>positif✔️</b> atau <b>negatif❌</b> secara otomatis! Kamu bisa pilih model analisis 🔍: <b>SVM, Naive Bayes,</b> atau <b>Logistic Regression</b>
</p>
""", unsafe_allow_html=True)

# Pilihan model
models = {
    "SVM": svm_model,
    "Naive Bayes": nb_model,
    "Logistic Regression": lr_model
}

selected_model_name = st.selectbox("Pilih Model Analisis Sentimen:", list(models.keys()))
selected_model = models[selected_model_name]

# Input user
user_input = st.text_area("Ketik teks di bawah ini 📩:", "")

# Tombol prediksi
if st.button("Prediksi Sentimen"):
    if user_input.strip() == "":
        st.warning("Silakan masukkan teks terlebih dahulu.")
    else:
        # Preprocessing
        preprocessed = preprocess_text(user_input)

        # Vektorisasi
        vectorized = vectorizer.transform([preprocessed])

        # Prediksi
        prediction = selected_model.predict(vectorized)
        label_raw = label_encoder.inverse_transform(prediction)[0]
        label = "positif ✔️" if label_raw == "positif" else "negatif ❌"

        # Confidence score
        if hasattr(selected_model, "predict_proba"):
            prob = selected_model.predict_proba(vectorized)[0]
            confidence = max(prob)
            st.markdown(f"### Model yang Digunakan: `{selected_model_name}`")
            st.markdown(f"**Sentimen Prediksi** : `{label}`")
            st.markdown(f"**Skor Kepercayaan (Confidence)** : `{confidence:.2f}`")
        else:
            st.markdown(f"### Model yang Digunakan: `{selected_model_name}`")
            st.markdown(f"**Sentimen Prediksi** : `{label}`")
            st.info("Model ini tidak mendukung skor kepercayaan (confidence).")


st.markdown(
    """
    <hr style="margin-top: 50px;">
    <div style='text-align: center; color: gray; font-size: 14px;'>
        Built by Amanda Amelia | Analisis Sentimen Toner Eksfoliasi Sociolla 💖
    </div>
    """,
    unsafe_allow_html=True
)


st.sidebar.success("Menu Sidebar 👆")


