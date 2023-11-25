import random
print("welcome to the rock, paper, scissor game")
player_wins=0
computer_wins=0
while True:
    player=input("\n Enter a choice: \n1.Rock \n2.paper \n3.scissor :")
    choices=["rock","paper","scissor"]
    computer=random.choice(choices)
    print(f"\nYou choose{player}, computer choose{computer}.")

    if player==computer:
        print(f"Both payers selected{player}.It is a try")
    elif player=="rock":
        if computer=="scissor":
            print("rock smashes scissors. you win")
            player_wins+=1
        else:
            print("paper covers rock. you lose")
            computer_wins+=1

    elif player=="paper":
        if computer=="rock":
           print("paper covers rock. you win")
           player_wins+=1
        else:
             print("rock smashes scissors. you lose")
             computer_wins+=1

    elif player=="scissor":
        if computer=="paper":
           print("scissor cuts paper. you win")
           player_wins+=1
        else:
             print("computer wins. you lose")
             computer_wins+=1

    print("\nyou have " + str(player_wins) + " wins")
    print("the computer has " + str(computer_wins) + " wins")

    repeat=input("\nplay again? (yes/no):")
    if  repeat.lower()!="yes":
        print("Thanks fofr playing!")
        break

    
           
        