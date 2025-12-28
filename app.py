import streamlit as st
from PIL import Image
from ai_detector_model import load_model, predict

# Load your model (consider loading outside of a function to load once)
model, device = load_model('best_combined_resnet_model.pth')

st.title('AI Image Detector')

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    prediction, confidence = predict(image, model, device)
    st.write(f"Prediction: {prediction} with {confidence:.2f}% confidence.")