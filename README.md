# Proyek Akhir: Menyelesaikan Permasalahan Jaya Jaya Institut

## Business Understanding
Berdiri sejak tahun 2000 an, Jaya jaya institut sebagai salah satu institusi pendidikan telah mempunyai cukup banyak mahasiswa yang belajar di institut tersebut dan mencetak lulusan dengan reputasi yang cukup baik. 

Akan tetapi permasalahan yang mengganggu Jaya jaya Institut ialah banyaknya jumlah mahasiswa yang tidak lulus atau Dropout. Hal tersebut dapat mempengaruhi reputasi kampus karena menurunnya tingkat kelulusan mahasiswanya.

### Permasalahan Bisnis
Dari latar belakang diatas dapat disimpulkan bahwa terdapat permasalahan bisnis sebagai berikut:
- Tinggi nya presentase mahasiswa yang dropout
- Reputasi/akreditasi Jaya jaya Institut dapat terpengaruh karena tingkat kelulusan yang berkurang.
- Tingkat kepercayaan calon mahasiswa yang ingin mendaftar ke Jaya jaya institut menurun, & akan berpotensi jumlah mahasiswa yang mendaftar ke institut tersebut berkurang.

### Cakupan Proyek
Berikut merupakan hal-hal yang akan dikerjakan dan mencakup dalam proyek ini:
- Memperoleh, memahami dan memberikan analisa serta visualisasi tentang data performa mahasiswa yang digunakan pada proyek ini.
- Membuat Model machine Learning untuk prediksi mahasiswa yang Lulus atau Dropout.
- Membuat Sebuah Sistem sederhana untuk melakukan prediksi mahasiswa yang akan lulus atau dropout berdasarkan beberapa inputan.
- Memberikan beberapa rekomendasi yang dapat dilakukan untuk mengatasi masalah yang dihadapi oleh jaya jaya institut.

### Persiapan

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/README.md

Setup environment:
```
pip install requirements
```

## Business Dashboard
Pembuatan dashboard bisnis bertujuan untuk memberikan visualisasi dan pemahaman kepada pemangku kebijakan yang ada di Jaya jaya institut terkait faktor/matriks apa saja yang mempengaruhi seorang mahasiswa Dropout. Sehingga Institusi dapat memberikan kebijakan yang tepat untuk mengatasi permasalahn tersebut.

Dalam proyek ini dashboard yang dibuat menggunakan Looker Studio dengan url dashboard yang dapat diakses melalui link berikut ini:  
https://lookerstudio.google.com/reporting/4c101131-5e72-4404-824f-203bdfd6adc0  


## Menjalankan Sistem Machine Learning
Pada proyek ini dibuat sebuah sistem sederhana untuk melakukan prediksi mahasiswa yang droput atau lulus berdasarkan beberapa inputan. Sistem ini dibangun menggunakan streamlit dan di deploy pada streamlit cloud. Untuk menjalankan sistem ini secara lokal anda dapat mengikuti beberapa langkah berikut:   
- Instal library
```
pip install requirements  
```  
- lalu jalankan file yang bernama:  
```
notebook.ipynb   
```  
- Setelah menjalankan file notebook tersebut anda akan mendapatkan sebuah model yang kemudian akan digunakan pada sistem untuk melakukan prediksi.  

- kemudian jalankan  file yang bernama
```
streamlit_submission2.py  
```
Maka akan otomatis dialihkan sebuah halaman website yang berisi form yang perlu diisikan untuk menghasilkan prediksi mahasiswa tersebut lulus/dropout.  

Berikut merupakan link dari sistem yang sudah di deploy:  
[URL DEPLOYMENT STREAMLIT](https://dzulfikrisubmission2.streamlit.app/)


## Conclusion
Berdasarkan analisa yang telah dilakukan, dapat diketahui bahwa mahasiswa yang dropout dari Jaya jaya Institut memiliki beberapa indikator antara lain adalah nilai, dimana nilai mahasiswa yang dropout cenderung memiliki nilai yang rendah pada ip semester 1 & 2 yang mayoritas memiliki nilai 0. Kemudian hal tersebut juga mempengaruhi jumlah mata kuliah yang lulus lebih sedikit daripada mata kuliah yang di daftarkan pada awal semester. Meskipun tidak terlalu signifikan, ekonomi juga mempengaruhi mahasiswa untuk dropout, tidak sedikit mahasiswa droput dikarenakan pembayaran administrasi yang terlambat. Selain itu mahasiswa yang dropout mayoritas berstatus lajang dengan pembagian yang cukup seimbang untuk laki-laki dan perempuan. Distribusi usia mahasiswa yang dropout cukup bervariasi namun didominasi oleh rentang usia 17-20 tahun yang dapat diindikasikan kemungkinan penyebabnya ialah salah jurusan ataupun diterima di universitas lain, selain rentang usia tersebut usia dengan lebih 30 tahun juga menyumbang cukup banyak jumlah mahasiswa yang dropout, hal ini dapat diindikasikan dengan mahasiswa yang memiliki semester banyak / mengulang banyak mata kuliah sehingga di umur tersebut ia tidak bisa menyelesaikan studi dan lebih memilih untuk dropout. Dan yang terakhir prodi yang paling banyak menyumbang jumlah mahasiswa dropout ialah prodi manajemen baik kelas malam ataupun reguler.

### Rekomendasi Action Items
Berdasarkan hasil analisis yang telah dilakukan, berikut merupakan beberapa rekomendasi yang dapat dilakukan oleh Jaya jaya institut untuk menurunkan presentase mahasiswa yang dropout:  
- Institusi dapat menganalisa lebih lanjut prodi manajemen yang menyumbang jumlah mahasiswa droput terbanyak, sehingga dapat memberikan solusi yang sesuai dengan kondisi yang dialami oleh mahasiswa pada program studi tersebut. 
- Institusi dapat memberikan percobaan kedua kalinya setelah ujian dilakukan seperti remidial dan tugas tambahan untuk memperbaiki nilai yang dapat menurunkan angka ketidaklulusan mata kuliah yang diambil. 
- Memberikan beberapa opsi dukungan keringanan biaya administrasi dengan beberapa ketentuan hingga beasiswa yang dapat diambil oleh mahasiswa yang memiliki kesulitan ekonomi.
- Institusi dapat memperbaiki fasilitas yang dapat mendukung mahasiswa belajar dengan lebih baik.
- Memberikan evaluasi kepada tenaga pendidik/dosen apakah sudah melakasanakan tugas nya dengan baik sehingga mata kuliah yang diajar dapat diserap ilmunya oleh mahasiswa.
- Institut dapat melakukan survei pada periode tertentu kepada mahasiswanya sehingga dapat mendapatkan feedback dari mahasiswa terkait proses akademik yang yang ada di kampus tersebut.
