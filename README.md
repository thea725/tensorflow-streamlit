## Getting started

### Prerequisites
Terlebih dahulu menginstall requirements
```
pip install -r requirements.txt
```

### Running the model
Model dapat mengenali aksara jawa melalui foto dan upload gambar, model dapat dijalankan dengan
```
streamlit run app.py
```

### Proses
Proses pembuatan apps ini terbagi atas tiga:</br>
</br><strong>1. Membersihkan dataset</strong></br>
Dataset yang didapatkan sebelumnya dikelompokkan terlebih dahulu dan dibersihkan dari data yang rusak.</br>
</br><strong>2. Melatih model</strong></br>
Model dilatih dengan dukungan teachablemachine, hal ini sebenarnya kurang disarankan karena tingkat akurasi yang cenderung buruk dan waktu pemrosesan yang lama, namun dengan tingkat pembuatan yang sangat cepat, karena mementingkan fungsi waktu maka model dibuat dengan teachablemachine</br>
</br><strong>3. Integrasi dengan UI</strong></br>
Setelah model dibentuk maka model diimplementasikan ke dalam bentuk web app agar lebih mudah digunakan.
