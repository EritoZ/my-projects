n = input()
for character in n:
    if character == "0":
        character = "0000"
    elif character == "1":
        character = "0001"
    elif character == "2":
        character = "0010"
    elif character == "3":
        character = "0011"
    elif character == "4":
        character = "0100"
    elif character == "5":
        character = "0101"
    elif character == "6":
        character = "0110"
    elif character == "7":
        character = "0111"
    elif character == "8":
        character = "1000"
    elif character == "9":
        character = "1001"
    elif character == "A":
        character = "1010"
    elif character == "B":
        character = "1011"
    elif character == "C":
        character = "1100"
    elif character == "D":
        character = "1101"
    elif character == "E":
        character = "1110"
    elif character == "F":
        character = "1111"

    print(character, end="")
