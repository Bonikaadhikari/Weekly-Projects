#Take a sentence as input from the user and print the length of the sentence 
#Also, convert the string to uppercase and reverse it.

name = input("What is your name?")
print(name)
print(f"The length of {name} of", len(name))

upper = name.upper()
print(upper)

r = name[::-1]
print(r)