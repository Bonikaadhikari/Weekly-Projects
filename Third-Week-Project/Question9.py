#Given a positive integer num, return true if num is a perfect square or false otherwise.
def isPerfectSquare(num):
        for i in range(1, num+1):
            if i * i == num:
                return True
            if i * i > num:
                return False
num = int(input("Provide a number"))
result = isPerfectSquare(num)
print(result)

