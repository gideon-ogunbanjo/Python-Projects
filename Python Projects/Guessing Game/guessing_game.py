import random
welcome = ("Welcome to the number guessing game")
print("Welcome to the number guessing game")
do = input("Do you want to play? ")
if do == "yes":
    print("okay, lets play!")
    print("You have to guess a number between 1 and 10")
    print("You have 3 tries")
    number = random.randint(1,10)
    tries = 3
    while tries > 0:
        guess = int(input("Guess a number "))
        if guess == number:
            print("You Won!")
            break
        else:
            print("Wrong guess try again")
            tries -= 1
            if tries == 0:
                print("You lost")
                print("The number was, number.randint(1,10) ")

        play_again = input("Play Again? (yes/no): ").lower()

        if play_again != "yes": 
            print("bye")
            break
        

print("bye")               