import pandas as pd

# Load the dataset
data = pd.read_csv("student_scores.csv")

# Display the first 5 rows
print("First 5 Rows:")
print(data.head())

# Display the last 5 rows
print("\nLast 5 Rows:")
print(data.tail())

# Display the shape of the dataset
print("\nDataset Shape:")
print(data.shape)

# Display column names
print("\nColumn Names:")
print(data.columns)

# Display dataset information
print("\nDataset Information:")
print(data.info())
