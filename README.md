# 🖌️ Digit Recognizer using Streamlit

[![Streamlit App](https://img.shields.io/badge/Live%20Demo-Streamlit-blue?logo=streamlit)](https://digit-recognizer-krn.streamlit.app/)

An interactive web app that recognizes handwritten digits using a Convolutional Neural Network (CNN) trained on the MNIST dataset. Built with **Streamlit** and **TensorFlow**.

---

## 🚀 Live Demo

👉 Try it here: [https://digit-recognizer-krn.streamlit.app/](https://digit-recognizer-krn.streamlit.app/)

---

## ✨ Features

- 🧠 Trained on MNIST dataset  
- 🖱️ Draw digits directly in your browser  
- ⚡ Predicts digits using a pre-trained CNN model  
- 🚀 Built with Python, Streamlit, and TensorFlow  
- 💡 Easy to retrain with your own model  

---

## 📁 Project Structure

```
digit-recognizer/
├── app.py                # Streamlit app
├── train_model.py        # CNN model training script
├── mnist_model.h5        # Pre-trained model
├── requirements.txt      # Dependencies
├── .gitignore
└── LICENSE               # MIT License
```

---

## 🛠️ How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/morikaransinh/digit-recognizer.git
cd digit-recognizer
```

### 2. (Optional) Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run app.py
```

Open your browser at:  
👉 `http://localhost:8501`

---

## 🧠 Model Training (Optional)

If you want to retrain the model from scratch:

```bash
python train_model.py
```

This will generate the `mnist_model.h5` file used by the app.

---

## 🌍 Deployment

You can deploy the app on:

- [Streamlit Community Cloud](https://streamlit.io/cloud)
- [Render](https://render.com/)
- [Hugging Face Spaces](https://huggingface.co/spaces)

The current app is already deployed at 👉 [https://digit-recognizer-krn.streamlit.app/](https://digit-recognizer-krn.streamlit.app/)

---

## 📄 License

This project is licensed under the **MIT License**.  
See the [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)


---

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io)
- [TensorFlow](https://www.tensorflow.org/)
- [MNIST Dataset](http://yann.lecun.com/exdb/mnist/)

---

⭐ Star this repo if you find it helpful!
