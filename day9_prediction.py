import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load the dataset
data = pd.read_csv("student_scores.csv")

# Input (Hours) and Output (Scores)
X = data[["Hours"]]
y = data["Scores"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict scores for the test data
predictions = model.predict(X_test)

# Display actual and predicted scores
result = pd.DataFrame({
    "Study Hours": X_test["Hours"].values,
    "Actual Score": y_test.values,
    "Predicted Score": predictions
})

print("Prediction Results:")
print(result)
hours = 6.5
predicted_score = model.predict([[hours]])

print(f"\nPredicted score for {hours} study hours: {predicted_score[0]:.2f}")