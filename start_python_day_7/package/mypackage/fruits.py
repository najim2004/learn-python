# fruits.py - ফলের সম্পর্কে তথ্য

def color(fruit):
    """ফলের নাম অনুযায়ী তার রঙ ফেরত দিবে"""
    colors = {
        "apple": "red or green",
        "orange": "orange",
        "banana": "yellow",
        "mango": "green or yellow"
    }
    return colors.get(fruit, "Color not known!")


def taste(fruit):
    """ফলের নাম অনুযায়ী তার স্বাদ ফেরত দিবে"""
    tastes = {
        "apple": "sweet or sour",
        "orange": "sweet and slightly sour",
        "banana": "sweet",
        "mango": "sweet or sour"
    }
    return tastes.get(fruit, "Taste not known!")
