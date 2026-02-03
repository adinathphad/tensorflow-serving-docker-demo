# 🚀 TensorFlow Model Deployment using Docker & TensorFlow Serving

This project demonstrates how to train a simple Machine Learning model and deploy it as a production-ready REST API using Docker and TensorFlow Serving.

It covers the complete workflow:

Train → Export → Serve → API → Predict

---

## 📌 Tech Stack

- Python
- TensorFlow
- Docker
- TensorFlow Serving
- Linux
- curl (API testing)

---

## ⚙️ Setup

### 1️⃣ Install dependencies

pip install -r requirements.txt

---

### 2️⃣ Train and export the model

python model.py

This creates:

half_plus_two/1/

TensorFlow Serving requires the model inside a versioned folder.

---

## 🐳 Deploy with Docker

### Pull image (first time only)

docker pull tensorflow/serving

### Start server

docker run -d -p 9501:8501 \
--mount type=bind,source=$(pwd)/half_plus_two,target=/models/half_plus_two \
-e MODEL_NAME=half_plus_two \
tensorflow/serving

---

## 🌐 Test API

curl -X POST http://localhost:9501/v1/models/half_plus_two:predict \
-d '{"instances":[[1.0],[2.0],[5.0]]}'

---

## ✅ Expected Output

{
  "predictions": [[2.5],[3.0],[4.5]]
}

---

## 🧠 How it works

1. Train model using TensorFlow
2. Export SavedModel format
3. Mount model into Docker container
4. TensorFlow Serving exposes REST API
5. Send prediction requests using curl

---

## 📖 Learning Outcomes

- Model training
- Model export for production
- Docker containerization
- API serving
- Linux command-line usage
- DevOps-style deployment
