import math

# গানিতিক অপারেশন গুলোর জন্য math মডিউল ইম্পোর্ট করা

# মান গুলো
number = 16  # এখানে আপনার ইচ্ছামত সংখ্যা দিতে পারেন
base = 2
power = 3
a = 10
b = 20
decimal_number = 3.7

# বর্গমূল
square_root = math.sqrt(number)
print("1. Square root of", number, "is:", square_root)

# ঘাত/পাওয়ার
power_result = math.pow(base, power)
print("2. Power of", base, "raised to", power, "is:", power_result)

# সর্বনিম্ন সংখ্যা
minimum = min(a, b)
print("3. Minimum between", a, "and", b, "is:", minimum)

# সর্বোচ্চ সংখ্যা
maximum = max(a, b)
print("4. Maximum between", a, "and", b, "is:", maximum)

# পূর্ণসংখ্যায় রাউন্ড
rounded = round(decimal_number)
print("5. Rounded value of", decimal_number, "is:", rounded)

# সিলিং - উপরের পূর্ণসংখ্যায় রাউন্ড
ceiling = math.ceil(decimal_number)
print("6. Ceiling value of", decimal_number, "is:", ceiling)

# ফ্লোর - নিচের পূর্ণসংখ্যায় রাউন্ড
floor = math.floor(decimal_number)
print("7. Floor value of", decimal_number, "is:", floor)

# পরম মান (অ্যাবসলিউট)
absolute = abs(-10)
print("8. Absolute value of -10 is:", absolute)

# ফ্যাক্টোরিয়াল
factorial = math.factorial(5)
print("9. Factorial of 5 is:", factorial)

# পাই (π) এর মান
PI = math.pi
print("10. Value of PI (π) is:", PI)

# ই (e) এর মান
E = math.e
print("11. Value of E (e) is:", E)
