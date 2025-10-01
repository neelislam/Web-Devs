num = input("Enter number: ")
size = len(num)
flag = 0
for i in range(size):
    if num[i] == '4':
        flag += 1

print(f"Count of 4 is: {flag}")