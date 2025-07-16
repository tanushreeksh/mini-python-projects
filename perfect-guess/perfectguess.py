from random import randint

def chooselevel():
    print("Welcome to the Perfect Guess game. Choose game level")
    print("1.Easy (15 attempts)")
    print("2.Medium (10 attempts)")
    print("3.Hard (5 attempts)")


    while True:
        choice = input("\nEnter you choice (1/2/3)- ")

        choice = int(choice)

        if choice == 1:
            return 15
        elif choice == 2:
            return 10
        elif choice == 3:
            return 5
        else:
            return "Invalid choice! Choose between 1,2,3"
        

def playgame():
    num_to_guess = randint(1, 100)
    attempt = 0
    max_attempt = chooselevel()

    print("\nGuess the number between 1 to 100")

    while attempt < max_attempt:
        guess = input((f"\nAttempt {attempt + 1} Enter your guess: "))

        if not guess.isdigit():
            print("Enter a valid number!")
            continue

        guess = int(guess)

        if guess < num_to_guess:
            print("Higher number please")
            attempt += 1
        elif guess > num_to_guess:
            print("Lower number please")
            attempt += 1
        else:
            print(f"\nYay you have guessed the correct number in {attempt} attempts")
            break
    
    else:
        print(f"\nOops out of attempts. The correct number was {num_to_guess}")



def perfectguess():
    while True:
        playgame()

        again = input("\nDo you want to play another round? (yes/no)- ").lower()
        if again != "yes":
            print("Thanks for playing.Come back soon!")
            break


perfectguess()
    
