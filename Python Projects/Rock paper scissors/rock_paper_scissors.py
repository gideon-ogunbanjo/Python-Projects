import random  # import the random module

do = input("Do you want to play? ")
if do == "yes":
    print("okay, lets play!")
    while True:
        choices = ["rock","paper","scissors"] #create choices of rock, paper, scissors..

        computer = random.choice(choices) #here i let the computer pick a random choice amongst my assigned choices
        player = None #the player picks none

        while player not in choices: #if the players input is not among my listed choices, this line of code will make it keep on asking until he makes the desired choice
            player = input("rock, paper or scissors?: ").lower() # pick a choice..

        if player == computer:

            print("computer: ",computer)
            print("player: ",player)
            print("Tie") #this block of code says if the computer and the player pick the same choice, it should output as a tie! janken

        elif player ==  "rock":
            if computer == "paper":
                print("computer: ",computer)
                print("player: ",player)
                print("You Lose!") #This shows if the player picks rock, and the computer picks paper, its a loss...
            if computer == "scissors":
                print("computer: ",computer)
                print("player: ",player)
                print("You Win!") #this shows if the player picks rock and the computer picks scissors, you win!

        elif player ==  "scissors":
            if computer == "rock":
                print("computer: ",computer)
                print("player: ",player)
                print("You Lose!") #this shows if the player picks scissors and the computer picks rock, you lose!
            if computer == "paper":
                print("computer: ",computer)
                print("player: ",player)
                print("You Win!") #this shows if the player picks scissors and the computer picks paper, you win!
        
        elif player ==  "paper":
            if computer == "rock":
                print("computer: ",computer)
                print("player: ",player)
                print("You Win!") #this shows if the player picks paper and the computer picks rock, you win!
            if computer == "scissors":
                print("computer: ",computer)
                print("player: ",player)
                print("You Lose!") #this shows if the player picks paper and the computer picks scissors, you win!
        play_again = input("Play Again? (yes/no): ").lower() #this line of code is to ask if the player wants to play a again

        if play_again is not "yes": 
            break
        
        
    print("Bye") #the game is over  
