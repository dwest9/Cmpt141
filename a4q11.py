# David Emmanuel

# 11298443

# doe869

# jason coutu


def rock_paper_scissors_lizard_spock(player1,player2):

    if player1 == player2:
        print("It was a tie!")
        return 0
    if player1 == "rock" and (player2 == "scissors" or player2 == "lizard"):
        print("player 1 wins!")
        return 1
    elif player1 == "paper" and (player2 == "rock" or player2 == "spock"):
        print("Player 1 wins!")
        return 1
    elif player1 == "scissors" and (player2 == "paper" or player2 == "lizard"):
        print("Player 1 wins!")
        return 1
    elif player1 == "spock" and (player2 == "paper" or player2 == "lizard"):
        print("Player 1 wins!")
        return 1
    elif player1 == "lizard" and (player2 == "scissors" or player2 == "rock"):
        print("Player 1 wins!")
        return 1
    elif player1 == "end" or player2 == "end":
        exit()
    else:
        print("Player 2 wins!")
        return 2

player1_points=0

player2_points=0

def game_loop(rounds):
    # play against the opponent until someone wins best of n games
    # to win, you must win ceil(n/2) games (ie 2/3, 3/5, 4/7)
    global player1_points, player2_points, total_game_rounds
    for i in range(rounds):
        player1 = input("Enter move for player 1: ").lower()
        player2 = input("Enter move for player 2: ").lower()
        winner = rock_paper_scissors_lizard_spock(player1,player2)

        total_game_rounds += 1
        if winner == 1:
            player1_points += 1
            print('player 1 won this round. The score is', player1_points, ":", player2_points)
        elif winner == 2:
            player2_points += 1
            print('player 2 won this round. The score is', player1_points, ":", player2_points)
        elif winner == 0:
            print('It is a tie. The score is', player1_points, ',', player2_points)

        if max(player1_points,player2_points) > (rounds/2):
            break

    if player1_points > player2_points:
        print('Player 1 wins the game with', player1_points,'points out of', total_game_rounds)
        if total_game_rounds >= rounds:
            print('player 1 won with the last move')
    elif player2_points > player1_points:
        print('Player 2 wins the game with', player2_points,'points out of', total_game_rounds)
        if total_game_rounds >= rounds:
            print('player 2 won with the last move')
    elif player1_points == player2_points:
        print('Last move to go. First to win, wins the game')
        rounds=1
        game_loop(rounds)

total_game_rounds=0
rounds=int(input("How many rounds is this game: "))
game_loop(rounds)
