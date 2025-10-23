class Solution:
    def containsDuplicate(self, nums):
        hashset = set()

        for x in nums:
            if x in hashset:
                return True
            hashset.add(x)    
        return False