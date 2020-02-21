class Solution(object):
    def decompressRLElist(self, nums):
        ret = []
        for i in range(len(nums)/2):
            ret += nums[2*i] * [nums[2*i + 1]]
        return ret
        """
        :type nums: List[int]
        :rtype: List[int]
        """
            
