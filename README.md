♻️ EcoVision AI
Deep Learning Powered Waste Recognition System

EcoVision AI is an AI-driven computer vision system designed to intelligently classify waste materials using deep convolutional neural networks and transfer learning. The system leverages a pre-trained MobileNetV2 architecture to perform high-accuracy waste classification and is deployed through an interactive Streamlit web interface for real-time inference.

This project demonstrates the integration of deep learning, computer vision, and lightweight deployment frameworks to create an intelligent waste recognition pipeline that can support smart recycling and automated waste management systems.

🚀 Key Features

Transfer Learning Architecture using MobileNetV2 for efficient feature extraction

Deep Convolutional Neural Network optimized for multi-class image classification

Data Augmentation Pipeline to improve generalization and mitigate overfitting

Real-time Image Inference via an interactive Streamlit web interface

GPU-accelerated training using TensorFlow

Lightweight deployment-ready architecture

🧠 Model Architecture

The system employs transfer learning by utilizing a pre-trained MobileNetV2 backbone trained on the ImageNet dataset.

Architecture Pipeline
Input Image (224×224)
        │
        ▼
MobileNetV2 (Pretrained Feature Extractor)
        │
        ▼
GlobalAveragePooling2D
        │
        ▼
Dense Layer (128 neurons, ReLU)
        │
        ▼
Dense Layer (64 neurons, ReLU)
        │
        ▼
Softmax Output Layer (5 Waste Classes)

This architecture significantly reduces training complexity while preserving high feature representation quality.

📊 Dataset

The model was trained on a multi-class waste classification dataset containing labeled images across multiple waste categories.

Classes Used

Cardboard

Metal

Paper

Plastic

Trash

Images were split into training and validation datasets with an 80/20 distribution.

⚙️ Data Preprocessing Pipeline

The dataset undergoes a data augmentation pipeline to enhance model robustness.

Applied transformations include:

Random Rotation

Horizontal Flipping

Zoom Augmentation

Shear Transformation

Pixel Normalization

These transformations increase dataset diversity and improve model generalization capability.

📈 Model Training

The model was trained using TensorFlow/Keras with GPU acceleration.

Training Configuration
Parameter	Value
Image Size	224×224
Batch Size	32
Epochs	10
Optimizer	Adam
Loss Function	Categorical Crossentropy

Training was performed using transfer learning, where the MobileNetV2 feature extractor layers were frozen during initial training.

📉 Performance Evaluation

Model performance was evaluated using:

Validation Accuracy

Loss Curves

Confusion Matrix

The trained model demonstrates strong classification capability across the waste categories with robust generalization performance.

🌐 Streamlit Web Application

The project includes a fully interactive web interface built with Streamlit.

Features of the Web App

Image Upload Interface

Real-time Waste Classification

Model Inference Visualization

Users can upload an image of waste material and the system will instantly predict its category.

🖥️ Running the Application
Clone Repository
git clone https://github.com/yourusername/EcoVision-AI.git
Install Dependencies
pip install -r requirements.txt
Run Streamlit Application
streamlit run app.py

Then open:

http://localhost:8501
📂 Project Structure
EcoVision-AI
│
├── dataset/
├── app.py
├── waste_classifier_model.h5
├── waste_classifier.ipynb
├── requirements.txt
├── README.md
└── .gitignore
🧩 Technology Stack
Technology	Purpose
TensorFlow	Deep Learning Framework
Keras	Model Development
MobileNetV2	Transfer Learning Backbone
NumPy	Numerical Computation
Matplotlib	Data Visualization
Streamlit	Web Application Interface
🌍 Potential Applications

EcoVision AI can be extended for several real-world applications:

Smart recycling systems

Automated waste segregation

AI-powered sustainability tools

Smart city infrastructure

Industrial waste management automation

📌 Future Improvements

Real-time camera-based waste detection

Integration with IoT-enabled smart bins

Edge deployment using TensorFlow Lite

Expansion to larger multi-category waste datasets

👨‍💻 Author

Developed as part of an AI/ML computer vision project focusing on sustainable AI solutions and
