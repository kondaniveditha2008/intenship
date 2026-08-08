import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


data = pd.read_csv("data/student_scores.csv")


X = data[["Hours"]]
y = data["Scores"]


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


model = LinearRegression()

model.fit(X_train, y_train)


hours = float(input("Enter study hours: "))

predicted_score = model.predict([[hours]])


print("--------------------------------")
print("Student Score Prediction")
print("--------------------------------")
print("Study Hours:", hours)
print("Predicted Score:", round(predicted_score[0], 2))