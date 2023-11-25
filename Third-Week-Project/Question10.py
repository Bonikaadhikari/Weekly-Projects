#Given an integer array nums sorted in non-decreasing order, return an array of the squares 
#of each number sorted in non-decreasing order.

def sortedSquares(nums):
    results = [num**2 for num in nums]
    results.sort()
    return results
num = [4, 2, 0, -6, -4]
result = sortedSquares(num)
print(result)