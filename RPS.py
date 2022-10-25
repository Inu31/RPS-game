import random
ans="y"
while ans.lower()=="y":
    game=['rock','paper','scissors']
    name=input("Enter your name")
    ComputerScore=0
    PlayerScore=0
    NumberOfRounds=0
    print("Welcome",name.title())
    print("It is a game of 5 rounds")
    while NumberOfRounds<5:
        ComputerOption=random.choice(game)
        PlayerOption=input("Enter rock/ paper/ scissors   :")
        print("Computer option:",ComputerOption)
        print(name.title(),"option:",PlayerOption)
        NumberOfRounds +=1
        if ComputerOption==PlayerOption:
            print('Tie')

        elif (ComputerOption=='rock' and PlayerOption=='scissors')or(ComputerOption=='paper' and PlayerOption=='rock')or(ComputerOption=='scissors' and PlayerOption=='paper'):
            print('Computer Wins')
            ComputerScore=+1

        elif(PlayerOption=='rock' and ComputerOption=='scissors')or(PlayerOption=='paper' and ComputerOption=='rock')or (PlayerOption=='scissors' and ComputerOption=='paper'):
            print(name.title(),"Wins")
            PlayerScore=+1

        else:
            print("Enter Correct option to play")
        print("--------------------")
        print("")
        print("Round No:",NumberOfRounds)
        print("--------ScoreBoard----------")
        print(f"{name.title()}:{PlayerScore}   |  Computer:{ComputerScore}")
        print("=======================")
        print("")
        if NumberOfRounds==5:
            break
    if PlayerScore==ComputerScore:
        print("Draw")
    elif PlayerScore>ComputerScore:
        print(f"Congrats{name.title()}.You won the game")
    elif PlayerScore<ComputerScore:
        print(f"Oh no Computer won the game. Try harder next time {name.title()}.")
    ans=input("Do you want to continue this game y/n")
    if ans.lower()=="n":
        break