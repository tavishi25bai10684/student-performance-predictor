import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Load dataset
data = pd.read_csv("C:/Users/admin/OneDrive/Desktop/student-performance-predictor/data/student_data.csv")

# Select features and target
X = data[['StudyHours', 'Attendance', 'SleepHours', 'PreviousMarks']]
y = data['Result']

# Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create and train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Print model accuracy
accuracy = model.score(X_test, y_test)
print("Model Accuracy:", accuracy)

# Take input from user
print("\nEnter student details:")

study = float(input("Study Hours: ") or 0)
attendance = float(input("Attendance (%): ") or 0)
sleep = float(input("Sleep Hours: ") or 0)
marks = float(input("Previous Marks: ") or 0)

# Predict result
prediction = model.predict([[study, attendance, sleep, marks]])

# Display result
if prediction[0] == 1:
    print("Prediction: PASS ✅")
else:
    print("Prediction: FAIL ❌")