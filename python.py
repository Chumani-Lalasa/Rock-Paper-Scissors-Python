import random
ROCK = "rock"
PAPER = "paper"
SCISSORS = "scissors"
def get_user_choice():
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    return user_choice
def get_computer_choice():
    choices = [ROCK, PAPER, SCISSORS]
    computer_choice = random.choice(choices)
    return computer_choice
def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"

    if (
        (user == ROCK and computer == SCISSORS) or
        (user == PAPER and computer == ROCK) or
        (user == SCISSORS and computer == PAPER)
    ):
        return "You win!"

    return "Computer wins!"

# Main program
def main():
    user_choice = get_user_choice()
    if user_choice not in [ROCK, PAPER, SCISSORS]:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        return
    computer_choice = get_computer_choice()
    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)
    result = determine_winner(user_choice, computer_choice)
    print(result)
main()