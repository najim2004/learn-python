str1 = 'Hello! My name is Mohammad Najim. I am a coder.'

# strip() -> স্ট্রিং এর শুরু এবং শেষের whitespace মুছে ফেলে
print(str1.strip())

# lstrip() -> স্ট্রিং এর শুরুর whitespace মুছে ফেলে
print(str1.lstrip())

# rstrip() -> স্ট্রিং এর শেষের whitespace মুছে ফেলে
print(str1.rstrip())

# capitalize() -> শুধু প্রথম অক্ষরকে বড় হাতের করে
print(str1.capitalize())

# count() -> কোন শব্দ বা অক্ষর কতবার আছে তা গণনা করে
print(str1.count('a'))

# startswith() -> স্ট্রিং কোন শব্দ দিয়ে শুরু হয়েছে কিনা চেক করে
print(str1.startswith('Hello!'))

# endswith() -> স্ট্রিং কোন শব্দ দিয়ে শেষ হয়েছে কিনা চেক করে
print(str1.endswith('coder.'))

# split() -> স্ট্রিং কে টুকরো টুকরো করে লিস্টে রূপান্তর করে
print(str1.split())

# join() -> লিস্টের এলিমেন্টগুলোকে একটি স্ট্রিং এ রূপান্তর করে
words = str1.split()
print(' '.join(words))

# isalpha() -> স্ট্রিং শুধু অক্ষর দিয়ে তৈরি কিনা চেক করে
print("HelloWorld".isalpha())

# isdigit() -> স্ট্রিং শুধু সংখ্যা দিয়ে তৈরি কিনা চেক করে
print("12345".isdigit())

# islower() -> স্ট্রিং সম্পূর্ণ ছোট হাতের কিনা চেক করে
print(str1.islower())

# isupper() -> স্ট্রিং সম্পূর্ণ বড় হাতের কিনা চেক করে
print(str1.isupper())

# swapcase() -> বড় হাতের অক্ষরগুলোকে ছোট হাতের এবং ছোট হাতের অক্ষরগুলোকে বড় হাতের করে
print(str1.swapcase())
# find() -> স্ট্রিং এর মধ্যে কোন শব্দ বা অক্ষর কোন পজিশনে আছে তা খুঁজে বের করে
print(str1.find('Najim'))

# replace() -> স্ট্রিং এর মধ্যে কোন শব্দ বা অক্ষর পরিবর্তন করে
print(str1.replace('Najim', 'John'))

# lower() -> স্ট্রিং কে ছোট হাতের করে
print(str1.lower())

# upper() -> স্ট্রিং কে বড় হাতের করে
print(str1.upper())

# title() -> প্রতিটি শব্দের প্রথম অক্ষর বড় হাতের করে
print(str1.title())

# center() -> স্ট্রিং কে মাঝখানে রেখে বাকি জায়গা স্পেস দিয়ে পূরণ করে
print(str1.center(50))

# zfill() -> স্ট্রিং এর বাম পাশে জিরো যোগ করে
print("123".zfill(5))

# isalnum() -> স্ট্রিং শুধু অক্ষর এবং সংখ্যা দিয়ে তৈরি কিনা চেক করে
print("Hello123".isalnum())

# isspace() -> স্ট্রিং শুধু স্পেস দিয়ে তৈরি কিনা চেক করে
print("   ".isspace())

# istitle() -> স্ট্রিং টাইটেল কেস কিনা চেক করে
print(str1.istitle())

# partition() -> স্ট্রিং কে তিন ভাগে ভাগ করে: প্রথম অংশ, সেপারেটর, শেষ অংশ
print(str1.partition('is'))

# ljust() -> স্ট্রিং কে বাম দিকে সারিবদ্ধ করে
print(str1.ljust(50))

# rjust() -> স্ট্রিং কে ডান দিকে সারিবদ্ধ করে
print(str1.rjust(50))
