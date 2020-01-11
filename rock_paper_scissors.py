import random

print("""
#######################################
### Welcome to Rock Paper Scissors! ###
#######################################""")

while True:
	computer_wins = "\n######################\n### COMPUTER WINS! ###\n######################"
	player_wins = "\n####################\n### PLAYER WINS! ###\n####################"
	draw = "\n####################\n### IT'S A DRAW! ###\n####################"

	moves = ["rock" , "paper", "scissors"]

	computer_choice = random.choice(moves)

	player_choice = input("\nTest your luck against the computer by\nentering 'rock', 'paper', or 'scissors':\n\n")
	player_choice = player_choice.lower()

	if player_choice not in moves:
		print("Please enter a valid move!")
	else:
		if player_choice == computer_choice:
			print(f"You picked: {player_choice}\nComputer picked: {computer_choice}")
			print(draw)
		elif computer_choice == "rock" and player_choice == "scissors":
			print(f"You picked: {player_choice}\nComputer picked: {computer_choice}")
			print(computer_wins)
		elif computer_choice == "paper" and player_choice == "rock":
			print(f"You picked: {player_choice}\nComputer picked: {computer_choice}")
			print(computer_wins)
		elif computer_choice == "scissors" and player_choice == "paper":
			print(f"You picked: {player_choice}\nComputer picked: {computer_choice}")
			print(computer_wins)
		else:
			print(f"You picked: {player_choice}\nComputer picked: {computer_choice}")
			print(player_wins)