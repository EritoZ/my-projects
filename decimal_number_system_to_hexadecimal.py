n = int(input())
total = ""
while n != 0:
    new_number = n // 16
    remainder = n % 16
    n = new_number
    if remainder == 10:
        remainder = "A"
    elif remainder == 11:
        remainder = "B"
    elif remainder == 12:
        remainder = "C"
    elif remainder == 13:
        remainder = "D"
    elif remainder == 14:
        remainder = "E"
    elif remainder == 15:
        remainder = "F"

    total += str(remainder)

print(total[::-1])
