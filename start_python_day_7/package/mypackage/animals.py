# animals.py - প্রাণীদের সম্পর্কে তথ্য

def sound(animal):
    """প্রাণীর নাম অনুযায়ী তার স্বাভাবিক শব্দ ফেরত দিবে"""
    sounds = {
        "dog": "woof woof!",
        "cat": "meow meow!",
        "cow": "moo moo!",
        "lion": "roar!"
    }
    return sounds.get(animal, "Sound not found for this animal!")


def legs(animal):
    """প্রাণীর নাম অনুযায়ী তার পায়ের সংখ্যা ফেরত দিবে"""
    leg_counts = {
        "dog": 4,
        "cat": 4,
        "cow": 4,
        "chicken": 2,
        "human": 2
    }
    return leg_counts.get(animal, "Information not found for this animal!")
