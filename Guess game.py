import random

Singelplayer = True
computer = random.randint(1,10)
antal = 0

while Singelplayer == True:
    try:
        guess = int(input("Skriv ett tal mellan 1 - 10: "))
        if antal > 1:
            Singelplayer = False
        if guess < computer:
            print("Högre")
            antal += 1
        elif guess > computer:
            print("Lägre")
            antal += 1
        elif guess == computer:
            print("Rätt")
            antal += 1
            Singelplayer = False
    except (ValueError):
        print("Skriv en siffra")