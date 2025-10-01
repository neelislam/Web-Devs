def value_in_group_tester(value, group):
    if value in group:
        return True
    else:
        return False
    

premium = [1,5,8,3]    
    
entry_def = int(input("Enter a number: "))

print(value_in_group_tester(entry_def, premium))    