import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score, classification_report, confusion_matrix
import streamlit as st
import pickle

# Load Model
model_path = 'random_forest_model.pkl'
try:
    with open(model_path, 'rb') as f:
        rf_model = pickle.load(f)
        model_features = rf_model.feature_names_in_  # Get expected features from the model
except FileNotFoundError:
    st.error("Model tidak ditemukan. Pastikan file random_forest_model.pkl tersedia.")
    rf_model = None
    model_features = None

# Define Input Interface
st.title("Aplikasi Prediksi Volume Sampah Harian")
st.markdown("""
Masukkan parameter yang diperlukan untuk memprediksi volume sampah harian menggunakan model Random Forest.
""")

# User Inputs
st.sidebar.header("Input Parameter")
def user_input_features():
    bulan = st.sidebar.slider("Bulan (1-12):", 1, 12, 6)
    luas = st.sidebar.number_input("Luas Lokasi (m²):", min_value=0.0, value=100.0, step=10.0)
    tanggal = st.sidebar.slider("Tanggal (1-31):", 1, 31, 15)
    kecamatan = st.sidebar.selectbox("Kecamatan:", ["Johar Baru", "Kemayoran", "Senen", "Cempaka Putih"])
    wilayah = st.sidebar.selectbox("Wilayah:", ["Jakarta Pusat", "Jakarta Timur", "Jakarta Barat", "Jakarta Selatan"])

    # Create feature dictionary
    data = {
        'Bulan': bulan,
        'Luas(m2)': luas,
        'Tanggal': tanggal,
        'Kecamatan_Johar Baru': 1 if kecamatan == "Johar Baru" else 0,
        'Kecamatan_Kemayoran': 1 if kecamatan == "Kemayoran" else 0,
        'Kecamatan_Senen': 1 if kecamatan == "Senen" else 0,
        'Kecamatan_Cempaka Putih': 1 if kecamatan == "Cempaka Putih" else 0,
        'Wilayah_Jakarta Pusat': 1 if wilayah == "Jakarta Pusat" else 0,
        'Wilayah_Jakarta Timur': 1 if wilayah == "Jakarta Timur" else 0,
        'Wilayah_Jakarta Barat': 1 if wilayah == "Jakarta Barat" else 0,
        'Wilayah_Jakarta Selatan': 1 if wilayah == "Jakarta Selatan" else 0
    }
    return pd.DataFrame([data])

# Align Input Data
if model_features is not None:
    input_df = user_input_features()
    aligned_input = pd.DataFrame(0, index=[0], columns=model_features)  # Create a DataFrame with all features set to 0
    for col in input_df.columns:
        if col in aligned_input.columns:
            aligned_input[col] = input_df[col]

    st.write("## Data Input yang Diselaraskan")
    st.write(aligned_input)

    # Prediction Button
    if st.button("Hasilkan Prediksi"):
        if rf_model:
            try:
                # Make Predictions
                prediction = rf_model.predict(aligned_input)
                proba = rf_model.predict_proba(aligned_input)[:, 1]

                # Display Results
                st.header("Hasil Prediksi")
                st.subheader("Prediksi Random Forest")
                st.write(f"Prediksi Kelas: {'Tinggi' if prediction[0] == 1 else 'Rendah'}")
                st.write(f"Probabilitas Kelas Tinggi: {proba[0]:.2f}")
            except Exception as e:
                st.error(f"Terjadi kesalahan saat melakukan prediksi: {str(e)}")
else:
    st.error("Fitur model tidak tersedia. Pastikan model telah dimuat dengan benar.")