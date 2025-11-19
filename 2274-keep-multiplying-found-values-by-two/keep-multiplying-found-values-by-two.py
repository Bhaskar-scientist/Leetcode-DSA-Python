from typing import List

class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        # Keep multiplying `original` by 2 while it exists in `nums`
        while original in nums:
            original *= 2
        return original
