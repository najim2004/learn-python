# পলিমরফিজম (Polymorphism) সম্পর্কে সহজ ব্যাখ্যা সহ পাইথন কোড

# পলিমরফিজম কি?
# পলিমরফিজম এমন একটি বৈশিষ্ট্য যেখানে একই মেথড বা ফাংশন বিভিন্ন ক্লাসে ভিন্নভাবে কাজ করতে পারে।
# এটি কোডের পুনঃব্যবহারযোগ্যতা বৃদ্ধি করে এবং অবজেক্ট-ওরিয়েন্টেড প্রোগ্রামিং (OOP) সহজ করে তোলে।

# উদাহরণ ১: পলিমরফিজম ইনহেরিটেন্সের মাধ্যমে
class Animal:
    def make_sound(self):
        return "Some generic sound"


class Dog(Animal):
    def make_sound(self):
        return "Bark!"


class Cat(Animal):
    def make_sound(self):
        return "Meow!"


# একাধিক অবজেক্ট তৈরি করা
animals = [Dog(), Cat(), Animal()]

# লুপের মাধ্যমে প্রতিটি অবজেক্টের make_sound() মেথড কল করা
for animal in animals:
    # আউটপুট: "Bark!", "Meow!", "Some generic sound"
    print(animal.make_sound())

# উদাহরণ ২: অপারেটর ওভারলোডিং এর মাধ্যমে পলিমরফিজম


class Shape:
    def area(self):
        pass  # এই মেথডটি সাবক্লাসে ওভাররাইড করা হবে


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height  # আয়তক্ষেত্রের ক্ষেত্রফল গণনা


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.1416 * self.radius * self.radius  # বৃত্তের ক্ষেত্রফল গণনা


shapes = [Rectangle(5, 10), Circle(7)]

for shape in shapes:
    print("Area:", shape.area())  # আউটপুট: 50 (Rectangle), 153.9384 (Circle)

# উদাহরণ ৩: বিল্ট-ইন ফাংশন এর সাথে পলিমরফিজম
print(len("Hello"))  # স্ট্রিং এর দৈর্ঘ্য গণনা, আউটপুট: 5
print(len([1, 2, 3, 4]))  # লিস্টের দৈর্ঘ্য গণনা, আউটপুট: 4

# পলিমরফিজম ব্যবহার করে কোডকে আরও ডায়নামিক এবং পুনঃব্যবহারযোগ্য করা যায়।
