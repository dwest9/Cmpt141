# David Emmanuel

# 11298443

# doe869

# jason coutu


def rock_paper_scissors_lizard_spock(player1,player2):

    '''
    computing the winner! of every input been entered by both players of the game

    :param player1: this player should input one word of the game function to determine the winner
    :param player2: this player should input one word of the game function to determine the winner
    :return: returning the winner of the game after calling out the function to print it out
    '''
    if player1 == player2:
        return " It was a tie!"
    if player1 == "rock" and (player2 == "scissors" or player2 == "lizard"):
        return "player 1 wins!"
    elif player1 == "paper" and (player2 == "rock" or player2 == "spock"):
        return "Player 1 wins!"
    elif player1 == "scissors" and (player2 == "paper" or player2 == "lizard"):
        return "Player 1 wins!"
    elif player1 == "spock" and (player2 == "scissors" or player2 == "rock"):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

p1 = input("Enter move for player 1: ").lower()
p2 = input("Enter move for player 2: ").lower()

winner = rock_paper_scissors_lizard_spock(p1, p2)
print(winner)


