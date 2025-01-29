# এখানে আমরা পাইথন এর বিভিন্ন Exception হ্যান্ডলিং শিখবো
# Exception হলো এমন একটি ঘটনা যা প্রোগ্রাম এক্সিকিউশন এর সময় ঘটে

# 1. Basic Try-Except
try:
    print("1. Basic division example:")
    result = 10 / 0  # Division by zero error
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# 2. Multiple Exception Handling
# একাধিক Exception একসাথে হ্যান্ডেল করা
try:
    print("\n2. List index error example:")
    numbers = [1, 2, 3]
    print(numbers[5])  # Index out of range
    result = 10 / 0
except IndexError:
    print("Error: List index out of range!")
except ZeroDivisionError:
    print("Error: Division by zero!")

# 3. Try-Except-Else-Finally
# else: যদি কোন error না হয়
# finally: error হোক বা না হোক এটা execute হবে
try:
    print("\n3. File handling example:")
    file = open("non_existent_file.txt", "r")
except FileNotFoundError:
    print("Error: File not found!")
else:
    print("File operations successful!")
finally:
    print("This will always execute!")


# 4. Real-world Example: Database Connection
# ডাটাবেস কানেকশন এরর হ্যান্ডলিং
def connect_to_database():
    raise ConnectionError("Database connection failed!")


try:
    print("\n4. Database connection example:")
    connect_to_database()
except ConnectionError as e:
    print(f"Error: {e}")


# 5. Custom Exception
# নিজস্ব Exception তৈরি করা
class InsufficientBalanceError(Exception):
    pass


def withdraw_money(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError("Insufficient funds!")
    return balance - amount


try:
    print("\n5. Banking transaction example:")
    balance = 1000
    withdraw_money(balance, 1500)
except InsufficientBalanceError as e:
    print(f"Error: {e}")

# 6. Validating User Input
# ইউজার ইনপুট ভ্যালিডেশন
try:
    print("\n6. User input validation example:")
    age = -20
    if age < 0:
        raise ValueError("Age cannot be negative!")
except ValueError as e:
    print(f"Error: Please enter a valid age!")

# 7. Type Error Handling
try:
    print("\n7. Type error example:")
    text = "hello"
    number = 5
    result = text + number
except TypeError as e:
    print(f"Error: Cannot add string and number!")

# 8. Key Error in Dictionary
try:
    print("\n8. Dictionary key error example:")
    my_dict = {"name": "John", "age": 30}
    print(my_dict["address"])
except KeyError as e:
    print(f"Error: Key not found in dictionary!")

# 9. Attribute Error
try:
    print("\n9. Attribute error example:")
    number = 42
    number.append(10)  # integers don't have append method
except AttributeError as e:
    print(f"Error: Object doesn't have this attribute!")

# 10. Import Error
try:
    print("\n10. Import error example:")
    import non_existent_module
except ImportError as e:
    print(f"Error: Module not found!")

# 11. Multiple Error Types in One Except Block
try:
    print("\n11. Multiple errors example:")
    data = [1, 2, 3]
    value = data[5] / 0
    result = "text" + 5
except (IndexError, ZeroDivisionError, TypeError) as e:
    print(f"Error: Caught one of multiple possible errors! {type(e).__name__}")
