from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        # 1. Find pivot
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        if i == -1:                     # whole array non-increasing
            nums.reverse()
            return
        
        # 2. Find successor (rightmost > nums[i])
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        
        # 3. Swap
        nums[i], nums[j] = nums[j], nums[i]
        
        # 4. Reverse suffix
        left, right = i + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1