class Solution:
    # Attempt 1: Could be improved
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        triplets = set()
        nums = sorted(nums)
        
        for i in range(len(nums)):
            n = nums.copy()
            target = -1 * n.pop(i)
            
            left = 0
            right = len(n) - 1
            while left < right:
                if n[left] + n[right] == target:
                    triplets.add(tuple(sorted([n[left], n[right], target * -1])))
                    left += 1
                    right -= 1
                elif n[left] + n[right] < target:
                    left += 1
                else:
                    right -= 1
        ret = []
        for triplet in triplets:
            ret.append(list(triplet))
        return ret
