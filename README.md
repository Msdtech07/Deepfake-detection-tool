# Deepfake Detection System Using CNN 🧠🖼️

A Deep Learning based web application that detects whether an uploaded image is **Real** or **Fake (Deepfake)** using a trained **ResNet18 CNN model** with a simple and interactive **Streamlit interface**.

---

## 🚀 Features

* Upload and analyze images instantly
* Detects Real vs Fake images
* Built using Deep Learning (CNN)
* Streamlit-based interactive UI
* Uses pretrained ResNet18 architecture
* GPU support using PyTorch
* Simple and lightweight deployment

---

## 🛠️ Technologies Used

* Python
* Streamlit
* PyTorch
* Torchvision
* PIL (Pillow)
* Deep Learning
* CNN (Convolutional Neural Network)

---

## 📂 Project Structure

```text id="iwteho"
Deepfake-Detection/
│
├── app.py               # Streamlit frontend
├── predict.py           # Prediction script
├── model.pth            # Trained model
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash id="s1mij0"
git clone https://github.com/your-username/Deepfake-Detection.git
cd Deepfake-Detection
```

---

### 2️⃣ Install Dependencies

```bash id="6lrm9c"
pip install -r requirements.txt
```

Or install manually:

```bash id="i6bjj7"
pip install streamlit torch torchvision pillow
```

---

## ▶️ Run the Application

```bash id="dx5h2u"
streamlit run app.py
```

---

## 🧠 Model Architecture

The project uses:

* **ResNet18**
* Final fully connected layer modified for:

  * 2 classes:

    * Real
    * Fake

---

## 📌 How It Works

1. User uploads an image
2. Image is resized to **224×224**
3. Image is converted into tensor format
4. Trained ResNet18 model predicts:

   * Fake
   * Real
5. Result is displayed on the Streamlit app

---

## 📷 Supported Image Formats

* JPG
* JPEG
* PNG

---

## 🔍 Prediction Output Example

```text id="14r7c5"
Prediction: Fake
```

or

```text id="61iy9h"
Prediction: Real
```

---

## 📈 Future Improvements

* Video deepfake detection
* Live webcam detection
* Confidence score visualization
* Attention heatmaps
* Mobile app deployment
* Improved dataset training

---

## 🔒 Applications

* Social media content verification
* Cybersecurity and digital forensics
* Fake news detection
* Media authenticity verification

---

## 👨‍💻 Author

Developed as a Deep Learning and Cybersecurity project for educational purposes.

---

## 📜 License

This project is intended for educational and research purposes only.
