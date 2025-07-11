from typing import List

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        answer = nums[0]
        largest = nums[0]
        for num in nums:
            if abs(num) < abs(answer):
                answer = num
            elif abs(num) == abs(answer):
                if num > answer:
                    answer = num
        return answer