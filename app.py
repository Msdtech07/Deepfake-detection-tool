import streamlit as st
import subprocess

st.title("Deepfake Detection App")

uploaded_file = st.file_uploader("Upload an image", type=["jpg","jpeg","png"])

if uploaded_file is not None:

    file_path = "temp.jpg"

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.image(file_path, caption="Uploaded Image")

    result = subprocess.run(
        ["python", "predict.py", file_path],
        capture_output=True,
        text=True
    )

    st.subheader("Prediction Result:")
    st.write(result.stdout)