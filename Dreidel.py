import random

starting_amount = 10
pot = 0
ante = 2
players = []


def init_game():
	global players
	player_count = int(input('How many players? '))
	for i in range(player_count):
		names = input('Enter names: ')
		players.append([names, starting_amount])
	reset_pot(players)
	print(pot)
	print(players)

def reset_pot(players):
	global pot
	pot = 0
	for player in players:
		deposit_ante(player)
	check_scores(players)

def deposit_ante(player):
	global pot
	if player[1] >= ante:
		player[1] -= ante
		pot += ante
	else:
		pot += player[1]
		player[1] = 0

def play_round(players):
	global pot
	for player in players:
		input(player[0] + ", press enter to spin.")
		spin_result = spin()
		print(player[0], "got a", spin_result + "!")
		if spin_result == "gimmel":
			player[1] += pot
			reset_pot(players)
		elif spin_result == "hey":
			half = pot // 2
			player[1] += half
			pot -= half
			if pot == 0:
				reset_pot(players)
		elif spin_result == "shin":
			deposit_ante(player)

def spin():
	spin_result = random.randint(1, 4)
	spin_result_string = ""
	if spin_result == 1:
		spin_result_string = "nun"
	elif spin_result == 2:
		spin_result_string = "gimmel"
	elif spin_result == 3:
		spin_result_string = "hey"
	elif spin_result == 4:
		spin_result_string = "shin"
	return spin_result_string

def print_scores(players):
	for player in players:
		print(player[0] + "'s score is", player[1])

def check_scores(players):
	for player in players:
		if player[1] <= 0:
			print(player[0], "is out!")
			players.remove(player)
	if len(players) <= 1:
		return True
	return False

def play_game(players):
	end_game = False
	while not end_game:
		play_round(players)
		print_scores(players)
		end_game = check_scores(players)

def main():
	global players
	init_game()
	play_game(players)
	
main()