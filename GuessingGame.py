import random

number = random.randint(1, 100)

# the user enters a number
player = input("Guess the number: ")

# check the drawn and given number
while number != player:
    try:
        if int(player) < number:
            print("To small!")
            player = input("Guess the number: ")
        elif int(player) > number:

            print("To big!")
            player = input("Guess the number: ")
        else:
            break
    except ValueError:
        print("It's not number")
        player = number
print("You win")

