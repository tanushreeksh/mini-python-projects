import random

youdict = {"r" : 1, "p" : 0, "s": -1}
gamedict = {1: "rock", 0: "paper", -1: "scissors"}

print("Rock Paper Scissors shoot!")


def playgame():

    yourchoice = input("Enter your choice (r/p/s)- ").lower()

    if yourchoice not in youdict:
        return "Invalid choice. Please choose between r,p,s"


    you = youdict[yourchoice]
    computer = random.choice([1,0,-1])


    print(f"\nYou chose {gamedict[you]}")
    print(f"Computer chose {gamedict[computer]}")


    if you == computer:
        print("\nDRAW")
    else:
        if (you == 1 and computer == -1) or (you == 0 and computer == 1) or (you == -1 and computer == 0):
            print("\nYay you Won")
        elif (you == 1 and computer == 0) or (you == 0 and computer == -1) or (you == -1 and computer == 1):
            print("\nOh no you Lost")
        else:
            print("\nSomething went wrong...")


def rpsgame():
    while True:
        playgame()

        again = input("\nDo you want to play again? (Yes/No)- ").lower()
        if again != "yes":
            print("Thanks for playing.Come back soon!")
            break

rpsgame()
