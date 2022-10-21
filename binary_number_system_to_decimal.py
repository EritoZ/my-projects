n = input()
total = 0
for i, character in enumerate(n[::-1]):
    total += int(character) * 2 ** i

print(total)