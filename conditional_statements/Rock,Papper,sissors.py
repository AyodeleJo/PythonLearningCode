# Scissors beats paper, Paper beats rock, Rock beats scissors
player1 = input("Enter a choice(rock, paper, scissors)")
player2 = input("Enter a choice(rock, paper, scissors)")
if player1 == "rock" and player2 == "scissors":
    result = player1
    print(result, "smashes sissors player 1 wins")
elif player2 == "rock" and player1 == "scissors":
    result = player2
    print(result, "smashes sissors player 2 wins")
elif player1 == "paper" and player2 == "rock":
    result = player1
    print(result, "smashes rock player 1 wins")
elif player2 == "papper" and player1 == "rock":
    result = player2
    print(result, "smaches rock player 2 wins")
elif player1 == "scissors" and player2 == "paper":
    result = player1
    print(result, "smaches paper player 1 wins")
else:
    print(player2, "Smaches paper palyer 2 wins")
