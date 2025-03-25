# Your Student ID: 220543603
# Your Name and Surname: Muhammed Elubeyid

user_input = input("Enter a string: ")

character_count = {}

for character in user_input:
    if character in character_count:
        character_count[character] += 1
    else:
        character_count[character] = 1  


print("Character frequencies:")
for character in sorted(character_count):
    print(character, ":", character_count[character])
