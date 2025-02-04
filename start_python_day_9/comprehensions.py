# কম্প্রিহেনশন হলো পাইথনের একটি শর্টকাট নিয়ম যা দিয়ে লিস্ট, ডিকশনারি, সেট তৈরি করা যায়

# List Comprehension Example
# সাধারণ for লুপের পরিবর্তে একলাইনে লিস্ট তৈরি
numbers = [1, 2, 3, 4, 5]
squares = [num * num for num in numbers]
print("Example-1:- List Comprehension:", squares)  # Output: [1, 4, 9, 16, 25]

# Dictionary Comprehension Example
# ডিকশনারি কম্প্রিহেনশন দিয়ে কী-ভ্যালু পেয়ার তৈরি
dict_comp = {x: x*x for x in range(4)}
# Output: {0: 0, 1: 1, 2: 4, 3: 9}
print("\nExample-2:- Dict Comprehension:", dict_comp)

# Set Comprehension Example
# সেট কম্প্রিহেনশন দিয়ে ডুপ্লিকেট ভ্যালু বাদ দিয়ে সেট তৈরি
set_comp = {num % 3 for num in range(10)}
print("\nExample-3:- Set Comprehension:", set_comp)  # Output: {0, 1, 2}

# Conditional Comprehension
# শর্তসাপেক্ষে কম্প্রিহেনশন
even_nums = [x for x in range(10) if x % 2 == 0]
print("\nExample-4:- Conditional Comprehension:",
      even_nums)  # Output: [0, 2, 4, 6, 8]
