import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import numpy as np
import cv2
import os
import subprocess
import time
from tensorflow.keras.models import load_model
import streamlit.components.v1 as components

st.set_page_config(page_title="Digit Recognizer", layout="centered")
st.title("🖌️ Draw a Number (0-9) and Let AI Predict!")

# --- Section 1: Draw and Predict ---
st.header("🎨 Draw a Digit")

canvas_result = st_canvas(
    fill_color="black",
    stroke_width=20,
    stroke_color="white",
    background_color="black",
    height=280,
    width=280,
    drawing_mode="freedraw",
    key="canvas"
)

if canvas_result.image_data is not None:
    img = canvas_result.image_data
    img = cv2.cvtColor(img.astype("uint8"), cv2.COLOR_RGBA2GRAY)
    img = cv2.resize(img, (28, 28))
    img = img / 255.0
    img = img.reshape(1, 28, 28, 1)

    if st.button("🧠 Predict"):
        try:
            model = load_model("mnist_model.h5")
            pred = model.predict(img)
            st.subheader(f"✅ Predicted Digit: {np.argmax(pred)}")
        except Exception as e:
            st.error("❌ Model not found or error during prediction.")
            st.text(str(e))

# --- Section 2: Train Model + Show TensorBoard ---
st.header("⚙️ Train New Model")

if st.button("🚀 Train Model from Scratch"):
    st.info("🔄 Training started... This may take a minute.")
    
    # Optional: clear logs
    if os.path.exists("logs/fit"):
        import shutil
        shutil.rmtree("logs/fit")

    # Run training script
    result = subprocess.run(["python", "train_model.py"])
    if result.returncode == 0:
        st.success("✅ Model trained successfully!")
        time.sleep(2)

        # Show TensorBoard dashboard
        st.info("📊 Loading Training Metrics...")
        components.iframe("http://localhost:6006", height=600, scrolling=True)
    else:
        st.error("❌ Training failed.")
