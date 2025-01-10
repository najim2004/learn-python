# ওজন ইনপুট নেওয়া হচ্ছে
weight=input("Enter your weight: ")
# ইউনিট ইনপুট নেওয়া হচ্ছে (পাউন্ড নাকি কেজি)
unit=input("Enter your unit (L for Lbs and K for Kg): ")

# যদি ইউনিট L হয় (পাউন্ড থেকে কেজিতে রূপান্তর)
if unit.upper() == "L":
    converted_weight = int(weight) * 0.45
    print(f"Your weight is {converted_weight} Kg")
# যদি ইউনিট K হয় (কেজি থেকে পাউন্ডে রূপান্তর)
else:
    converted_weight = int(weight) / 0.45
    print(f"Your weight is {converted_weight} Lbs")
