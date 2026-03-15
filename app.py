import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image

# load model
model = load_model("waste_classifier_model.h5")

class_names = ["cardboard","metal","paper","plastic","trash"]

st.title("♻️ Smart Waste Classifier")

st.write("Upload an image to classify waste type")

uploaded_file = st.file_uploader("Choose an image", type=["jpg","png","jpeg"])

if uploaded_file is not None:

    img = Image.open(uploaded_file)

    st.image(img, caption="Uploaded Image", use_column_width=True)

    img = img.resize((224,224))

    img_array = image.img_to_array(img)/255
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)

    predicted_class = class_names[np.argmax(prediction)]

    st.success(f"Predicted Waste Type: {predicted_class}")