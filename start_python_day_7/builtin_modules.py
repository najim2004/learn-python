# 🔹 Important Built-in Modules in Python

# ✅ ১. math (গাণিতিক গণনার জন্য)
import hashlib
import socket
import urllib.request0
from collections import Counter
import re
import json
import sys
import os
import time
from datetime import datetime
import random
import math

print("\n🔹 Math Module:")
print("Square root of 5:", math.sqrt(25))
print("5! (Factorial):", math.factorial(5))
print("Value of π:", math.pi)

# ✅ ২. random (এলোমেলো সংখ্যা ও ডাটা তৈরি করতে)

print("\n🔹 Random Module:")
print("Random number between 1 and 10:", random.randint(1, 10))
print("Random fruit:", random.choice(["Apple 🍎", "Banana 🍌", "Orange 🍊"]))

# ✅ ৩. datetime (তারিখ ও সময় সংক্রান্ত কাজের জন্য)

now = datetime.now()
print("\n🔹 DateTime Module:")
print("Current date and time:", now)
print("Formatted date:", now.strftime("%Y-%m-%d %H:%M:%S"))

# ✅ ৪. time (সময় সংক্রান্ত কাজ করতে)

print("\n🔹 Time Module:")
print("Start...")
time.sleep(2)  # ২ সেকেন্ড অপেক্ষা করবে
print("End after 2 seconds")

# ✅ ৫. os (অপারেটিং সিস্টেম সম্পর্কিত কাজের জন্য)

print("\n🔹 OS Module:")
print("Current directory:", os.getcwd())
# নতুন ফোল্ডার তৈরি করবে (একবার রান করলে পরের বার ভুল দেখাবে)
os.mkdir("new_folder")

# ✅ ৬. sys (সিস্টেম সম্পর্কিত তথ্য পেতে)

print("\n🔹 Sys Module:")
print("Python version:", sys.version)
print("System platform:", sys.platform)

# ✅ ৭. json (JSON ডাটা নিয়ে কাজ করতে)

data = {"name": "Najim", "age": 20, "city": "Dhaka"}
json_data = json.dumps(data)  # Python ডাটাকে JSON এ রূপান্তর করবে
print("\n🔹 JSON Module:")
print("JSON Data:", json_data)

# ✅ ৮. re (Regex বা Regular Expression এর জন্য)

text = "My email is najim.developer@gmail.com"
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

match = re.search(pattern, text)
print("\n🔹 RE (Regex) Module:")
if match:
    print("Email Found:", match.group())  # ইমেইল এক্সট্রাক্ট করবে

# ✅ ৯. collections (উন্নত ডাটা স্ট্রাকচার নিয়ে কাজ করতে)

fruits = ["Apple 🍎", "Banana 🍌", "Orange 🍊", "Apple 🍎", "Apple 🍎", "Orange 🍊"]
count = Counter(fruits)  # প্রতিটি আইটেমের সংখ্যা গুনবে
print("\n🔹 Collections Module:")
print("Fruit count:", count)

# ✅ ১০. urllib (ইন্টারনেট থেকে ডাটা ফেচ করার জন্য)

url = "https://www.example.com"
response = urllib.request.urlopen(url)
print("\n🔹 urllib Module:")
print("Webpage HTML:\n", response.read().decode(
    "utf-8")[:100])  # প্রথম ১০০ ক্যারেক্টার দেখাবে

# ✅ ১১. socket (নেটওয়ার্ক প্রোগ্রামিং ও সার্ভার তৈরি করতে)

host = "www.google.com"
ip = socket.gethostbyname(host)
print("\n🔹 Socket Module:")
print(f"IP address of {host}:", ip)

# ✅ ১২. hashlib (ডাটা এনক্রিপশন ও হ্যাশিং করার জন্য)

password = "mypassword"
hashed = hashlib.sha256(password.encode()).hexdigest()  # SHA-256 হ্যাশ তৈরি করবে
print("\n🔹 Hashlib Module:")
print("Hashed Password:", hashed)
