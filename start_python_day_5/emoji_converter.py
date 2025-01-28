# এমোজি কনভার্টার - মেসেজের মধ্যে ইমোজি কনভার্ট করে

# ইমোজি ডিকশনারি
emojis = {
    ":)": "😊",
    ":(": "😢",
    ":D": "😃",
    "<3": "❤️",
    ":p": "😛",
    ":o": "😮"
}

print("Welcome to Emoji Converter!")

while True:
    user_input = input("Enter a message (or 'quit' to exit): ")
    
    if user_input.lower() == 'quit':
        break
    
    # শব্দ গুলোকে আলাদা করা
    words = user_input.split(' ')
    
    # আউটপুট স্ট্রিং তৈরি
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    
    print("Converted message:", output.strip())

print("Thank you for using Emoji Converter!")
