import random


player_score = 0    
computer_score = 0

def game_result(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "The Match Draw!"
    elif (player_choice == "Stone" and computer_choice == "Scissor") or \
         (player_choice == "Paper" and computer_choice == "Stone") or \
         (player_choice == "Scissor" and computer_choice == "Paper"):
        return "You win the match!"
    else:
        return "Computer wins!"

print(".....WELCOME TO THE GAME.....")
OPTIONS = ["Scissor", "Paper", "Stone"]
rounds = int(input("Enter the times you want to play the game: "))



for i in range(rounds):
    player_choice = input("Choose 'Stone', 'Paper', 'Scissor': ").capitalize().strip()
    if player_choice not in OPTIONS:
        print("Please choose a valid option to continue the game.")
        continue
    computer_choice = random.choice(OPTIONS)
    print(f"Computer chose: {computer_choice}")

    result = game_result(player_choice, computer_choice)
    print(result)

    if "You win" in result:
        player_score += 1
    elif "Computer wins" in result:
        computer_score += 1


print("\nFinal Scores:")
print(f"You: {player_score}")
print(f"Computer: {computer_score}")

if player_score > computer_score:
    print("Congratulations! You won the game!")
elif computer_score > player_score:
    print("Computer won the game! Better luck next time.")
else:
    print("The game is a draw!")







    
    


    


    
    




