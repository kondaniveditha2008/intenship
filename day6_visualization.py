import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("student_scores.csv")


plt.figure(figsize=(6,4))
plt.scatter(data["Hours"], data["Scores"])
plt.title("Study Hours vs Scores")
plt.xlabel("Study Hours")
plt.ylabel("Scores")
plt.grid(True)
plt.show()

plt.figure(figsize=(6,4))
plt.plot(data["Hours"], data["Scores"], marker="o")
plt.title("Study Hours vs Scores (Line Chart)")
plt.xlabel("Study Hours")
plt.ylabel("Scores")
plt.grid(True)
plt.show()


plt.figure(figsize=(8,4))
plt.bar(range(len(data)), data["Scores"])
plt.title("Student Scores")
plt.xlabel("Student Number")
plt.ylabel("Score")
plt.show()