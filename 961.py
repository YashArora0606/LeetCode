class Solution(object):
    def repeatedNTimes(self, A):
        # key: number | value: number of occurances
        h = {}
        for i in range(len(A)):
            if A[i] not in h:
                h[A[i]] = 1
            else:
                return A[i]
                
