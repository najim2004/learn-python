import os
from pathlib import Path

# ১) ফাইলে লেখার জন্য
with open("test.txt", "w") as file:
    file.write("Hello, Python!")
print("File 'test.txt' has been written successfully.")

# ২) ফাইল থেকে পড়ার জন্য
with open("test.txt", "r") as file:
    content = file.read()
    print("Content of 'test.txt':", content)

# ৩) বর্তমান ডিরেক্টরির সব ফাইল এবং ফোল্ডার দেখার জন্য
print("Files and folders in current directory:", os.listdir("."))

# ৪) নতুন ফোল্ডার তৈরি করার জন্য
folder_name = "new_folder"
os.makedirs(folder_name, exist_ok=True)
print(f"Folder '{folder_name}' created successfully.")

# ৫) কোন ফাইল বা ফোল্ডার আছে কিনা চেক করার জন্য
if os.path.exists(folder_name):
    print(f"The folder '{folder_name}' exists.")
else:
    print(f"The folder '{folder_name}' does not exist.")

# ৬) প্যাথলিব ব্যবহার করে সব ফাইল এবং ফোল্ডার দেখার জন্য
path = Path(".")
print("Listing files and folders using Pathlib:")
for item in path.iterdir():
    print(item)

# ৭) প্যাথলিব ব্যবহার করে ফাইল আছে কিনা চেক করার জন্য
file_path = Path("test.txt")
if file_path.exists():
    print(f"The file '{file_path}' exists.")
else:
    print(f"The file '{file_path}' does not exist.")

# ৮) প্যাথলিব ব্যবহার করে নতুন ফোল্ডার তৈরি করার জন্য
Path("another_folder").mkdir(exist_ok=True)
print("Folder 'another_folder' created successfully.")

# ৯) ফাইল মুছে ফেলার জন্য
if os.path.exists("test.txt"):
    os.remove("test.txt")
    print("File 'test.txt' has been deleted successfully.")
else:
    print("File 'test.txt' not found.")
