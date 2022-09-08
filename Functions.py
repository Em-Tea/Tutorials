def greet_user(first_name, last_name):
    print(f'Hi there, {first_name} {last_name}!')
    print("Welcome aboard.")


print("Start")
greet_user("John", "Smith")
print("Finish")


def square(num):
    return num * num


print(square(3))


message = input(">")
def emoji_converter(message):
    words = message.split(' ')
    print(words)
    emojis = {
        ":)": "😊",
        ":(": "😔",
        ":|": "😐"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output

print(emoji_converter(message))