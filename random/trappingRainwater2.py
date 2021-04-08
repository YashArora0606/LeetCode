# Note that for TR1, we were able to start from the ends since we could be certain that there was no water on the ends. In 3 dimensions, this cannot be the case, but we can say that the entire list of outermost elements will form some border such that no element on the border contains water. We use this as our starting point. The most important thing about the border is the minimum height, since it limits the amount of water, and therefore we use a min heap or priority queue that stores the height for priority and location to show us which elements are in the border. My main thought process is that every element that has water on it must be surrounded by ONLY a water block or a border , and if we can keep pushing the minimum border wall inward, we can find all elements that are not a border (water)

# 1. create a min heap to represent the border
# 2. use the height of the index for priority
# 3. store i and j as its position in the matrix as well
# 4. start by creating a min heap of the border
# 5. store the lowest value of the border
# 6. for all elements in the border that have that value, check their cardinal neighbors
# 7. if the neighbor is greater (or equal?), make it part of the border
# 8. remove the element from the border (pop min)
# 9. if the neighbor is smaller, it must have water
# 10. increment the total water by min of heap minus the water at the index
# 11. once a water block is found, continue on all the neighbors of the water block using the same value for the min of min heap from before (optimization)

# Edits to the process while solving:
# 1. Use a matrix of booleans to keep track of what is seen, since the space used is n*m anyway
# 2. On step 6, you don't need to check all elements with that border value, since you will be popping and always be at the lowest in the border anyway (saves one useless while loop)
# 3. Before step 7, make sure to check that the neighbor is actually in the bounds of the matrix
# 4. Step 8 can be done earlier, since you will always be removing the checked value from the border
# 5. Step 7 logic is actually wrong. You cannot ONLY add if it's greater and remove if it's smaller, since you will never empty your border. Instead, always remove the element being checked. If neighbor is bigger, you can add it to the border, and if it is smaller, you can still add it to the border as the height of the orginal square, since the water kind of makes a border itself!


import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        
        # If either are < 3 then the entire system is border
        m = len(heightMap)
        n = len(heightMap[0])
        if m < 3 or n < 3:
            return 0
        
        # Construct boolean board to tracked already checked blocks
        checked = []
        for i in range(m):
            checked.append([False]*n)

        # Construct initial border
        border = []
        for i in range(m):
            heappush(border, (heightMap[i][0], (i, 0)))
            heappush(border, (heightMap[i][n - 1], (i, n - 1)))
            checked[i][0] = True
            checked[i][n - 1] = True
        for i in range(1, n-1):
            heappush(border, (heightMap[0][i], (0, i)))
            heappush(border, (heightMap[m - 1][i], (m - 1, i)))
            checked[0][i] = True
            checked[m - 1][i] = True        

        water = 0
        
        # Continue as long as there are elements to check
        while border:
            
            # You can actually pop right away, since you have always mark the block as checked
            border_block = heappop(border)
            height = border_block[0]

            x = border_block[1][0]
            y = border_block[1][1]

            cardinal_neighbors = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

            for neighbor in cardinal_neighbors:

                n_x = neighbor[0]
                n_y = neighbor[1]
                
                in_bounds = n_x >= 0 and n_y >= 0 and n_x < m and n_y < n

                if in_bounds and not checked[n_x][n_y]:

                    height_at_neighbor = heightMap[n_x][n_y]

                    # Push whichever is greater between the height and neighbor's height
                    # since the water will fill up to that level anyway
                    if height_at_neighbor >= height:
                        heappush(border, (height_at_neighbor, (n_x, n_y)))
                    else:
                        water += height - height_at_neighbor
                        heappush(border, (height, (n_x, n_y)))

                    checked[n_x][n_y] = True
                    
        return water
