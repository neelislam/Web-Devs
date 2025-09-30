def string_copy(text, n_copy):
    if text[:1] == "-":
        return text[1:] * n_copy
    else:
        return text * n_copy


Text = input("Enter a string: ")
copy_number = int(input("Enter number of copies: "))
print(string_copy(Text, copy_number))