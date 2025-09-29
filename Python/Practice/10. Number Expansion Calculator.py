# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
# Sample value of n is 5
# Expected Result : 615


number = input("Enter an integer: ")
n = int(number)
res = n + int(f"{n}{n}") + int(f"{n}{n}{n}")
print(f"The result is: {res}")