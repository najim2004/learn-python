# main.py - এখানে আমাদের প্যাকেজ ব্যবহার করা হবে

# আমাদের তৈরি করা প্যাকেজ ইমপোর্ট করা হচ্ছে
import mypackage


def main():
    # প্রাণীর তথ্য
    animal_name = input(
        "Enter an animal name (e.g., dog, cat, cow, lion): ")
    print(f"Sound of {animal_name}: {mypackage.sound(animal_name)}")
    print(f"Number of legs of {animal_name}: {mypackage.legs(animal_name)}")

    print("\n---------------------------\n")

    # ফলের তথ্য
    fruit_name = input("Enter a fruit name (e.g., apple, orange, banana, mango): ")
    print(f"Color of {fruit_name}: {mypackage.color(fruit_name)}")
    print(f"Taste of {fruit_name}: {mypackage.taste(fruit_name)}")


if __name__ == "__main__":
    main()
