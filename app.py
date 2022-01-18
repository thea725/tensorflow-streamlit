import streamlit as st
import keras
import numpy as np
from PIL import Image, ImageOps

CLASSES = ['ba','ca','da','dha','ga','ha','ja','ka','la','ma','na','nga','nya','pa','ra','sa','ta','tha','wa','ya']

st.title("Klasifikasi Aksara Jawa")
st.header("Berdasarkan dataset yg ada di https://www.kaggle.com/vzrenggamani/hanacaraka")
st.write("Tersedia mode upload gambar dan mengambil foto, keduanya terdapat di sidebar")

# fungsi yang secara umum memproses gambar dengan AI
def load_model(img):
    # Memuat model Tensorflow Keras
    model = keras.models.load_model('keras_model.h5')

    # Array yang sesuai untuk diload ke model
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = img
    #image sizing
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    #menerjemahkan gambar ke bentuk numpy
    image_array = np.asarray(image)
    # normalisasi gambar
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    # gambar diload dalam bentuk array
    data[0] = normalized_image_array

    # prediksi dan return hasil prediksi
    prediction = model.predict(data)
    return np.argmax(prediction)

# fungsi yang secara umum input gambar dengan upload
def upload():
    
    uploaded_file = st.file_uploader("Input Aksara Jawa", type="jpg")
    
    #jika gambar ditangkap
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, use_column_width=True)
        st.write("")
        st.write("Classifying...")
        
        #mendapatkan indeks prediksi
        index = load_model(image)
        
        #menampilkan hasil prediksi
        st.write(CLASSES[index])

# fungsi yang secara umum input gambar dengan menangkap frame dengan kamera
def foto():
    #mengakses kamera
    picture = st.camera_input("Take a picture")\
    
    #jika gambar ditangkap
    if picture:
        image = Image.open(picture)
        st.image(image, use_column_width=True)
        st.write("")
        st.write("Classifying...")
        
        #mendapatkan indeks prediksi
        index = load_model(image)
        
        #menampilkan hasil prediksi
        st.write(CLASSES[index])

#fungsi pertama yang dipanggil
if __name__ == "__main__":
    
    #UI untuk mengubah mode
    st.sidebar.header("Mode")
    mode = st.sidebar.radio("Yang tersedia", ("Upload Gambar", "Foto Kamera"))
    if mode == "Upload Gambar":
        upload()
    elif mode == "Foto Kamera":
        foto()