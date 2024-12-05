# 4a
def winner(player1, player2):
    # Dictionary mapping each choice to what it defeats
    beats = {
        'R': 'S',
        'S': 'P',
        'P': 'R'
    }

    if player1 == player2:
        return 0  # Tie
    elif beats[player1] == player2:
        return 1  # Player 1 wins
    else:
        return 2  # Player 2 wins

# 4b
player1 = ''
player2 = ''

score1 = 0
score2 = 0

while True:
    print("Enter 'R' for rock, 'P' for paper, or 'S' for scissors.")
    player1 = input('Player 1, enter your choice: ').upper()
    player2 = input('Player 2, enter your choice: ').upper()

    if player1 not in ['R', 'P', 'S'] or player2 not in ['R', 'P', 'S']:
        break
    else:
        result = winner(player1, player2)
        if result == 0:
            print('It\'s a tie!')
        elif result == 1:
            print('Player 1 wins!')
            score1 += 1
        else:
            print('Player 2 wins!')
            score2 += 1

    print()

print(f'Score:\nPlayer 1: {score1}\nPlayer 2: {score2}')

# 4c
"""
winner = score1 if score1 > score2 else score2

highest_scores = load_scores()
for i in range(3):
    if winner > highest_scores[i]:
        highest_scores[i] = winner
        break
        
store_scores(highest_scores.sort(reverse=True))
"""