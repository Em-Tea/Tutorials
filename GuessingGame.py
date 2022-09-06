import random
ran = 10
#ran = random.randint(1, 25)
cnt = 5
while cnt >= 1:
    ans = int(input(f'You have {cnt} guesses! Enter your guess: '))
    if ans == (ran <= ran - 4) or ans == ran + 1 or ans == ran - 2 or ans == ran + 2:
        print("Hot")
        cnt -= 1
    elif ans == ran + 3 or ans == ran - 3:
        print("Warm")
        cnt -= 1
    elif ans == ran + 4 or ans == ran - 4 or ans == ran + 5 or ans == ran - 5:
        print("Cold")
        cnt -= 1
    elif ans == ran:
        print(f'You win! The answer was indeed {ran}')
        break
    else:
        print("Freezing")
        cnt -= 1
