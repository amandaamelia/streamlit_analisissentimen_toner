import streamlit as st
from PIL import Image

st.sidebar.success("Kamu sedang berada di menu Confusion Matrix")

st.title("Confusion Matrix SVM")
image = Image.open('confusion_matrix_svm.png')
st.image(image, width = 500)
st.markdown(
    """
1. **True Negative (TN): Baris "negatif", Kolom "negatif" (Nilai: 5)**
\nIni adalah jumlah ulasan yang sebenarnya negatif dan diprediksi benar sebagai negatif oleh model.
\n**Interpretasi**: Model SVM berhasil memprediksi 5 ulasan negatif dengan benar sebagai negatif.
    
2. **False Positive (FP): Baris "negatif", Kolom "positif" (Nilai: 30))**
\nIni adalah jumlah ulasan yang sebenarnya negatif tetapi salah diprediksi sebagai positif oleh model. 
\n**Interpretasi**: Ada 30 ulasan yang sebenarnya memiliki sentimen negatif, tetapi model secara keliru menganggapnya sebagai positif.	

3. **False Negative (FN): Baris "positif", Kolom "negatif" (Nilai: 27)**
\nIni adalah jumlah ulasan yang sebenarnya positif tetapi salah diprediksi sebagai negatif oleh model. 
\n**Interpretasi**: Ada 27 ulasan yang sebenarnya memiliki sentimen positif, tetapi model secara keliru menganggapnya sebagai negatif.
    
4. **True Positive (TP): Baris "positif", Kolom "positif" (Nilai: 416)**    
\nIni adalah jumlah ulasan yang sebenarnya positif dan diprediksi benar sebagai positif oleh model.
\n**Interpretasi**: Model berhasil memprediksi 416 ulasan positif dengan benar sebagai positif.
    """
)

st.title("Confusion Matrix Naive Bayes")
image = Image.open('confusion_matrix_nb.png')
st.image(image, width = 500)
st.markdown(
    """
1. **True Negative (TN): Baris "negatif", Kolom "negatif" (Nilai: 13)**
\nIni adalah jumlah ulasan yang sebenarnya negatif dan diprediksi benar sebagai negatif oleh model.
\n**Interpretasi**: Model Naive Bayes berhasil memprediksi 13 ulasan negatif dengan benar sebagai negatif.

2. **False Positive (FP): Baris "negatif", Kolom "positif" (Nilai: 22)**
\nIni adalah jumlah ulasan yang sebenarnya negatif tetapi salah diprediksi sebagai positif oleh model.
\n**Interpretasi**: Ada 22 ulasan yang sebenarnya memiliki sentimen negatif, tetapi model secara keliru menganggapnya sebagai positif.

3. **False Negative (FN): Baris "positif", Kolom "negatif" (Nilai: 62)**
\nIni adalah jumlah ulasan yang sebenarnya positif tetapi salah diprediksi sebagai negatif oleh model. 
\n**Interpretasi**: Ada 62 ulasan yang sebenarnya memiliki sentimen positif, tetapi model secara keliru menganggapnya sebagai negatif.
    
4. **True Positive (TP): Baris "positif", Kolom "positif" (Nilai: 381)**    
\nIni adalah jumlah ulasan yang sebenarnya positif dan diprediksi benar sebagai positif oleh model.
\n**Interpretasi**: Model berhasil memprediksi 381 ulasan positif dengan benar sebagai positif.
    """
)

st.title("Confusion Matrix Logistic Regression")
image = Image.open('confusion_matrix_lr.png')
st.image(image, width = 500)
st.markdown(
    """
1. **True Negative (TN): Baris "negatif", Kolom "negatif" (Nilai: 11)**
\nIni adalah jumlah ulasan yang sebenarnya negatif dan diprediksi benar sebagai negatif oleh model.
\n**Interpretasi**: Model Regresi Logistik berhasil memprediksi 11 ulasan negatif dengan benar sebagai negatif.

2. **False Positive (FP): Baris "negatif", Kolom "positif" (Nilai: 24)**
\nIni adalah jumlah ulasan yang sebenarnya negatif tetapi salah diprediksi sebagai positif oleh model.
\n**Interpretasi**: Ada 24 ulasan yang sebenarnya memiliki sentimen negatif, tetapi model secara keliru menganggapnya sebagai positif.

3. **False Negative (FN): Baris "positif", Kolom "negatif" (Nilai: 42)**
\nIni adalah jumlah ulasan yang sebenarnya positif tetapi salah diprediksi sebagai negatif oleh model. 
\n**Interpretasi**: Ada 42 ulasan yang sebenarnya memiliki sentimen positif, tetapi model secara keliru menganggapnya sebagai negatif.

4. **True Positive (TP): Baris "positif", Kolom "positif" (Nilai: 401)**    
\nIni adalah jumlah ulasan yang sebenarnya positif dan diprediksi benar sebagai positif oleh model.
\n**Interpretasi**: Model berhasil memprediksi 401 ulasan positif dengan benar sebagai positif.
    """
)

st.markdown(
    """
    <hr style="margin-top: 50px;">
    <div style='text-align: center; color: gray; font-size: 14px;'>
        Built by Amanda Amelia | Analisis Sentimen Toner Eksfoliasi Sociolla 💖
    </div>
    """,
    unsafe_allow_html=True
)