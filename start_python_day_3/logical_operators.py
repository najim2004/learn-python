# এন্ড অপারেটর (&&) - দুইটা কন্ডিশন-ই true হতে হবে
# উদাহরণ: লোন অ্যাপ্রুভাল এর জন্য income এবং credit score দুইটাই ভালো হতে হবে
has_high_income = True
has_good_credit = True
if has_high_income and has_good_credit:
    print("Eligible for loan")

# অর অপারেটর (||) - যেকোনো একটা কন্ডিশন true হলেই হবে
# উদাহরণ: স্টুডেন্ট ডিসকাউন্ট পাওয়ার জন্য student ID অথবা senior citizen card এর যেকোনো একটা থাকলেই হবে
is_student = True
is_senior_citizen = False
if is_student or is_senior_citizen:
    print("Eligible for discount")

# নট অপারেটর (!) - কন্ডিশন টা উল্টা করে দেয়
# উদাহরণ: ওয়েবসাইট এ লগড ইন না থাকলে লগিন পেজ দেখাবে
is_logged_in = False
if not is_logged_in:
    print("Please log in first")

# কম্বাইন্ড অপারেটর
# উদাহরণ: ড্রাইভিং লাইসেন্স পাওয়ার জন্য বয়স ১৮+ এবং (লার্নার পারমিট অথবা ড্রাইভিং স্কুল সার্টিফিকেট) থাকতে হবে
age = 19
has_learner_permit = True
has_driving_certificate = False
if age >= 18 and (has_learner_permit or has_driving_certificate):
    print("Eligible for driving license")

# উদাহরণ: অনলাইন গেম খেলার জন্য (প্রিমিয়াম ইউজার অথবা সাবস্ক্রিপশন আছে) এবং ইন্টারনেট কানেকশন থাকতে হবে
is_premium_user = True
has_subscription = False
has_internet = True
if (is_premium_user or has_subscription) and has_internet:
    print("You can play the game")

# উদাহরণ: রেস্টুরেন্ট এ স্পেশাল ডিসকাউন্ট - (জন্মদিন অথবা বিবাহবার্ষিকী) এবং মিনিমাম অর্ডার ১০০০ টাকা
is_birthday = True
is_anniversary = False
order_amount = 1500
if (is_birthday or is_anniversary) and order_amount >= 1000:
    print("You get special discount")