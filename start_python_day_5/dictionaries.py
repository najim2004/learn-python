# ডিকশনারি হলো একটি ডেটা স্ট্রাকচার যেখানে কী-ভ্যালু পেয়ার আকারে ডেটা সংরক্ষণ করা হয়
# প্রতিটি কী অনন্য (unique) হতে হবে এবং যেকোনো ধরনের ডেটা ভ্যালু হিসেবে রাখা যায়
# ডিকশনারি কার্লি ব্রেস {} দিয়ে তৈরি করা হয়

# ডিকশনারি দিয়ে একজন ছাত্রের তথ্য রাখা
print("1. Student Information Example:")
student = {
    "name": "Karim Ahmed",
    "roll": 101,
    "class": "Ten",
    "subjects": ["Bangla", "English", "Math"],
    "results": {"Bangla": 85, "English": 90, "Math": 95}
}
print(student["name"])
print(student["results"]["Math"])

# রেস্টুরেন্টের মেনু এবং দাম
print("\n2. Restaurant Menu Example:")
menu = {
    "rice": 50,
    "beef": 180,
    "chicken": 140,
    "vegetables": 40,
    "drinks": {"coke": 25, "coffee": 30, "tea": 15}
}
print(f"Beef price: {menu['beef']} taka")
print(f"Coffee price: {menu['drinks']['coffee']} taka")

# একটি মোবাইল ফোনের স্পেসিফিকেশন
print("\n3. Mobile Phone Specifications Example:")
phone = {
    "brand": "Samsung",
    "model": "Galaxy A52",
    "price": 35000,
    "features": {
        "ram": "6GB",
        "storage": "128GB",
        "camera": "64MP"
    }
}
print(f"Phone model: {phone['model']}")
print(f"RAM: {phone['features']['ram']}")

# ই-কমার্স ইউজার প্রোফাইল
print("\n4. E-commerce User Profile Example:")
user = {
    "user_id": "U1001",
    "name": "Rahim Khan",
    "email": "rahim@example.com",
    "address": {
        "street": "123 Main Road",
        "city": "Dhaka",
        "postal_code": "1216"
    },
    "order_history": ["Order#123", "Order#124", "Order#125"]
}
print(f"User name: {user['name']}")
print(f"City: {user['address']['city']}")
print(f"Last order: {user['order_history'][-1]}")