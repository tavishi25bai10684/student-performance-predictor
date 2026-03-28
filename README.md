# Student Performance Predictor

## 📌 Description
This project is an AI/ML-based application that predicts whether a student will pass or fail based on input features such as study hours, attendance, sleep hours, and previous marks. The model is built using Logistic Regression.

---

## ⚙️ Setup Instructions

1. Install Python (version 3.x recommended)
2. Download or clone this repository
3. Open terminal in the project folder

---

## 📦 Dependencies Installation

Install required libraries using the following command:

pip install -r requirements.txt

---

## ⚙️ Configuration Steps

1. Ensure the dataset file is present at:
   data/student_data.csv

2. Ensure the following folder structure exists:

student-performance-predictor/
│── data/
│     └── student_data.csv
│── src/
│     ├── main.py
│     └── train.py
│── model/
│── requirements.txt
│── README.md

3. The model file will be automatically created in the `model/` folder after training.

---

## ▶️ Execution Steps

### Step 1: Train the Model

Run the following command in terminal:

python src/train.py

This will train the model and save it in:
model/student_model.pkl

---

### Step 2: Run Prediction

Run the following command:

python src/main.py

Enter the required input values when prompted.

---

## 📌 Output

- Displays model accuracy
- Predicts whether the student will Pass or Fail

---

## 🧠 Algorithm Used

- Logistic Regression

---  

Name - Tavishi gupta
Registration No. :- 25BAI10684
