# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut, sebuah institusi pendidikan terkemuka yang telah beroperasi sejak tahun 2000, memiliki reputasi yang sangat baik dalam mencetak lulusan berkualitas tinggi. Namun, institusi ini menghadapi tantangan serius dengan tingginya angka dropout siswa, yang dapat merusak reputasi dan efisiensi operasionalnya. Dengan mengidentifikasi siswa yang berpotensi untuk dropout lebih awal, Jaya Jaya Institut dapat memberikan bimbingan dan dukungan yang diperlukan untuk meningkatkan retensi siswa dan memastikan kelulusan mereka, sehingga mempertahankan reputasi institusi serta meningkatkan kepuasan dan keberhasilan siswa.

### Permasalahan Bisnis
Jaya Jaya Institut ingin mendeteksi lebih awal siswa yang berpotensi dropout sehingga dapat diberikan bimbingan khusus untuk meningkatkan retensi dan keberhasilan akademik siswa. Tujuan tersebut mengarahkan kepada permasalahan yang diuraikan berikut:
- Apa faktor utama yang menyebabkan mahasiswa berhenti studi, dan bagaimana strategi institusi dapat disesuaikan untuk mengurangi risiko tersebut?
- Sejauh mana dukungan akademik, sosial, dan finansial berdampak terhadap keberhasilan studi mahasiswa?

### Cakupan Proyek
- Mempersiapkan data mulai dari Data Understanding hingga Feature Engineering
- Membangun model klasifikasi ML dengan XGBoost untuk memprediksi kemungkinan dropout siswa
- Mengidentifikasi kepentingan setiap fitur terhadap dropout
- Mengembangkan dashboard untuk menganalisis fitur yang mempengaruhi dropout
- Mengembangkan prototype dengan Streamlit untuk memprediksi kemungkinan dropout siswa.
- Memberikan rekomendasi aksi yang memungkinkan untuk dilaksanakan berdasarkan hasil analisis.

### Persiapan

Sumber data: [Student Performance Data](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

Setup environment:
1. Buka Terminal atau Command Prompt. Pastikan Python 3.9+ sudah terinstal.

2. Buat dan aktifkan Virtual Environment Baru:

```
python -m venv venv
.\venv\Scripts\activate (windows)
source venv/bin/activate (macOS)
```
Atau
```
conda create --name main-env python=3.9
conda activate main-env
```
3. Instal depedencies:
```
pip install -r requirements.txt
```

## Business Dashboard
Business dashboard dibuat menggunakan Google Looker Studio mencakup satu halaman dashboard yang menampilkan fitur-fitur utama dari data performa siswa, yang mencakup Dropout dan Graduation Rate, Gender, Displaced status, Scholarship status, Debt status, admission grade, serta grade range.
Dashboard dapat diakses melalui: [Link Dashboard](https://lookerstudio.google.com/reporting/4585fa57-8ef9-4caf-b424-41c60b18a9df)

## Menjalankan Sistem Machine Learning
Jalankan perintah streamlit berikut di terminal atau command prompt:
```
streamlit run app.py
```
Prototype yang telah di-deploy dengan Streamlit dapat diakses melalui link: xxx

## Conclusion
Berdasarkan analisis dan pemodelan ML pada kasus ini, dapat diambil beberapa wawasan dan informasi mengenai faktor-faktor yang mempengaruhi kemungkinan dropout siswa Jaya Jaya Institut, yang antara lain Curricular_units_2nd_sem_grade, Gender, Admission_grade, Scholarship_holder, dan Displaced. Model klasifikasi dengan XGBoost yang telah dibangun memperoleh skor precision=0.95, recall=0.82, dan F1=0.88 untuk label 0, sedangkan precision=0.89, recall=0.97, dan F1=0.93 untuk label 1, mengindikasikan performa model yang dapat bekerja dengan baik dalam mengklasifikasi, meskipun distribusi data seharusnya lebih seimbang agar performa model menjadi lebih baik dan adil. Dashboard yang dibuat dapat membantu memonitor performa siswa, sementara prototype yang dibuat dapat membantu memprediksi kemungkinan dropout siswa.

### Rekomendasi Action Items
- Tingkatkan program pendampingan akademik (academic mentoring) khusus untuk mahasiswa tahun pertama menjelang semester kedua.
- Gender dan beasiswa merupakan indikator sosial penting. Kebijakan dukungan berbasis gender dan perluasan akses beasiswa bisa mengurangi dropout.
- Berikan intervensi proaktif (coaching, mentoring, konsultasi rutin) untuk mahasiswa dengan nilai masuk rendah.
- Mahasiswa displaced memerlukan dukungan tambahan secara akademik untuk menjaga keberlanjutan studi mereka.
