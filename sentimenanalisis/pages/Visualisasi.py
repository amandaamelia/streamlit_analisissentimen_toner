import streamlit as st
from PIL import Image

st.sidebar.success("Kamu sedang berada di menu Visualisasi")

st.title("WordCloud Sentimen Positif")
image = Image.open('wordcloud_positif.png')
st.image(image, width = 600)

st.title("WordCloud Sentimen Negatif")
image = Image.open('wordcloud_negatif.png')
st.image(image, width = 600)

st.subheader("Visualisasi Peringkat 20 Kata Berdasarkan TF-IDF")
image = Image.open('tfidf_top20.png')
st.image(image, width = 800)

st.subheader("Visualisasi Perbandingan Performa Model ")
image = Image.open('perbandingan_model.png')
st.image(image, width = 800)

st.markdown(
    """
    <hr style="margin-top: 50px;">
    <div style='text-align: center; color: gray; font-size: 14px;'>
        Built by Amanda Amelia | Analisis Sentimen Toner Eksfoliasi Sociolla 💖
    </div>
    """,
    unsafe_allow_html=True
)