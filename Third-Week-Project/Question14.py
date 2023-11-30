# Given a binary array nums, return the maximum number of consecutive 1's in the array.
def findMaxConsecutiveOnes(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        temp = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                temp += 1
            else: 
                temp = 0
            
            if count < temp:
                count = temp 
            else: 
                count = count
        return count

print(findMaxConsecutiveOnes([1,1,0,1,1,1]))
