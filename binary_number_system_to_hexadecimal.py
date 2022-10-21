n = input()[:: - 1]
total = ""
for i in range(0, len(n), 4):
    while len(n) % 4 != 0:
        n += "0"
    character = n[i:i + 4][:: - 1]
    if character == "0000":
        character = "0"
    elif character == "0001":
        character = "1"
    elif character == "0010":
        character = "2"
    elif character == "0011":
        character = "3"
    elif character == "0100":
        character = "4"
    elif character == "0101":
        character = "5"
    elif character == "0110":
        character = "6"
    elif character == "0111":
        character = "7"
    elif character == "1000":
        character = "8"
    elif character == "1001":
        character = "9"
    elif character == "1010":
        character = "A"
    elif character == "1011":
        character = "B"
    elif character == "1100":
        character = "C"
    elif character == "1101":
        character = "D"
    elif character == "1110":
        character = "E"
    elif character == "1111":
        character = "F"

    total += character

print(total[::-1])
