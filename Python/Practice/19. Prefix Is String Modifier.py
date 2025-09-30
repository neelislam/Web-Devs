def new_string(text):
    if len(text) >=2 and text[:2] == "Is":
        return text
    else: 
        return "Is" + text
    



Text = input("Enter a string: ")
print(new_string(Text))
