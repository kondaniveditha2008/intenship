import numpy as np


numbers = np.array([10, 20, 30, 40, 50])

# Print the array
print("Array:", numbers)


print("First element:", numbers[0])
print("Second element:", numbers[1])
print("Last element:", numbers[-1])

# Slicing
print("Elements from index 1 to 3:", numbers[1:4])


a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Mathematical operations
print("Addition:", a + b)
print("Subtraction:", b - a)
print("Multiplication:", a * b)
print("Division:", b / a)


print("Sum:", np.sum(numbers))
print("Average:", np.mean(numbers))
print("Maximum:", np.max(numbers))
print("Minimum:", np.min(numbers))

marks = np.array([70, 85, 90, 65, 80])

print("Marks:", marks)
print("Average Marks:", np.mean(marks))
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))