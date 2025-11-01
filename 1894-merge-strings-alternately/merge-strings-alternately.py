class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []  # result
        i,j = 0,0 # Two pointers

        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            i+=1
            res.append(word2[j])
            j+=1
        
        res.extend(word1[i:])
        res.extend(word2[j:])
        
        return "".join(res)