# Klasifikasi-Volume-Pengangkutan-Sampah
Nama : Muchamad Bagus Triyadi (202110370311347)

Proyek ini adalah implementasi klasifikasi volume pengangkutan sampah, dengan menggunakan pendekatan Random Forest dan XGBoost ini dapat membantu mengklasifikasi volume sampah.

Model dapat di akses di Drive Berikut:
https://drive.google.com/drive/folders/1UMZbOoko7asoXkzoRS5h4WNjuUgF1iV-?usp=sharing


**RANDOM FOREST**

(![image](https://github.com/user-attachments/assets/5170d5d2-3b81-4230-b31d-72885ebd255b)

**XGBOOST**
(![image](https://github.com/user-attachments/assets/4aa32f43-af7a-4234-86e6-1736dac02ec2)


## Latar Belakang

**Latar Belakang**

Aplikasi ini bertujuan untuk memprediksi volume sampah harian berdasarkan parameter yang dimasukkan oleh pengguna. Sampah merupakan salah satu permasalahan lingkungan utama yang memengaruhi kehidupan manusia. Ketidakpastian dalam pengelolaan sampah, seperti fluktuasi volume harian, dapat berdampak pada efisiensi pengangkutan, kapasitas tempat pembuangan akhir, dan keberlanjutan lingkungan. Oleh karena itu, prediksi volume sampah yang akurat menjadi kebutuhan penting untuk membantu masyarakat dan pihak pengelola dalam merancang sistem pengelolaan sampah yang efektif.

Seiring dengan perkembangan teknologi, model pembelajaran mesin (machine learning) telah digunakan secara luas untuk memprediksi berbagai fenomena, termasuk volume sampah. Model ini memiliki kemampuan untuk menganalisis data historis volume sampah dan memprediksi pola di masa depan dengan tingkat akurasi yang tinggi.

Aplikasi Prediksi Volume Sampah Harian ini dikembangkan untuk memanfaatkan kekuatan model pembelajaran mesin seperti Random Forest dan XGBoost dalam memprediksi volume sampah. Dengan memberikan masukan berupa parameter seperti jumlah penduduk, aktivitas ekonomi, cuaca, dan pola pengangkutan sebelumnya, aplikasi ini dapat memberikan hasil prediksi yang mudah dipahami serta disertai dengan visualisasi untuk interpretasi model.

Dengan adanya aplikasi ini, diharapkan masyarakat dan pihak pengelola sampah dapat mengambil keputusan yang lebih baik, seperti perencanaan pengangkutan, alokasi sumber daya, atau pengelolaan kapasitas tempat pembuangan akhir. Aplikasi ini juga memberikan edukasi kepada pengguna tentang bagaimana faktor-faktor tersebut memengaruhi volume sampah melalui interpretasi fitur.

# Prediksi volume sampah

Aplikasi web ini memprediksi volume samapah berdasarkan parameter luas lokasi, bulan dan tanggal yang dimasukkan pengguna. Aplikasi ini dibangun menggunakan **Streamlit**, dengan dukungan model pembelajaran mesin seperti **Random Forest** dan **XGBoost**.

## Fitur Utama
1. **Input Parameter Volume Sampah:**
   - Bulan.
   - Luas Lokasi.
   - Tanggal.
   - Kecamatan.
   - Wilayah.

2. **Prediksi Hasil:**
   - Prediksi berapa banyak volume sampah tiap titik lokasi menggunakan Random Forest dan XGBoost.

3. **Interpretasi Model:**
   - Visualisasi interpretasi fitur dengan untuk model Random Forest.
   - Debugging input data dan hasil prediksi untuk XGBoost.

## Teknologi yang Digunakan
- **Streamlit**: Untuk antarmuka pengguna.
- **Scikit-learn**: Implementasi model Random Forest.
- **XGBoost**: Implementasi model XGBoost.
- **Matplotlib**: Untuk visualisasi probabilitas prediksi.


## Cara Menggunakan Aplikasi
1. Jalankan aplikasi dengan perintah:
   ```bash
   streamlit run app.py

## hasil Algoritma 
1. Random Forest
<img width="323" alt="image" src="https://github.com/user-attachments/assets/38832a65-4b48-4914-a4a6-e79022a2f50f" />

visualisasi hasil validasi ROC ccurve :
<img width="422" alt="image" src="https://github.com/user-attachments/assets/c0194b6d-f158-47bd-b045-c7f9378d2dd2" />

3. XGBoost
<img width="360" alt="image" src="https://github.com/user-attachments/assets/9463552f-f5d7-4a12-9e08-5059bf49219c" />

visualisasi hasil validasi ROC curve :
<img width="630" alt="image" src="https://github.com/user-attachments/assets/5f71da35-9ee0-4374-b85e-6c487e922a46" />


## perbandingan hasil algoritma
Akurasi:

Random Forest memiliki akurasi 100%.
XGBoost memiliki akurasi 80%.
Dengan demikian, Random Forest memiliki akurasi yang lebih tinggi dibandingkan XGBoost.
Precision, Recall, dan F1-Score:

Untuk kelas 0.0:
Random Forest menunjukkan precision 1.00, recall 1.00, dan F1-score 1.00.
XGBoost menunjukkan precision 0.81, recall 0.98, dan F1-score 0.89.
Pada kelas ini, Random Forest lebih unggul dalam recall dan F1-score.
Untuk kelas 1.0:
Random Forest memiliki precision 1.00, recall 1.00, dan F1-score 1.00.
XGBoost memiliki precision 0.64, recall 0.13, dan F1-score 0.21.
Pada kelas ini,Random Forestlebih unggul dalam recall,precision dan F1-score.
Rata-rata (Macro dan Weighted):

Random Forest memiliki rata-rata precision, recall, dan F1-score (macro dan weighted) sebesar 1.00.
XGBoost memiliki rata-rata precision, recall, dan F1-score (macro dan weighted) sebesar 0.74 hingga 0.80.
Secara keseluruhan, Random Forest memberikan performa yang lebih konsisten dan unggul pada rata-rata.

Kesimpulan: Random Forest unggul dalam hal akurasi, precision, recall, dan F1-score dibandingkan XGBoost, meskipun XGBoost tetap memiliki performa yang baik.
