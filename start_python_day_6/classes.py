# বাস্তব জগতের কয়েকটি ক্লাস এর উদাহরণ

class Student:
    """A class to represent a student in a school"""

    def __init__(self, name, roll, class_name):
        self.name = name
        self.roll = roll
        self.class_name = class_name
        self.marks = []

    # ছাত্রের নম্বর যোগ করার মেথড
    def add_marks(self, mark):
        self.marks.append(mark)

    # ছাত্রের গড় নম্বর বের করার মেথড
    def get_average(self):
        return sum(self.marks) / len(self.marks) if self.marks else 0


# গাড়ির উদাহরণ
class Car:
    """A class to represent a car"""

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0

    # গাড়ির গতি বাড়ানোর মেথড
    def accelerate(self):
        self.speed += 10

    # গাড়ির গতি কমানোর মেথড
    def brake(self):
        self.speed = max(0, self.speed - 10)


# ব্যাংক একাউন্টের উদাহরণ
class BankAccount:
    """A class to represent a bank account"""

    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    # টাকা জমা করার মেথড
    def deposit(self, amount):
        self.balance += amount
        return f"Deposited ${amount}. New balance: ${self.balance}"

    # টাকা তোলার মেথড
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        return "Insufficient funds!"


# Example usage:
if __name__ == "__main__":
    # Example 1: Student
    print("Example 1: Student")
    student1 = Student("Rahim", 101, "Class 10")
    student1.add_marks(85)
    student1.add_marks(92)
    print(f"Student average marks: {student1.get_average()}")

    # Example 2: Car
    print("\nExample 2: Car")
    car1 = Car("Toyota", "Corolla", 2020)
    car1.accelerate()
    print(f"Car speed after acceleration: {car1.speed} km/h")

    # Example 3: Bank Account
    print("\nExample 3: Bank Account")
    account1 = BankAccount("Karim", 1000)
    print(account1.deposit(500))
    print(account1.withdraw(200))
