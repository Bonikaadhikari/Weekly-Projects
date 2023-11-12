#Madlib is a string concatenation project

Name = input("Enter your name: ")
age = int(input("Enter your age: "))
percentage = float(input("Enter the percentage you've secured: "))

madlib = f"My name is {Name}. I am {age} years old. I've secured {percentage:.2f}% in my final examination."

print(madlib)