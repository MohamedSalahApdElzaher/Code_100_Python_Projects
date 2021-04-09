Placeholder = "[name]"

with open('./Input/Names/invited_names.txt') as names:
    n = names.readline()

with open('./Input/Letters/starting_letter.txt') as l:
    letters = l.read()
    for name in n:
        strippedName = name.strip()
        new_letter = letters.replace(Placeholder, strippedName)
        with open(f"./Output/ReadyToSend/letter_for_{strippedName}.txt", mode='w') as endLetter:
            endLetter.write(new_letter)
