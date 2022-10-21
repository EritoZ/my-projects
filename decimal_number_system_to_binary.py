n = int(input())
total = ""
while n != 0:
    new_number = n // 2
    remainder = n % 2
    n = new_number
    total += str(remainder)

print(total[::-1])
