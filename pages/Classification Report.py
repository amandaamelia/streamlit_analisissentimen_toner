import streamlit as st
from PIL import Image

st.sidebar.success("Kamu sedang berada di menu Classification Report")

st.title("Classification Report SVM")
image = Image.open("cr_svm.png")
st.image(image, width = 400)
st.markdown(
  """
🔹 Negatif
- Precision 0.16: Dari semua prediksi yang diklaim sebagai "negatif", hanya 16% yang benar-benar negatif. Ini menunjukkan banyak prediksi negatif yang salah.
- Recall 0.14: Dari 35 data negatif yang sebenarnya ada, hanya 14% yang berhasil dikenali oleh model. Artinya, sebagian besar data negatif tidak terdeteksi.
- F1-score 0.15: Kombinasi precision dan recall yang rendah ini menunjukkan bahwa model kurang mampu mendeteksi sentimen negatif secara akurat.

🔹 Positif
- Precision 0.93: Sebagian besar prediksi yang diklasifikasikan sebagai "positif" memang benar positif. Ini menandakan model sangat jarang salah saat memprediksi data sebagai positif.
- Recall 0.94: Hampir seluruh data yang benar-benar positif berhasil dikenali model (94%).
- F1-score 0.94: Nilai ini memperkuat bahwa model sangat baik dalam mengenali sentimen positif.
"""

)

st.title("Classification Report Naive Bayes")
image = Image.open("cr_nb.png")
st.image(image, width = 400)
st.markdown(
  """
🔹 Negatif
- Precision 0.17: Dari semua prediksi yang diklaim sebagai "negatif", hanya 17% yang benar-benar negatif. Artinya, mayoritas prediksi negatif justru salah klasifikasi.
- Recall 0.37: Dari 35 data negatif yang sebenarnya, 37% berhasil dikenali oleh model. Ini menunjukkan bahwa model sedikit lebih baik dibanding SVM dalam mendeteksi sentimen negatif, meskipun masih tergolong rendah.
- F1-score 0.24: Gabungan precision dan recall menunjukkan bahwa performanya terhadap kelas negatif masih lemah, meskipun ada sedikit peningkatan dibanding model sebelumnya.

🔹 Positif
- Precision 0.95: Prediksi yang dinyatakan sebagai "positif" oleh model sangat akurat — 95% benar. Ini berarti model sangat jarang salah dalam memprediksi data sebagai positif.
- Recall 0.86: Dari semua data positif yang sebenarnya ada, 86% berhasil dikenali. Ini menunjukkan model cukup kuat mengenali kelas mayoritas.
- F1-score 0.90: Skor ini menunjukkan bahwa model Naive Bayes sangat baik dalam mendeteksi sentimen positif, meskipun recall-nya sedikit lebih rendah dari SVM.

"""
)

st.title("Classification Report Logistic Regression")
image = Image.open("cr_lr.png")
st.image(image, width = 400)
st.markdown(
  """
🔹 Negatif
- Precision 0.21: Dari semua prediksi yang diklasifikasikan sebagai "negatif", hanya 21% yang benar-benar negatif. Ini menunjukkan bahwa masih banyak prediksi negatif yang salah.
- Recall 0.31: Dari 35 data negatif yang sebenarnya ada, 31% berhasil dikenali oleh model. Ini menandakan bahwa performa model terhadap kelas negatif lebih baik dibanding SVM dan Naive Bayes.
- F1-score 0.25: Kombinasi precision dan recall menunjukkan kemampuan model mengenali sentimen negatif cukup meningkat, meskipun masih tergolong rendah.

🔹 Positif
- Precision 0.94: Sebagian besar data yang diprediksi sebagai "positif" memang benar positif — 94% akurat.
- Recall 0.91: Dari semua data yang sebenarnya positif, 91% berhasil dikenali dengan benar.
- F1-score 0.92: Hasil ini menunjukkan bahwa Logistic Regression sangat baik dalam mengklasifikasikan sentimen positif, bahkan sedikit lebih baik daripada Naive Bayes dari sisi recall dan f1-score.
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
