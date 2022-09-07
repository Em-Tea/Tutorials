"""
We use a dictionary when we need to store information that come as key value pairs
e.g. Customer:
KEY  |     VALUE
Name: John Smith
Email: john@gmail.com
phone: 1029
"""

customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}

#customer["name"] = "Jack Smith"

print(customer.get("name"))
#OR
print(customer["age"])

phone = "1234"
digits_mapping = {
    "1": "One ",
    "2": "Two ",
    "3": "Three ",
    "4": "Four "
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!")
print(output)

message = input(">")
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
print(output)