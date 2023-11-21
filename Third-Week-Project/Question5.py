#Write a program to check if the given strings are anagram or not.

def isAnargam(a, b):
    a = a.lower()
    b = b.lower()
    return sorted(a) == sorted(b)
str1 = input("Provide a word")
str2 = input("Proivide another word")

if(isAnargam(str1, str2)):
    print(str1 and str2, "is a anargam number")
else:
    print(str1 and str2, "is not anargam number")