# ল্যাম্বডা ফাংশন সম্পর্কে সহজ ব্যাখ্যা সহ পাইথন কোড

# ল্যাম্বডা ফাংশন কি?
# এটি একটি ছোট ফাংশন যা শুধুমাত্র এক লাইনে লেখা যায় এবং এর কোনো নাম থাকে না।
# এটি সাধারণত তখন ব্যবহার করা হয় যখন অল্প কিছু কোড লিখে দ্রুত কাজ করতে হয়।

# সাধারণ ফাংশন কেমন হয়?
from functools import reduce


def add(a, b):
    return a + b


print("Normal Function Sum:", add(5, 10))  # আউটপুট: 15

# একই কাজ ল্যাম্বডা ফাংশন দিয়ে করা যায়


def sum_lambda(a, b): return a + b


print("Lambda Function Sum:", sum_lambda(5, 10))  # আউটপুট: 15

# একটি সংখ্যা বর্গফল বের করার জন্য ল্যাম্বডা ফাংশন


def square_lambda(x): return x * x


print("Lambda Square:", square_lambda(4))  # আউটপুট: 16

# লিস্টের সব সংখ্যা বর্গফল বের করতে map() ও ল্যাম্বডা ফাংশন
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("Squared Numbers:", squared_numbers)  # আউটপুট: [1, 4, 9, 16, 25]

# শুধুমাত্র জোড় সংখ্যা বের করতে filter() ও ল্যাম্বডা ফাংশন
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", even_numbers)  # আউটপুট: [2, 4]

# তালিকা (list) কে বয়স অনুযায়ী সাজানো
students = [("Alice", 25), ("Bob", 20), ("Charlie", 23)]
sorted_students = sorted(
    students, key=lambda student: student[1])  # বয়স অনুযায়ী সাজানো
# আউটপুট: [('Bob', 20), ('Charlie', 23), ('Alice', 25)]
print("Sorted Students by Age:", sorted_students)

# তালিকার সব সংখ্যার গুণফল বের করতে reduce() ও ল্যাম্বডা ফাংশন
product = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
print("Product of Numbers:", product)  # আউটপুট: 120

# ল্যাম্বডা ফাংশন দ্রুত এবং সহজ, তবে জটিল লজিকের জন্য সাধারণ ফাংশন ব্যবহার করাই ভালো।
