import random

ran = random.randint(1, 25)
guess_limit = 5
while guess_limit >= 1:
    ans = int(input(f'You have {guess_limit} guesses! Enter your guess: '))
    if ans == (ran_num <= ran_num - 4) or ans == ran_num + 1 or ans == ran_num - 2 or ans == ran_num + 2:
        print("Hot")
        guess_limit -= 1
    elif ans == ran_num + 3 or ans == ran_num - 3:
        print("Warm")
        guess_limit -= 1
    elif ans == ran_num + 4 or ans == ran_num - 4 or ans == ran_num + 5 or ans == ran_num - 5:
        print("Cold")
        guess_limit -= 1
    elif ans == ran_num:
        print(f'You win! The answer was indeed {ran_num}')
        break
    else:
        print("Freezing")
        guess_limit -= 1
