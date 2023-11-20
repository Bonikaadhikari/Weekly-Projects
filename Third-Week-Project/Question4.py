#Write a program to check if the given number is palindrome or not.

def IsPalindrome(a):
   num = str(a)

   return num == num[::-1]

n = int(input("Provide a number"))
if IsPalindrome(n):
    print(n, "is a palindrome number")
else:
    print(n, "is not palindrome number")
