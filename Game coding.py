import random
import time

print("Hi! Welcome to the guessing game. I am going to pick a number between 1 and 100")
time.sleep(3)
difficulty = int(input("Select Difficulty.\n1-Easy\n2-Hard\n: "))
time.sleep(3)
print("Done")
time.sleep(3)
print("Get Ready!!")
time.sleep(3)
print("Picking a number .......")
time.sleep(2)
guess = int(input("Guess the number?: "))
correct_number = random.randint(1,100)
guess_count = 1
if difficulty == 1:
    while guess != correct_number:
        time.sleep(1)
        guess_count += 1
        if guess < correct_number:
            guess = int(input("Wrong. You need to guess higher. Guess the number?: "))
        else:
            guess = int(input("Wrong. You need to guess lower. Guess the number?: "))
else:
    while guess != correct_number:
        time.sleep(1)
        guess_count += 1
        guess = int(input("Wrong. Guess the number?: "))

print(f"Congrats! The right answer was {correct_number}. It took you {guess_count} guesses. ")

