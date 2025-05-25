from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []

        def backtrack(i): # i is the index in nums that we're currently deciding to include or exclude
            if i == n:
                res.append(sol[:])
                return
            
            # Don't pick nums[i]
            backtrack(i + 1)

            # Pick nums[i]
            sol.append(nums[i])
            backtrack(i+1)
            sol.pop()
        
        # Start the backtracking from index 0
        backtrack(0)
        return res