try:
    with open("C:\\Users\\Micha\\Desktop\\imhere.txt") as file:
        print(file.read())
except FileNotFoundError as e:
    print(f'The file was not found :(\n {e}')

