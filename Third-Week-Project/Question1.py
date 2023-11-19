#Define a function that takes two values as arguments and take two inputs from the user and pass the value 
#when the function is called.Perform addition, subtraction, multiplication, division, and modulos operation 
#inside the function and return each of the values and print the results inside the function.

def isOperators(a, b):
    ans1 = a + b
    ans2 = a - b
    ans3 = a * b
    ans4 = a / b
    ans5 = a % b

    print(f"The addition of {a} and {b} is {ans1}")
    print(f"The subtraction of {a} and {b} is {ans2}")
    print(f"The multiplication of {a} and {b} is {ans3}")
    print(f"The division of {a} and {b} is {ans4}")
    print(f"The Modulus of {a} and {b} is {ans5}")
x = int(input("Enter first number"))
y = int(input("Enter Second number"))

isOperators(x, y)




