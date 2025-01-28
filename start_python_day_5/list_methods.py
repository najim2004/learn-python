# Some important list methods:

# Creating dataset
dataset = [23, 45, 12, 67, 34, 89, 56, 78]

# ১. append() - শেষে নতুন ডেটা যোগ করা 
# Example: Adding a new student's exam score
dataset.append(91)

# ২. extend() - একাধিক ডেটা একসাথে যোগ করা
# Example: Adding scores from another class
new_scores = [88, 76, 82]
dataset.extend(new_scores)

# ৩. sort() - ডেটা ক্রমানুসারে সাজানো
# Example: Arranging scores in ascending order
dataset.sort()

# ৪. reverse() - ডেটার ক্রম উল্টানো
# Example: Arranging scores in descending order
dataset.sort(reverse=True)

# ৫. index() - কোন ডেটার অবস্থান জানা
# Example: Finding position of a score
position = dataset.index(91)

# ৬. count() - কোন ডেটা কতবার আছে গণনা
# Example: Counting frequency of a score
frequency = dataset.count(88)

# ৭. remove() - নির্দিষ্ট ডেটা মুছে ফেলা
# Example: Removing an incorrect score
dataset.remove(12)

# ৮. pop() - নির্দিষ্ট পজিশনের ডেটা মুছে ফেলা
# Example: Removing the last entered score
last_score = dataset.pop()

# ৯. clear() - সম্পূর্ণ লিস্ট খালি করা
# Example: Resetting data for new semester
temp_list = dataset.copy()
temp_list.clear()

print("1. Processed Dataset:", dataset)

# ১০. copy() - লিস্টের একটি কপি তৈরি করা
# Example: Creating copy for experimentation
dataset_copy = dataset.copy()

# ১১. insert() - নির্দিষ্ট পজিশনে নতুন ডেটা ঢোকানো
# Example: Adding missing score
dataset.insert(0, 95)

# ১২. sum() - লিস্টের সকল এলিমেন্টের যোগফল
# Example: Total score calculation
total_score = sum(dataset)

# ১৩. len() - লিস্টের সাইজ মাপা
# Example: Total number of students
total_students = len(dataset)

# ১৪. max() এবং min() - সর্বোচ্চ ও সর্বনিম্ন মান
# Example: Highest and lowest scores
highest_score = max(dataset)
lowest_score = min(dataset)

print("\nStatistical Information:")
print("2. Total Students:", total_students)
print("3. Highest Score:", highest_score)
print("4. Lowest Score:", lowest_score)
print("5. Average Score:", total_score/total_students)