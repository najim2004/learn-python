import random
secret_number= random.randint(1,10)
guess_count=0
guess_limit=3
while guess_count<guess_limit:
    guess=int(input("Guess the number under 1 to 10: "))
    guess_count+=1
    if guess==secret_number:
        print("You won!")
        break
else:
    print("Sorry, you failed!")