# 🌍♻️ EcoVision AI
### 🚀 Deep Learning Powered Waste Recognition System

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/TensorFlow-Deep%20Learning-orange?style=for-the-badge&logo=tensorflow">
  <img src="https://img.shields.io/badge/Computer%20Vision-MobileNetV2-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Streamlit-Web%20Application-red?style=for-the-badge&logo=streamlit">
</p>

---

## 📌 Overview

**EcoVision AI** is an intelligent waste recognition system that leverages **Transfer Learning** and **Deep Learning-based Computer Vision** to automatically classify waste materials into multiple categories.

The project utilizes a **MobileNetV2 backbone network** for high-performance feature extraction and classification, enabling efficient and scalable waste identification for smart recycling applications.

By integrating a lightweight **Streamlit Web Interface**, EcoVision AI provides real-time image classification capabilities through an interactive user experience.

---

## ✨ Key Features

✅ Transfer Learning using MobileNetV2

✅ Deep Learning-powered Waste Classification

✅ Data Augmentation for Enhanced Generalization

✅ Real-Time Prediction through Streamlit

✅ Lightweight and Deployment-Friendly Architecture

✅ GPU Accelerated Training using TensorFlow

---

## 🧠 Model Architecture

```text
Input Image (224x224)
        │
        ▼
MobileNetV2 (Pretrained Feature Extractor)
        │
        ▼
GlobalAveragePooling2D
        │
        ▼
Dense Layer (128 Units, ReLU)
        │
        ▼
Dropout Layer
        │
        ▼
Dense Layer (64 Units, ReLU)
        │
        ▼
Softmax Output Layer
```

The architecture combines transfer learning with a custom classification head to achieve robust performance while minimizing computational overhead.

---

## 📊 Dataset

The model was trained on a multi-class waste classification dataset consisting of various recyclable and non-recyclable waste categories.

### Categories

- 📦 Cardboard
- 🥫 Metal
- 📄 Paper
- 🧴 Plastic
- 🗑️ Trash

### Dataset Split

| Dataset | Percentage |
|----------|-----------|
| Training | 80% |
| Validation | 20% |

---

## ⚙️ Data Preprocessing

The following augmentation techniques were applied:

- Image Rescaling
- Random Rotation
- Horizontal Flipping
- Zoom Augmentation
- Data Normalization

These preprocessing steps improve model generalization and reduce overfitting.

---

## 📈 Training Configuration

| Parameter | Value |
|------------|--------|
| Architecture | MobileNetV2 |
| Input Size | 224 × 224 |
| Batch Size | 32 |
| Optimizer | Adam |
| Loss Function | Categorical Crossentropy |
| Framework | TensorFlow/Keras |

---

## 🌐 Web Application

EcoVision AI includes an interactive web application built using Streamlit.

### Workflow

```text
Upload Waste Image
        │
        ▼
AI Model Inference
        │
        ▼
Waste Category Prediction
        │
        ▼
Display Result
```

The application enables users to upload an image and receive an instant waste classification prediction.

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/PramitKumarPanda18/ecovision-ai-deep-learning-powered-waste-recognition-system.git
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit Application

```bash
streamlit run app.py
```

---

## 📂 Project Structure

```text
EcoVision-AI
│
├── app.py
├── waste_classifier_model.h5
├── waste_classifier.ipynb
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🛠️ Technology Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| TensorFlow | Deep Learning Framework |
| Keras | Model Development |
| MobileNetV2 | Transfer Learning |
| NumPy | Numerical Computing |
| Matplotlib | Data Visualization |
| Streamlit | Web Deployment |

---

## 🌍 Applications

- Smart Recycling Systems
- Automated Waste Segregation
- Sustainable Waste Management
- Environmental Monitoring Solutions
- Smart City Infrastructure

---

## 🔮 Future Enhancements

- Real-Time Camera-Based Detection
- IoT Smart Bin Integration
- TensorFlow Lite Deployment
- Expanded Multi-Class Waste Dataset
- Mobile Application Integration

---



### ♻️ EcoVision AI — Transforming Waste Management Through Intelligent Computer Vision
