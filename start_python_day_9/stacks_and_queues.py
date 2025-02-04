# স্ট্যাক এবং কিউ সম্পর্কে ব্যাখ্যা সহ পাইথন কোড

# Stack (স্ট্যাক) একটি LIFO (Last In, First Out) ডেটা স্ট্রাকচার।
# এটি লিস্ট ব্যবহার করে বাস্তবায়ন করা হয়েছে।
from collections import deque


class Stack:
    def __init__(self):
        self.stack = []  # একটি খালি লিস্ট দিয়ে স্ট্যাক শুরু করা হয়

    def push(self, item):
        self.stack.append(item)  # নতুন এলিমেন্ট স্ট্যাকে যোগ করা হয়

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()  # সর্বশেষ এলিমেন্ট সরিয়ে ফেরত দেয়
        return "Stack is empty"  # যদি স্ট্যাক খালি হয় তাহলে বার্তা ফেরত দেয়

    def peek(self):
        if not self.is_empty():
            # সর্বশেষ এলিমেন্টটি দেখানো হয় কিন্তু সরানো হয় না
            return self.stack[-1]
        return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0  # চেক করা হয় স্ট্যাক ফাঁকা কিনা

    def size(self):
        return len(self.stack)  # স্ট্যাকের মোট এলিমেন্ট সংখ্যা ফেরত দেয়


# Queue (কিউ) একটি FIFO (First In, First Out) ডেটা স্ট্রাকচার।
# এটি collections.deque ব্যবহার করে বাস্তবায়ন করা হয়েছে।


class Queue:
    def __init__(self):
        self.queue = deque()  # একটি খালি deque দিয়ে কিউ শুরু করা হয়

    def enqueue(self, item):
        self.queue.append(item)  # নতুন এলিমেন্ট কিউতে যোগ করা হয়

    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()  # প্রথম এলিমেন্ট সরিয়ে ফেরত দেয়
        return "Queue is empty"

    def front(self):
        if not self.is_empty():
            # প্রথম এলিমেন্টটি দেখানো হয় কিন্তু সরানো হয় না
            return self.queue[0]
        return "Queue is empty"

    def is_empty(self):
        return len(self.queue) == 0  # চেক করা হয় কিউ ফাঁকা কিনা

    def size(self):
        return len(self.queue)  # কিউর মোট এলিমেন্ট সংখ্যা ফেরত দেয়


# স্ট্যাক এবং কিউ এর ব্যবহারিক উদাহরণ
if __name__ == "__main__":
    # Stack ব্যবহার
    print("Stack Example:")
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    print("Stack Pop:", s.pop())  # সর্বশেষ এলিমেন্ট (30) সরানো হবে
    print("Stack Peek:", s.peek())  # এখন সর্বশেষ এলিমেন্ট হবে 20

    # Queue ব্যবহার
    print("\nQueue Example:")
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print("Queue Dequeue:", q.dequeue())  # প্রথম এলিমেন্ট (10) সরানো হবে
    print("Queue Front:", q.front())  # এখন প্রথম এলিমেন্ট হবে 20
