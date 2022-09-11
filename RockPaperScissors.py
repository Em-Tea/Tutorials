import random

choices = ["Rock", "Paper", "Scissors"]
player = None
user_score = 0
comp_score = 0
comp = None

while user_score < 3 and comp_score < 3:
    player = None
    comp = random.choice(choices)
    while player not in choices:
        player = input("Please choose Rock, Paper or Scissors: ").capitalize()
    if player == comp:
        print(f"Computer: {comp}\nPlayer: {player}\nIt's a tie!")
    elif player == 'Rock':
        if comp == 'Paper':
            print(f"Computer: {comp}\nPlayer: {player}\nYou win!")
            user_score += 1
        if comp == 'Scissors':
            print(f"Computer: {comp}\nPlayer: {player}\nYou lose!")
            comp_score += 1
    elif player == 'Paper':
        if comp == 'Rock':
            print(f"Computer: {comp}\nPlayer: {player}\nYou win!")
            user_score += 1
        if comp == 'Scissors':
            print(f"Computer: {comp}\nPlayer: {player}\nYou lose!")
            comp_score += 1
    elif player == 'Scissors':
        if comp == 'Paper':
            print(f"Computer: {comp}\nPlayer: {player}\nYou win!")
            user_score += 1
        if comp == 'Rock':
            print(f"Computer: {comp}\nPlayer: {player}\nYou lose!")
            comp_score += 1
    print(f'User score = {user_score}, Comp score = {comp_score}')
print("Game Over!")