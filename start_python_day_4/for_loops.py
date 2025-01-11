# ১. লিস্টের মধ্যে থেকে সব ফলের নাম প্রিন্ট করা
fruits = ['Mango', 'Berry', 'Banana', 'Lichi', 'Pineapple']
for fruit in fruits:
    print(f"1. Fruit name: {fruit}")

# ২. ১ থেকে ১০ পর্যন্ত সংখ্যার যোগফল বের করা
sum = 0
for num in range(1, 11):
    sum += num
print(f"2. Sum of numbers from 1 to 10: {sum}")

# ৩. ছাত্রদের পরীক্ষার নম্বর থেকে গড় বের করা
marks = [85, 92, 78, 65, 98]
total = 0
for mark in marks:
    total += mark
average = total / len(marks)
print(f"3. Average marks: {average}")

# ৪. শব্দের প্রতিটি অক্ষর আলাদা করে দেখানো
word = "Bangladesh"
for letter in word:
    print(f"4. Letter: {letter}")

# ৫. ডিকশনারি থেকে ছাত্রদের তথ্য প্রিন্ট করা
students = {
    "Rahim": "Class 5",
    "Karim": "Class 6",
    "Salma": "Class 7"
}
for name, class_name in students.items():
    print(f"5. Name: {name}, Class: {class_name}")

# ৬. ১ থেকে ২০ পর্যন্ত জোড় সংখ্যা প্রিন্ট করা
for num in range(2, 21, 2):
    print(f"6. Even number: {num}")