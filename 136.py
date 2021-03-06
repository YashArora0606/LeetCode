class Solution(object):
    def singleNumber(self, nums):
        seen = {}
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1

        for num in seen:
            if seen[num] == 1:
                return num
        """
        :type nums: List[int]
        :rtype: int
        """

class Solution(object):
    def singleNumber(self, nums):
        n = 0
        for num in nums:
            n ^= num
        return n
        """
        :type nums: List[int]
        :rtype: int
        """
