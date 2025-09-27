#  Write a Python program to print the following string in a specific format (see the output).
# Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
# Output :

# Twinkle, twinkle, little star,
# 	How I wonder what you are! 
# 		Up above the world so high,   		
# 		Like a diamond in the sky. 
# Twinkle, twinkle, little star, 
# 	How I wonder what you are


poem = input("Enter the poem: ")

poem = poem.replace("star, ", "star,\n\t").replace("! ", "!\n\t\t").replace(". ", ".\n").replace("sky. ", "sky.\n").replace("are", "are")


print(poem)