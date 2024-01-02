# necessary imports
import secrets
import random
import string

# Getting password length
length = int(input("Enter password length: "))
if length < 9:
	print("Password should be at least 9 characters.")
	length= input("Please enter password length again: ")

# Available character sets
characterSets = {
    "lower": string.ascii_lowercase,
    "upper": string.ascii_uppercase,
    "digit": string.digits,
    "special": string.punctuation,
}

# Ask user to select character sets
selectedCharacterSets = []
while True:
    print("Choose character set for password:")
    for i, characterSet in enumerate(characterSets):
        print(f"{i + 1}. {characterSet}")
    print(f"{len(characterSets) + 1}. Exit")

    choice = int(input("Pick a number "))
    if 1 <= choice <= len(characterSets):
        selectedCharacterSets.append(characterSets[list(characterSets.keys())[choice - 1]])
    elif choice == len(characterSets) + 1:
        break
    else:
        print("Please pick a valid option!")

# Join all selected character sets
characterList = "".join(selectedCharacterSets)
password = []
for i in range(length):
    # Picking a random character from our 
    # character list
    randomchar = secrets.choice(characterList)
    # appending a random character to password
    password.append(randomchar)

# printing password as a string
print("A random password is " + "".join(password))




