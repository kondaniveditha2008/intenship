import pandas as pd
from sklearn.model_selection import train_test_split

# Load the dataset
data = pd.read_csv("student_scores.csv")

# Input (Hours) and Output (Scores)
X = data[["Hours"]]
y = data["Scores"]

# Split the dataset into Training (80%) and Testing (20%)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Display the results
print("Total Records:", len(data))
print("Training Records:", len(X_train))
print("Testing Records:", len(X_test))

print("\nTraining Data:")
print(X_train)

print("\nTesting Data:")
print(X_test)