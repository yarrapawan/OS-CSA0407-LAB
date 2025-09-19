import os
import pickle

# Employee structure: [id, name, salary]
employees = [
    [101, "Alice", 50000],
    [102, "Bob", 60000],
    [103, "Charlie", 55000],
]

# Write employees to a binary file
file = open("employees.dat", "wb")
for emp in employees:
    pickle.dump(emp, file)
file.close()
print("Employee records written to file.")

# Random access: Read specific employee
file = open("employees.dat", "rb")
# Seek to 2nd employee (index 1)
index = 1
for i in range(index + 1):
    emp = pickle.load(file)
print(f"Random access: Employee at index {index} -> {emp}")
file.close()
