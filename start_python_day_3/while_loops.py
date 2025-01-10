# উদাহরণ ১: ১ থেকে ৫ পর্যন্ত গণনা
# যতক্ষণ শর্ত সত্য থাকবে ততক্ষণ while লুপ চলতে থাকবে
i=1
while i<=5:
    print("1.",i)
    i=i+1
print("2. Done")

# উদাহরণ ২: এটিএম থেকে টাকা তোলার সিমুলেশন
balance = 1000
while balance > 0:
    withdraw = 200
    balance = balance - withdraw
    print(f"3. Withdrawal: {withdraw}, Remaining balance: {balance}")

# উদাহরণ ৩: গেম স্কোর ক্যালকুলেশন
score = 0
game_active = True
while game_active and score < 100:
    score += 10
    print(f"4. Current score: {score}")
    if score >= 100:
        print("5. Game Over!")