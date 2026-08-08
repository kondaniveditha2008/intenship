# Import the libraries we need
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load the student score dataset
data = pd.read_csv("student_scores.csv")

# Select study hours and scores
X = data[["Hours"]]
y = data["Scores"]

# Split the data into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create the Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Display a message
print("Model trained successfully!")