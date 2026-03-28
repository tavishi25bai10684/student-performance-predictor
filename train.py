import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

# Load dataset
data = pd.read_csv("data/student_data.csv")

X = data[['StudyHours', 'Attendance', 'SleepHours', 'PreviousMarks']]
y = data['Result']

# Train model
model = LogisticRegression()
model.fit(X, y)

# Save model
joblib.dump(model, "model/student_model.pkl")

print("Model saved successfully!")