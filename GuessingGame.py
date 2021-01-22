import random
n = random.randint(1, 9)
guess = int(input("Enter a number from 1 to 9: "))
max_chances = 0
while max_chances < 9:
    max_chances += 1
    if guess < n:
        print("guess is low")
        guess = int(input("Enter a number from 1 to 9: "))
    elif guess > n:
        print("guess is high")
        guess = int(input("Enter a number from 1 to 9: "))
    else:
        print("you guessed it!")
        print("You Won!!")
        break
    
if guess != n:
    print("Game Over")
    print("Correct Number is:", n)
