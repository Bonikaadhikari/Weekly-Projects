#Given an integer array nums of length n, you want to create an array ans of length 2n 
#where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed)
def getConcatenation(nums):
    ans = []
    for i in range(2):
        for n in nums:
            ans.append(n)
    return ans
nums = [1,3,4]
ans = getConcatenation(nums)
print(ans)