import random

while True:

    player = input("Enter a choice (r, p, s): ")
    possible_actions = ["r", "p", "s"]
    cpu = random.choice(possible_actions)
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

    if player == cpu:
        print(f"Both players selected {user_action}. It's a tie!")
    elif player == "r":
        if cpu == "s":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
        break
    elif player == "p":
        if cpu == "r":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
        break
    elif player == "s":
        if cpu == "p":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
        break
    else:
        print("given input is invalid...")
