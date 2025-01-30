# main.py (মেইন প্রোগ্রাম যেখানে মডিউল ব্যবহার হবে)

# আমাদের তৈরি করা মডিউল দুটি ইমপোর্ট করছি
import calculator  # গণনা সম্পর্কিত ফাংশন
import greetings   # স্বাগতম বার্তা সম্পর্কিত ফাংশন


def main():
    # Taking name input
    name = input("Enter your name: ")

    # Welcome message
    print(greetings.greet(name))  # Display welcome message

    # Some calculations
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print(f"{num1} + {num2} = {calculator.add(num1, num2)}")  # Addition
    print(f"{num1} * {num2} = {calculator.multiply(num1, num2)}")  # Multiplication
    print(f"{num1} - {num2} = {calculator.subtract(num1, num2)}")  # Subtraction
    print(f"{num1} / {num2} = {calculator.divide(num1, num2)}")  # Division


if __name__ == "__main__":
    main()  # মেইন ফাংশন চালানো
