import json

data = {
    "name": "Suyash",
    "age": 20,
    "course": "AI and Data Science"
}

# Create JSON file
with open("student.json", "w") as file:
    json.dump(data, file, indent=4)

print("JSON file created successfully.")

# Read JSON file
with open("student.json", "r") as file:
    student_data = json.load(file)

print("\nData read from JSON file:")
print(student_data)

print("Name:", student_data["name"])
print("Course:", student_data["course"])