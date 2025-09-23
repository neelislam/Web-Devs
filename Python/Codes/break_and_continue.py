i = 0

while i <= 12:
    print(i)
    i += 1
    if i % 2 != 0:
        continue
    print("even")
    if i == 9:
        break
