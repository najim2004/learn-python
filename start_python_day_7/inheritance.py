# ----------------- পেরেন্ট ক্লাস (Parent Classes) -----------------
class Animal:
    """এই ক্লাসটি সব পশুর জন্য পেরেন্ট (Parent) ক্লাস হিসেবে কাজ করবে।"""

    def __init__(self, name):
        self.name = name  # পশুর নাম সেট করা

    def speak(self):
        """এই মেথডটি প্রতিটি পশুর জন্য আলাদা হবে, তাই এটি পরবর্তী ক্লাসে ওভাররাইট করতে হবে।"""
        raise NotImplementedError("Subclasses must implement this method")


class Device:
    """এই ক্লাসটি ইলেকট্রনিক ডিভাইসের জন্য পেরেন্ট (Parent) ক্লাস।"""

    def __init__(self, brand):
        self.brand = brand  # ডিভাইসের ব্র্যান্ড সেট করা

    def power_on(self):
        """ডিভাইস চালু হওয়ার একটি সাধারণ মেথড।"""
        return f"{self.brand} is turning on"

# ----------------- ১. সিংগেল ইনহেরিটেন্স (Single Inheritance) -----------------


class Dog(Animal):
    """Dog ক্লাসটি Animal থেকে ইনহেরিট করছে।"""

    def speak(self):
        return f"{self.name} বলে Woof!"  # কুকুরের সাউন্ড

# ----------------- ২. মাল্টিলেভেল ইনহেরিটেন্স (Multilevel Inheritance) -----------------


class WildDog(Dog):
    """WildDog ক্লাসটি Dog থেকে ইনহেরিট করেছে, মানে এটি Animal-এর ও অংশ।"""

    def hunt(self):
        return f"{self.name} বন্য পরিবেশে শিকার করছে!"

# ----------------- ৩. হায়ারার্কিক্যাল ইনহেরিটেন্স (Hierarchical Inheritance) -----------------


class Cat(Animal):
    """Cat ক্লাসটি Animal থেকে ইনহেরিট করেছে।"""

    def speak(self):
        return f"{self.name} বলে Meow!"


class Tiger(Animal):
    """Tiger ক্লাসটি Animal থেকে ইনহেরিট করেছে।"""

    def speak(self):
        return f"{self.name} বলে Roar!"

# ----------------- ৪. মাল্টিপল ইনহেরিটেন্স (Multiple Inheritance) -----------------


class RobotPet(Animal, Device):
    """
    RobotPet ক্লাসটি Animal এবং Device উভয় ক্লাস থেকে ইনহেরিট করেছে।
    এটি একটি রোবটিক পোষা প্রাণী যা কথা বলতে এবং পাওয়ার অন করতে পারে।
    """

    def __init__(self, name, brand):
        Animal.__init__(self, name)  # Animal এর কনস্ট্রাক্টর কল
        Device.__init__(self, brand)  # Device এর কনস্ট্রাক্টর কল

    def speak(self):
        return f"{self.name} ইলেকট্রনিকভাবে শব্দ করে: Beep Beep!"

# ----------------- ৫. হাইব্রিড ইনহেরিটেন্স (Hybrid Inheritance) -----------------


class ElectronicDog(Dog, Device):
    """
    ElectronicDog ক্লাসটি Dog (Animal থেকে এসেছে) এবং Device উভয় থেকে ইনহেরিট করেছে।
    এটি কুকুরের মতো শব্দ করতে পারে এবং ডিভাইসের মতো চালু হতে পারে।
    """

    def __init__(self, name, brand):
        Dog.__init__(self, name)     # Dog (Animal) এর কনস্ট্রাক্টর কল
        Device.__init__(self, brand)  # Device এর কনস্ট্রাক্টর কল

    def special_bark(self):
        """একটি ইলেকট্রনিক কুকুরের বিশেষ ধরনের শব্দ।"""
        return f"{self.name} ({self.brand}) ইলেকট্রনিকভাবে ঘেউ ঘেউ করছে!"

# ----------------- মেইন ফাংশন (Main Execution) -----------------


def main():
    """এই ফাংশনটিতে আমরা সব ইনহেরিটেন্সের উদাহরণ চেক করবো।"""

    print("----- ১. Single Inheritance -----")
    dog = Dog("Tommy")
    print(dog.speak())  # Output: Tommy বলে Woof!

    print("\n----- ২. Multilevel Inheritance -----")
    wild_dog = WildDog("Wolf")
    print(wild_dog.speak())  # Dog থেকে এসেছে
    print(wild_dog.hunt())   # WildDog-এর নিজস্ব মেথড

    print("\n----- ৩. Hierarchical Inheritance -----")
    cat = Cat("Kitty")
    tiger = Tiger("Shera")
    print(cat.speak())   # Output: Kitty বলে Meow!
    print(tiger.speak())  # Output: Shera বলে Roar!

    print("\n----- ৪. Multiple Inheritance -----")
    robot_pet = RobotPet("RX-2024", "TechCorp")
    # Output: RX-2024 ইলেকট্রনিকভাবে শব্দ করে: Beep Beep!
    print(robot_pet.speak())
    print(robot_pet.power_on())  # Output: TechCorp is turning on

    print("\n----- ৫. Hybrid Inheritance -----")
    electronic_dog = ElectronicDog("RoboDog", "PetTech")
    print(electronic_dog.speak())       # Output: RoboDog বলে Woof!
    print(electronic_dog.power_on())    # Output: PetTech is turning on
    # Output: RoboDog (PetTech) ইলেকট্রনিকভাবে ঘেউ ঘেউ করছে!
    print(electronic_dog.special_bark())


# স্ক্রিপ্টটি সরাসরি রান হলে `main()` ফাংশন কল হবে
if __name__ == "__main__":
    main()
