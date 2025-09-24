try:
    print(15/0)
except ZeroDivisionError as e:
    print("Error:", e)

file_path = "/Users/rabiul/Documents/Projects/Web Devs/Python/Codes/chipa.txt"

# Read the file first
with open(file_path, "r") as f:
    content = f.read()
    print("Before writing:")
    print(content)

# Append text
with open(file_path, "a") as f:
    f.write("\nI am fine.")

# Read again to confirm the new content
with open(file_path, "r") as f:
    updated = f.read()
    print("\nAfter writing:")
    print(updated)
