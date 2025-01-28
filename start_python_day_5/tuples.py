# টিউপল (Tuple) হলো একটি immutable (অপরিবর্তনীয়) ডেটা স্ট্রাকচার

# ডেটা পয়েন্ট টিউপল
data_point = (25.6, 12.3, 87.2)  # Features like temperature, humidity, pressure

# ইমেজ পিক্সেল কোঅর্ডিনেট টিউপল
pixel_coordinates = [(0, 0), (100, 200), (300, 400)]  # (x, y) coordinates

# RGB কালার টিউপল
colors = [
    (255, 0, 0),    # Red
    (0, 255, 0),    # Green
    (0, 0, 255)     # Blue
]

# ক্লাসিফিকেশন লেবেল এবং প্রোবাবিলিটি
predictions = [
    ("cat", 0.95),
    ("dog", 0.85),
    ("bird", 0.75)
]

# টিউপল অপারেশন examples
# টিউপল থেকে ভ্যালু অ্যাক্সেস
first_color = colors[0]
print(f"1. First color RGB values: {first_color}")

# টিউপল আনপ্যাকিং
x, y, z = data_point
print(f"2. Temperature: {x}, Humidity: {y}, Pressure: {z}")

# টিউপল কাউন্টিং
# একই রকম ভ্যালু কতবার আছে তা গণনা
sample_data = (1, 2, 2, 3, 2, 4, 5, 2)
count_of_2 = sample_data.count(2)
print(f"3. Number 2 appears {count_of_2} times")

# টিউপল ইনডেক্সিং
# কোন ভ্যালু কোন পজিশনে আছে তা বের করা
position = sample_data.index(3)
print(f"4. Position of number 3: {position}")