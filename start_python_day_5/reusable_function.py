# ফাংশন কি?
# একটি ফাংশন হলো কোডের একটি পুনঃব্যবহারযোগ্য ব্লক যা একটি নির্দিষ্ট কাজ করে

def add_numbers(a, b):
    """
    This function adds two numbers and returns the result
    """
    return a + b

# কিভাবে ফাংশন পুনঃব্যবহার করা যায়?
# একবার ফাংশন লেখার পর এটি বারবার ব্যবহার করা যায়
result1 = add_numbers(5, 3)  # returns 8
result2 = add_numbers(10, 20)  # returns 30

# প্যারামিটার সহ ফাংশন
def greet_user(name, age):
    """
    This function greets user with name and age
    """
    return f"Hello {name}, you are {age} years old!"

# ডিফল্ট প্যারামিটার সহ ফাংশন
def multiply(x, y=2):
    """
    This function multiplies two numbers, y is optional
    """
    return x * y

# ফাংশনের রিটার্ন ভ্যালু
def get_user_info(first_name, last_name):
    """
    This function returns multiple values
    """
    full_name = f"{first_name} {last_name}"
    name_length = len(full_name)
    return full_name, name_length

# একটি ফাংশন অন্য ফাংশনের ভিতরে ব্যবহার করা যায়
def process_numbers(numbers):
    """
    This function processes a list of numbers using other functions
    """
    total = 0
    for num in numbers:
        # Using multiply function inside another function
        total += multiply(num)
    return total