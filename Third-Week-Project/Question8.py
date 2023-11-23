#Given an integer array return true if any value appears at least twice in the array, 
#and return false if every element is distinct. 
def isRepeated(num):
  return len(num) != len(set(num))

num1 = [1, 2, 3, 4, 2]
num2 = [1, 2, 3, 4, 5]

print(isRepeated(num1))
print(isRepeated(num2))