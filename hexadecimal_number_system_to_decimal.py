n = input()
total = 0
for i, character in enumerate(n[::-1]):
    if character == "A":
        character = 10
    elif character == "B":
        character = 11
    elif character == "C":
        character = 12
    elif character == "D":
        character = 13
    elif character == "E":
        character = 14
    elif character == "F":
        character = 15

    total += int(character) * 16 ** i

print(total)
