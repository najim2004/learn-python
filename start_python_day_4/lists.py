# বিভিন্ন ধরনের লিস্ট এর উদাহরণ

# ১. ছাত্র-ছাত্রীদের নামের তালিকা
students = ["Rahim", "Karim", "Salma", "Ruby", "Jasim"]

# ২. একটি দোকানের পণ্যের দাম (টাকায়)
product_prices = [50.5, 120.0, 30.75, 240.25, 85.0]

# ৩. একজন ছাত্রের বিভিন্ন বিষয়ে পরীক্ষার ফলাফল
exam_scores = [85, 92, 78, 95, 88]

# ৪. মিশ্র তথ্য সম্বলিত লিস্ট (নাম, বয়স, উচ্চতা)
person_info = ["Kamal", 25, 5.7, "Dhaka"]

# ৫. দৈনিক তাপমাত্রার রেকর্ড (সেলসিয়াস)
temperatures = [23, 25, 28, 30, 27, 24, 26]

# ৬. টু-ডু লিস্ট
todo_list = ["Shopping", "Go to Bank", "Doctor's Appointment", "Read Book"]

# ৭. নেস্টেড লিস্ট (একটি স্কুলের ক্লাস এবং ছাত্র সংখ্যা)
school_data = [
    ["Class 6", 45],
    ["Class 7", 52],
    ["Class 8", 48]
]

# ৮. সংখ্যার লিস্টে সবচেয়ে বড় সংখ্যা
numbers = [45, 78, 90, 23, 56, 12, 89]
largest_number = numbers[0]  # Start with first number
for num in numbers:
    if num > largest_number:
        largest_number = num


# Print statements with serial numbers
print("1. First student name:", students[0])
print("2. Total product price:", sum(product_prices))
print("3. Average temperature:", sum(temperatures) / len(temperatures))
print("4. Largest number:", largest_number)