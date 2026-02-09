# name = input("Enter your name: ")

# # Prints the name of user and greets good afternoon
# print(f"Good Afternoon {name}")



# ============== User input in string =============


# letter = f'''
# Dear {input("Enter Name: ")},
# You are selected!
# {input("Enter date: ")}
# '''

# # prints the string with user inputs
# print(letter)


# other way

# letter = f'''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''

# print(letter.replace("<|Name|>","Naman").replace("<|Date|>", "24 september 2050"))



# ============== Detect Double space in a string =============


# str = "Hello  How are You?"

# # Finds in the string and returns index
# print(str.find("  "))



# ================ Replace double space with single ===============


str = "Hello  How are You?"


print(str.replace("  ", " "))