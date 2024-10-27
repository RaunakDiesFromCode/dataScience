def create_dict():
    user_dict = {}
    
    while True:
        # Prompt the user for a key
        key = input("Enter a key (or 'done' to finish): ")
        
        if key.lower() == 'done':
            break
        
        value = input(f"Enter a value for key '{key}': ")
        
        user_dict[key] = value
    
    return user_dict


my_dict = create_dict()
print("Created Dictionary:")

for i in my_dict: 
    print(i,"\t",my_dict[i])
