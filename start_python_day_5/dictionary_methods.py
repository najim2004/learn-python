# ডিকশনারি মেথড এর উদাহরণ
my_dict = {'name': 'John', 'age': 25, 'city': 'Dhaka'}

# 1. get() মেথড - কোন কি এর ভ্যালু পাওয়ার জন্য, কি না থাকলে ডিফল্ট ভ্যালু রিটার্ন করে
print("1. Using get():", my_dict.get('name'), my_dict.get('country', 'Not Found'))

# 2. keys() মেথড - সব কি গুলো পাওয়ার জন্য
print("2. Using keys():", my_dict.keys())

# 3. values() মেথড - সব ভ্যালু গুলো পাওয়ার জন্য
print("3. Using values():", my_dict.values())

# 4. items() মেথড - কি-ভ্যালু পেয়ার পাওয়ার জন্য
print("4. Using items():", my_dict.items())

# 5. update() মেথড - ডিকশনারি আপডেট করার জন্য
my_dict.update({'country': 'Bangladesh', 'age': 26})
print("5. After update():", my_dict)

# 6. pop() মেথড - কোন কি-ভ্যালু রিমুভ করার জন্য
removed_value = my_dict.pop('city')
print("6. After pop():", my_dict, "Removed:", removed_value)

# 7. clear() মেথড - পুরো ডিকশনারি খালি করার জন্য
temp_dict = my_dict.copy()
temp_dict.clear()
print("7. After clear():", temp_dict)

# 8. copy() মেথড - ডিকশনারির কপি করার জন্য
new_dict = my_dict.copy()
print("8. After copy():", new_dict)

# 9. setdefault() মেথড - কি না থাকলে নতুন কি-ভ্যালু যোগ করার জন্য
print("9. Using setdefault():", my_dict.setdefault('email', 'john@example.com'))

# 10. fromkeys() মেথড - নতুন ডিকশনারি তৈরি করার জন্য
keys = ['a', 'b', 'c']
print("10. Using fromkeys():", dict.fromkeys(keys, 0))

# 11. popitem() মেথড - শেষের কি-ভ্যালু পেয়ার রিমুভ করে
last_item = my_dict.popitem()
print("11. After popitem():", my_dict, "Removed:", last_item)

# 12. len() ফাংশন - ডিকশনারির সাইজ জানার জন্য
print("12. Dictionary length:", len(my_dict))

# 13. in অপারেটর - কোন কি আছে কিনা চেক করার জন্য
print("13. 'name' in dictionary:", 'name' in my_dict)

# 14. dict() কনস্ট্রাক্টর - নতুন ডিকশনারি তৈরি করার জন্য
new_dict2 = dict(name='Alice', age=30)
print("14. Using dict():", new_dict2)

# 15. nested dictionary - ডিকশনারির ভিতর ডিকশনারি
nested_dict = {'user': {'name': 'John', 'age': 25}}
print("15. Nested dictionary access:", nested_dict['user']['name'])