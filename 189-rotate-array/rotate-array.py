class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x = 0
        while x < k:
            y = nums[-1]
            nums.insert(0,y)
            nums.pop()
            x+=1
