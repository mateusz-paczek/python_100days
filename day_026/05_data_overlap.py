# Read first file
with open("file1.txt") as f1:
    f1_list = f1.readlines()
print(f1_list)

with open("file2.txt") as f2:
    f2_list = f2.readlines()
print(f2_list)

result = [int(num) for num in f1_list if num in f2_list]
print(result)