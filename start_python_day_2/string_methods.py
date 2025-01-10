str1 = 'Hello! My name is Mohammad Najim. I am a coder.'

# strip() -> স্ট্রিং এর শুরু এবং শেষের whitespace মুছে ফেলে
print("1:", str1.strip())

# lstrip() -> স্ট্রিং এর শুরুর whitespace মুছে ফেলে
print("2:", str1.lstrip())

# rstrip() -> স্ট্রিং এর শেষের whitespace মুছে ফেলে
print("3:", str1.rstrip())

# capitalize() -> শুধু প্রথম অক্ষরকে বড় হাতের করে
print("4:", str1.capitalize())

# count() -> কোন শব্দ বা অক্ষর কতবার আছে তা গণনা করে
print("5:", str1.count('a'))

# startswith() -> স্ট্রিং কোন শব্দ দিয়ে শুরু হয়েছে কিনা চেক করে
print("6:", str1.startswith('Hello!'))

# endswith() -> স্ট্রিং কোন শব্দ দিয়ে শেষ হয়েছে কিনা চেক করে
print("7:", str1.endswith('coder.'))

# split() -> স্ট্রিং কে টুকরো টুকরো করে লিস্টে রূপান্তর করে
print("8:", str1.split())

# join() -> লিস্টের এলিমেন্টগুলোকে একটি স্ট্রিং এ রূপান্তর করে
words = str1.split()
print("9:", ' '.join(words))

# isalpha() -> স্ট্রিং শুধু অক্ষর দিয়ে তৈরি কিনা চেক করে
print("10:", "HelloWorld".isalpha())

# isdigit() -> স্ট্রিং শুধু সংখ্যা দিয়ে তৈরি কিনা চেক করে
print("11:", "12345".isdigit())

# islower() -> স্ট্রিং সম্পূর্ণ ছোট হাতের কিনা চেক করে
print("12:", str1.islower())

# isupper() -> স্ট্রিং সম্পূর্ণ বড় হাতের কিনা চেক করে
print("13:", str1.isupper())

# swapcase() -> বড় হাতের অক্ষরগুলোকে ছোট হাতের এবং ছোট হাতের অক্ষরগুলোকে বড় হাতের করে
print("14:", str1.swapcase())

# find() -> স্ট্রিং এর মধ্যে কোন শব্দ বা অক্ষর কোন পজিশনে আছে তা খুঁজে বের করে
print("15:", str1.find('Najim'))

# replace() -> স্ট্রিং এর মধ্যে কোন শব্দ বা অক্ষর পরিবর্তন করে
print("16:", str1.replace('Najim', 'John'))

# lower() -> স্ট্রিং কে ছোট হাতের করে
print("17:", str1.lower())

# upper() -> স্ট্রিং কে বড় হাতের করে
print("18:", str1.upper())

# title() -> প্রতিটি শব্দের প্রথম অক্ষর বড় হাতের করে
print("19:", str1.title())

# center() -> স্ট্রিং কে মাঝখানে রেখে বাকি জায়গা স্পেস দিয়ে পূরণ করে
print("20:", str1.center(50))

# zfill() -> স্ট্রিং এর বাম পাশে জিরো যোগ করে
print("21:", "123".zfill(5))

# isalnum() -> স্ট্রিং শুধু অক্ষর এবং সংখ্যা দিয়ে তৈরি কিনা চেক করে
print("22:", "Hello123".isalnum())

# isspace() -> স্ট্রিং শুধু স্পেস দিয়ে তৈরি কিনা চেক করে
print("23:", "   ".isspace())

# istitle() -> স্ট্রিং টাইটেল কেস কিনা চেক করে
print("24:", str1.istitle())

# partition() -> স্ট্রিং কে তিন ভাগে ভাগ করে: প্রথম অংশ, সেপারেটর, শেষ অংশ
print("25:", str1.partition('is'))

# ljust() -> স্ট্রিং কে বাম দিকে সারিবদ্ধ করে
print("26:", str1.ljust(50))

# rjust() -> স্ট্রিং কে ডান দিকে সারিবদ্ধ করে
print("27:", str1.rjust(50))

# encode() -> স্ট্রিং কে বাইট অ্যারেতে রূপান্তর করে
print("28:", str1.encode())

# expandtabs() -> ট্যাব ক্যারেক্টার কে স্পেস দিয়ে প্রতিস্থাপন করে
print("29:", "Hello\tWorld".expandtabs(4))

# format() -> স্ট্রিং ফরম্যাটিং করে
print("30:", "{} is {}".format("Python", "awesome"))

# translate() -> ক্যারেক্টার প্রতিস্থাপন করে
trans_table = str.maketrans("aeiou", "12345")
print("31:", str1.translate(trans_table))

# casefold() -> স্ট্রিং কে লোয়ারকেস এ রূপান্তর করে (lower() এর চেয়ে শক্তিশালী)
print("32:", str1.casefold())

# removeprefix() -> স্ট্রিং এর শুরু থেকে নির্দিষ্ট প্রিফিক্স মুছে ফেলে
print("33:", str1.removeprefix('Hello!'))

# removesuffix() -> স্ট্রিং এর শেষ থেকে নির্দিষ্ট সাফিক্স মুছে ফেলে
print("34:", str1.removesuffix('coder.'))

# isprintable() -> স্ট্রিং প্রিন্টযোগ্য কিনা চেক করে
print("35:", str1.isprintable())

# isidentifier() -> স্ট্রিং পাইথন আইডেন্টিফায়ার হিসেবে ব্যবহারযোগ্য কিনা চেক করে
print("36:", str1.isidentifier())

# "..." in str -> স্ট্রিং এর মধ্যে কোন শব্দ বা অক্ষর আছে কিনা চেক করে
print("37:", "Najim" in str1)

# "..." not in str -> স্ট্রিং এর মধ্যে কোন শব্দ বা অক্ষর নেই কিনা চেক করে
print("38:", "John" not in str1)
