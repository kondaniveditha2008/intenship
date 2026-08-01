import pandas as pd

# Load the dataset
data = pd.read_csv("student_scores.csv")

# Display original dataset
print("Original Dataset:")
print(data)

# Check for missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Remove rows with missing values (if any)
data = data.dropna()

# Remove duplicate rows (if any)
data = data.drop_duplicates()

# Display cleaned dataset
print("\nCleaned Dataset:")
print(data)

# Display statistical summary
print("\nDataset Statistics:")
print(data.describe())
# Save cleaned dataset
data.to_csv("cleaned_student_scores.csv", index=False)

print("\nCleaned dataset saved as 'cleaned_student_scores.csv'")