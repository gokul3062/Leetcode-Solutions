'''
Question:

You are given an integer array nums of length n and a 2D array queries where queries[i] = [li, ri, vali].

Each queries[i] represents the following action on nums:

Decrement the value at each index in the range [li, ri] in nums by at most vali.
The amount by which each value is decremented can be chosen independently for each index.
A Zero Array is an array with all its elements equal to 0.

Return the minimum possible non-negative value of k, such that after processing the first k queries in sequence, nums becomes a Zero Array. If no such k exists, return -1.

 

Example 1:

Input: nums = [2,0,2], queries = [[0,2,1],[0,2,1],[1,1,3]]

Output: 2

Explanation:

For i = 0 (l = 0, r = 2, val = 1):
Decrement values at indices [0, 1, 2] by [1, 0, 1] respectively.
The array will become [1, 0, 1].
For i = 1 (l = 0, r = 2, val = 1):
Decrement values at indices [0, 1, 2] by [1, 0, 1] respectively.
The array will become [0, 0, 0], which is a Zero Array. Therefore, the minimum value of k is 2.
Example 2:

Input: nums = [4,3,2,1], queries = [[1,3,2],[0,2,1]]

Output: -1

Solution:

'''


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)

        #Check an nums array can become an Zero Array
        def can_make_zero_array(k):
            diff = [0] * (n + 1)
            
            for i in range(k):
                left, right, val = queries[i]
                diff[left] += val
                diff[right + 1] -= val
            
            curr_val = 0
            for i in range(n):
                curr_val += diff[i]
                #This condition makes whether some index in nums can become zero or not
                if curr_val < nums[i]:
                    return False
            
            return True
        
        if all(x == 0 for x in nums):
            return 0
        
        left, right = 1, len(queries)
        
        if not can_make_zero_array(right):
            return -1

        # Binary Search on nums
        while left < right:
            mid = left + (right - left) // 2
            #If mid satisfies then Shrink the right and still there may be least queries to make Zero Array
            if can_make_zero_array(mid):
                right = mid
            else:
                left = mid + 1
                    
        return left
