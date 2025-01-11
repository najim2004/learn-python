# ১. স্কুলের ক্লাস এবং ছাত্রদের উদাহরণ
print("\n--- Example 1: School Classes and Students ---")
classes = ["Class 6", "Class 7", "Class 8"]
students = ["Rahim", "Karim", "Salam"]

for cls in classes:
    print(f"\n{cls} Students List:")
    for student in students:
        print(f"- {student}")

# ২. সাপ্তাহিক রুটিনের উদাহরণ
print("\n--- Example 2: Weekly Routine ---")
weeks = ["Week 1", "Week 2"]
days = ["Sunday", "Monday", "Tuesday"]

for week in weeks:
    print(f"\n{week}:")
    for day in days:
        print(f"- {day}")

# ৩. মাল্টিপ্লিকেশন টেবিল (নামতা)
print("\n--- Example 3: Multiplication Table ---")
for i in range(1, 4):  # Multiplication table from 1 to 3
    print(f"\nMultiplication table of {i}:")
    for j in range(1, 6):  # Multiply by 1 to 5
        print(f"{i} x {j} = {i*j}")

# ৪. শপিং মল এবং দোকানের উদাহরণ
print("\n--- Example 4: Shopping Mall ---")
floors = ["Ground Floor", "1st Floor", "2nd Floor"]
shops = ["Clothing Store", "Shoe Store", "Food Court"]

for floor in floors:
    print(f"\n{floor}:")
    for shop in shops:
        print(f"- {shop}")