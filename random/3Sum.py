class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums = sorted(nums)
        triplets = set()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            low = i + 1
            high = len(nums) - 1
            while low < high:
                summation = nums[i] + nums[low] + nums[high]
                if summation > 0:
                    high -= 1
                elif summation < 0:
                    low += 1
                else:
                    triplets.add((nums[i], nums[low], nums[high]))
                    high -= 1
                    low += 1
        return list(triplets)