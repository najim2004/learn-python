# এমোজি কনভার্টার - মেসেজের মধ্যে ইমোজি কনভার্ট করে
# এটি একটি সিম্পল প্রোগ্রাম যা টেক্সট মেসেজের ইমোজি সিম্বল গুলোকে আসল ইমোজিতে কনভার্ট করে

# ইমোজি ডিকশনারি - এখানে ইমোজি সিম্বল এবং তার আসল ইমোজি ম্যাপিং করা আছে
emojis = {
    ":)": "😊",
    ":(": "😢",
    ":D": "😃",
    "<3": "❤️",
    ":p": "😛",
    ":o": "😮"
}

print("Welcome to Emoji Converter!")

# মূল লুপ - যতক্ষণ ইউজার quit না করবে ততক্ষণ চলবে
while True:
    # ইউজারের কাছ থেকে মেসেজ ইনপুট নেওয়া
    user_input = input("Enter a message (or 'quit' to exit): ")
    
    # যদি ইউজার quit লিখে তাহলে প্রোগ্রাম বন্ধ হয়ে যাবে
    if user_input.lower() == 'quit':
        break
    
    # ইউজারের মেসেজকে শব্দ অনুযায়ী ভাগ করা
    words = user_input.split(' ')
    
    # প্রতিটি শব্দ চেক করে ইমোজি থাকলে কনভার্ট করা
    output = ""
    for word in words:
        # emojis ডিকশনারি থেকে ম্যাচিং ইমোজি খুঁজে বের করা
        # যদি ম্যাচ না পাওয়া যায় তাহলে মূল শব্দটাই রাখা
        output += emojis.get(word, word) + " "
    
    # কনভার্ট করা মেসেজ প্রিন্ট করা
    print("Converted message:", output.strip())

print("Thank you for using Emoji Converter!")
