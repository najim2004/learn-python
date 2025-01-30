# calculator.py (গণনা সম্পর্কিত ফাংশন)
def add(a, b):
    """দুটি সংখ্যার যোগফল দিবে"""
    return a + b


def multiply(a, b):
    """দুটি সংখ্যার গুণফল দিবে"""
    return a * b


def subtract(a, b):
    """দুটি সংখ্যার বিয়োগফল দিবে"""
    return a - b


def divide(a, b):
    """দুটি সংখ্যার ভাগফল দিবে"""
    if b == 0:
        return "ভাগ শূন্য দিয়ে করা সম্ভব নয়!"
    return a / b
