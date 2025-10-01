vowel = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}
char = input("Enter character: ")



if char in vowel:
    print(f"{char} is a vowel")
else:
    print(f"{char} is a consonant")