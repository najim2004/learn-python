# সব ধরনের ইনহেরিটেন্স এর উদাহরণ

# ----------------- পেরেন্ট ক্লাস (Parent Classes) -----------------
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Device:
    def __init__(self, brand):
        self.brand = brand
    
    def power_on(self):
        return f"{self.brand} is turning on"

# ----------------- সিংগেল ইনহেরিটেন্স (Single Inheritance) -----------------
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# ----------------- মাল্টিলেভেল ইনহেরিটেন্স (Multilevel Inheritance) -----------------
class WildDog(Dog):
    def hunt(self):
        return f"{self.name} is hunting"

# ----------------- হায়ারার্কিক্যাল ইনহেরিটেন্স (Hierarchical Inheritance) -----------------
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

class Tiger(Animal):
    def speak(self):
        return f"{self.name} says Roar!"

# ----------------- মাল্টিপল ইনহেরিটেন্স (Multiple Inheritance) -----------------
class RobotPet(Animal, Device):
    def __init__(self, name, brand):
        Animal.__init__(self, name)
        Device.__init__(self, brand)
    
    def speak(self):
        return f"{self.name} beeps electronically"

# ----------------- হাইব্রিড ইনহেরিটেন্স (Hybrid Inheritance) -----------------
class ElectronicDog(Dog, Device):
    def __init__(self, name, brand):
        Dog.__init__(self, name)
        Device.__init__(self, brand)
    
    def special_bark(self):
        return f"{self.name} from {self.brand} barks electronically"

def main():
    # Testing all types of inheritance
    print("-----Single Inheritance-----")
    dog = Dog("Buddy")
    print(dog.speak())
    
    print("\n-----Multilevel Inheritance-----")
    wild_dog = WildDog("Wolf")
    print(wild_dog.speak())
    print(wild_dog.hunt())
    
    print("\n-----Hierarchical Inheritance-----")
    cat = Cat("Whiskers")
    tiger = Tiger("Shera")
    print(cat.speak())
    print(tiger.speak())
    
    print("\n-----Multiple Inheritance-----")
    robot_pet = RobotPet("RX-2023", "TechCorp")
    print(robot_pet.speak())
    print(robot_pet.power_on())
    
    print("\n-----Hybrid Inheritance-----")
    electronic_dog = ElectronicDog("RoboDog", "PetTech")
    print(electronic_dog.speak())
    print(electronic_dog.power_on())
    print(electronic_dog.special_bark())

if __name__ == "__main__":
    main()