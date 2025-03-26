'''
Question:
You are given a 2D integer grid of size m x n and an integer x. In one operation, you can add x to or subtract x from any element in the grid.
A uni-value grid is a grid where all the elements of it are equal.
Return the minimum number of operations to make the grid uni-value. If it is not possible, return -1.

Example 1:
Input: grid = [[2,4],[6,8]], x = 2
Output: 4
Explanation: We can make every element equal to 4 by doing the following: 
- Add x to 2 once.
- Subtract x from 6 once.
- Subtract x from 8 twice.
A total of 4 operations were used.

Example 2:
Input: grid = [[1,2],[3,4]], x = 2
Output: -1
Explanation: It is impossible to make every element equal.

Solution:
'''

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        flattened = []
        for sublist in grid:
            flattened.extend(sublist)
        
        preRem = flattened[0] % x
        N = len(flattened)
        #If Every num didn't have an same remainder then it is not possible to have change all into an same number
        for i in range(1 , N):
            rem = flattened[i] % x
            if preRem != rem:
                return -1
        
        flattened.sort()
        res = 0
        # By Getting midvalue we can know to which number we can transfer into, 
        # Because middle number after sorting is the Required number that others need to change into
        mid = flattened[N//2]

        for n in flattened:
            res += abs(mid - n) // x
        
        return res 
