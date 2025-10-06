def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error! Can't divide by zero!"
    return a / b

def mod(a, b):
    if b == 0:
        return "Error! Can't modulus by zero!"
    return a % b

print("=== Simple Calculator ===")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")

choice = input("Enter choice (1/2/3/4/5): ")

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == '2':
        print(num1, "-", num2, "=", sub(num1, num2))
    elif choice == '3':
        print(num1, "*", num2, "=", mul(num1, num2))
    elif choice == '4':
        print(num1, "/", num2, "=", div(num1, num2))
    elif choice == '5':
        print(num1, "%", num2, "=", mod(num1, num2))
    else:
        print("Oops! Wrong choice 😢")
except ValueError:
    print("Error! Please enter a number only.")

print("\n")

import random

print("=== Number Guessing Game ===")
print("Guess a number between 1 and 100")

number = random.randint(1, 100)
tries = 0

while True:
    guess = input("Enter your guess: ")
    try:
        guess = int(guess)
        tries += 1
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("Yay! You guessed it in", tries, "tries!")
            break
    except ValueError:
        print("Oops! That's not a number 😅")
