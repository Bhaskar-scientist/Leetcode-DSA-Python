# Final Submission Code
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        tails = []
        for num in nums:
            l, r = 0, len(tails)
            while l < r:
                m = (l + r) // 2
                if tails[m] < num:
                    l = m + 1
                else:
                    r = m
            if l == len(tails):
                tails.append(num)
            else:
                tails[l] = num
        return len(tails)