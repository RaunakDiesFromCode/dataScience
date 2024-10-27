def create_dict():
    user_dict = {}
    
    while True:
        key = input("Enter a key (or 'done' to finish): ")
        
        if key.lower() == 'done':
            break
        
        value = input(f"Enter a value for key '{key}': ")
        
        user_dict[key] = value
    
    return user_dict

def swap_keys_values(d):
    rev = {}
    for key, value in d.items():
        rev[value] = key
    return rev

mydict = create_dict()
print("Created Dictionary:", mydict)

rev_dict = swap_keys_values(mydict)
print("Reversed Dictionary:", rev_dict)
