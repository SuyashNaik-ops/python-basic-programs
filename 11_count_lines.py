file_name = input("Enter file name: ")

with open(file_name, "r") as file:
    lines = file.readlines()

print("Total number of lines:", len(lines))