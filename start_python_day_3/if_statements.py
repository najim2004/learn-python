# এইটা একটা বুলিয়ান ভেরিয়েবল যা true/false ভ্যালু রাখে
is_hot=True

# যদি is_hot true হয় তাহলে এই ব্লক এক্সিকিউট হবে
if is_hot:
    print("1. It's a hot day")
    print("2. Drink plenty of water")
# যদি is_hot false হয় তাহলে এই ব্লক এক্সিকিউট হবে
else:
    print("3. It's a cold day")
    print("4. Wear warm clothes")
# এই লাইন সবসময় এক্সিকিউট হবে
print("5. Enjoy your day")

# যদি গরম হয়
is_hot = True
# যদি ঠান্ডা হয়
is_cold = False

# যদি গরম হয় তাইলে
if is_hot:
    print("6. Hot day")
    print("7. Drink lots of water")
# যদি ঠান্ডা হয় তাইলে    
elif is_cold:
    print("8. Cold day")
    print("9. Wear warm clothes")
# যদি কোনটাই না হয় তাইলে
else:
    print("10. Beautiful day")
    print("11. Enjoy")

# একটা নাম্বারের জন্য
number = 5

# যদি নাম্বার ০ এর চেয়ে বড় হয়
if number > 0:
    print("12. Positive number")
# যদি নাম্বার ০ এর চেয়ে ছোট হয়
elif number < 0:
    print("13. Negative number")
# যদি নাম্বার ০ হয়
else:
    print("14. Zero")

# দুইটা কন্ডিশন এক সাথে চেক করার জন্য
age = 25
income = 5000

if age >= 18 and income > 3000:
    print("15. You can get a loan")

# যেকোনো একটা কন্ডিশন সত্য হলেই হবে
has_credit_card = True
has_cash = False

if has_credit_card or has_cash:
    print("16. You can buy something")

# লিস্টের মধ্যে কিছু আছে কিনা চেক করা
fruits = ["apple", "orange", "mango"]
if "mango" in fruits:
    print("17. Mango is available")

# রেঞ্জের মধ্যে আছে কিনা চেক করা
score = 85
if 80 <= score <= 100:
    print("18. You got A+")

# স্ট্রিং খালি কিনা চেক করা
name = ""
if not name:
    print("19. Name is empty")
    
# বাড়ির দাম সেট করা হয়েছে
house_price = 1000000
# ক্রেডিট স্কোর ভালো কিনা সেটা বুলিয়ান ভেরিয়েবল দিয়ে সেট করা হয়েছে
has_good_credit = True

# যদি ক্রেডিট স্কোর ভালো হয়
if has_good_credit:
    # তাহলে ডাউন পেমেন্ট হবে মূল্যের ১০%
    down_payment = 0.1 * house_price
# যদি ক্রেডিট স্কোর ভালো না হয়
else:
    # তাহলে ডাউন পেমেন্ট হবে মূল্যের ২০%
    down_payment = 0.2 * house_price

# ডাউন পেমেন্টের পরিমাণ প্রিন্ট করা
print(f"20. Down payment: ${down_payment}")