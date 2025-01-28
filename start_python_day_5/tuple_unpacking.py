# Tuple unpacking examples with real-world scenarios

# Example 1 - coordinates
# কোনো পয়েন্টের x, y কো-অর্ডিনেট আনপ্যাক করা
print("1. Coordinate Unpacking:")
point = (10, 20)
x, y = point
print(f"X coordinate: {x}, Y coordinate: {y}\n")

# Example 2 - person info
# ব্যক্তিগত তথ্য আনপ্যাক করা
print("2. Personal Information Unpacking:")
person = ("John Doe", 25, "Software Engineer")
name, age, profession = person
print(f"Name: {name}, Age: {age}, Profession: {profession}\n")

# Example 3 - product details
# পণ্যের বিবরণ আনপ্যাক করা
print("3. Product Details Unpacking:")
product = ("Laptop", 999.99, 50)
product_name, price, stock = product
print(f"Product: {product_name}, Price: ${price}, Stock: {stock}\n")

# Example 4 - swapping variables
# দুটি ভ্যারিয়েবলের মান আদান-প্রদান করা
print("4. Variable Swapping:")
a, b = 5, 10
print(f"Before swap: a = {a}, b = {b}")
a, b = b, a
print(f"After swap: a = {a}, b = {b}\n")

# Example 5 - returning multiple values from function
# ফাংশন থেকে একাধিক মান রিটার্ন করা
print("5. Function Return Unpacking:")
def get_circle_info(radius):
    area = 3.14 * radius * radius
    circumference = 2 * 3.14 * radius
    return (area, circumference)

radius = 5
circle_area, circle_circumference = get_circle_info(radius)
print(f"Circle with radius {radius}:")
print(f"Area: {circle_area:.2f}, Circumference: {circle_circumference:.2f}")