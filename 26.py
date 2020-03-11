class Solution(object):
    def removeDuplicates(self, nums):
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                nums.pop(i-1)
                i -= 1
            i += 1
        return len(nums)
        
