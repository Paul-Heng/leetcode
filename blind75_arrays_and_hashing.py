# Arrays & Hashing 
# 217. Contains Duplicate (Easy)
# https://leetcode.com/problems/contains-duplicate/

from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashSet = set()
        
        for num in nums:
            if num in hashSet:
                return True
            else:
                hashSet.add(num)
                
        return False


# Arrays & Hashing 
# 242. Valid Anagram (Easy)
# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
            
        return countS == countT