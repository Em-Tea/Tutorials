print("[()---|C4R G4M3|---()]")
print("Type 'Help' to display commands.")
car_movement = False
user_choice = ""

while True:
    user_choice = input("Please enter a command: ").upper()
    if user_choice == "HELP":
        print("Start - starts the car. \nStop - stops the car. \nQuit - quit game.")
    elif user_choice == "START":
        if not car_movement:
            print("The car starts and gets moving.")
            car_movement = True
        else:
            print("The car is already moving!")
    elif user_choice == "STOP":
        if car_movement:
            print("The car stops")
            car_movement = False
        else:
            print("The car is not moving!")
    elif user_choice == "QUIT":
        print("You quit the game.")
        break
    else:
        print("Invalid selection.")