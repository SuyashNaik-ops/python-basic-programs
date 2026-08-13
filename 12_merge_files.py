file1 = input("Enter first file name: ")
file2 = input("Enter second file name: ")
output_file = input("Enter output file name: ")

with open(file1, "r") as f1:
    data1 = f1.read()

with open(file2, "r") as f2:
    data2 = f2.read()

with open(output_file, "w") as output:
    output.write(data1)
    output.write("\n")
    output.write(data2)

print("Files merged successfully.")