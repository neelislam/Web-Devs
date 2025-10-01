def string_prefix_copy(string,num_of_copy):
    if len(string) <= 2:
        return string * num_of_copy
    else:
        string_first_two = string[:2]
        return string_first_two * num_of_copy




String = input("Enter a string: ")

copy = int(input("Enter number of copies: "))
print(string_prefix_copy(String,copy))