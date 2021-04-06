# Note that for TR1, we were able to start from the ends since we could be certain that there was no water on the ends. In 3 dimensions, this cannot be the case, but we can say that the entire list of outermost elements will form some border such that no element on the border contains water. We use this as our starting point. The most important thing about the border is the minimum height, since it limits the amount of water, and therefore we use a min heap or priority queue that stores the height for priority and location to show us which elements are in the border. My main thought process is that every element that has water on it must be surrounded by ONLY a water block or a border , and if we can keep pushing the minimum border wall inward, we can find all elements that are not a border (water)
# 1. create a min heap to represent the border
# 2. use the height of the index for priority
# 3. store i and j as its position in the matrix as well
# 4. start by creating a min heap of the border
# 5. store the lowest value of the border
# 6. for all elements in the border that have that value, check their cardinal neighbors
# 7. if the neighbor is greater, make it part of the border
# 8. remove the element from the border (pop min)
# 9. if the neighbor is smaller, it must have water
# 10. increment the total water by min of heap minus the water at the index
# 11. once a water block is found, continue on all the neighbors of the water block using the same value for the min of min heap from before (optimization)

# we need to keep track of the indices that have been checked already, so maybe we need a hashmap for this, but actually maybe not since we can just iterate until the border heap is empty
# I'm worried about some weird edge cases like the following:
# 0 0 0 0 0 0 0 0 0
# 0 1 1 1 0 1 1 1 0
# 0 1 0 1 0 1 0 1 0
# 0 1 1 1 0 1 1 1 0
# 0 0 0 0 0 0 0 0 0
# actually I think it still works
# because you would end up yeeting all the elements you start with as your border (outer 0s), and then your borders would end up being just the 1s
# and then it would locate that water can exist inside
# and you would have min_of_heap = 1 => total += 1 - 0
# and this happens twice
# so total = 2
# which is correct
# ok that's enough thinking for today im gonna try to code it tmrw



import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        
        border = []
        m = len(heightMap)
        n = len(heightMap[0])
        
        # If either are < 3 then the entire system is border
        if m < 3 or n < 3:
            return 0
        
        # Construct initial border O(n + m - 4)
        for i in range(m):
            heappush(border, (heightMap[i][0], (i, 0)))
            heappush(border, (heightMap[i][n-1], (i, n-1)))
        for i in range(1, n-1):
            heappush(border, (heightMap[0][i], (0, i)))
            heappush(border, (heightMap[m-1][i], (m-1, i)))
        
        while len(border > 0):