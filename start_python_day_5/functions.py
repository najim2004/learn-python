# ১) Basic Function (সাধারণ ফাংশন)
def greet():
    print("1. Hello World")

# ২) Function with Parameters (প্যারামিটার সহ ফাংশন)
def add_numbers(a, b):
    print("2. Sum:", a + b)
    return a + b

# ৩) Default Parameter (ডিফল্ট প্যারামিটার সহ ফাংশন)
def greet_person(name="Guest"):
    print("3. Welcome", name)

# ৪) Multiple Parameters (একাধিক প্যারামিটার সহ ফাংশন)
def calculate_price(price, discount, tax):
    final_price = price - (price * discount/100) + (price * tax/100)
    print("4. Final Price:", final_price)
    return final_price

# ৫) *args - Variable Arguments (পরিবর্তনশীল সংখ্যক আর্গুমেন্ট)
def sum_all(*numbers):
    print("5. Sum of all numbers:", sum(numbers))
    return sum(numbers)

# ৬) **kwargs - Keyword Arguments (কীওয়ার্ড আর্গুমেন্ট)
def student_info(**kwargs):
    print("6. Student Information:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# উদাহরণ কিভাবে ফাংশনগুলো ব্যবহার করতে হয়
if __name__ == "__main__":
    # Basic function call
    greet()
    
    # Function with parameters
    add_numbers(5, 3)
    
    # Default parameter function
    greet_person()  # Uses default value
    greet_person("John")  # Uses provided value
    
    # Multiple parameters
    calculate_price(100, 10, 5)
    
    # Variable arguments
    sum_all(1, 2, 3, 4, 5)
    
    # Keyword arguments
    student_info(name="Rahim", age=20, grade="A")