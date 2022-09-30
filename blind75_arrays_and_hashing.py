# Arrays & Hashing #1
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


# Arrays & Hashing #2
# 242. Valid Anagram (Easy)
# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Checks if the lens equal each other. If they don't we know it is false. 
        if len(s) != len(t):
            return False

        # Initilize the hashmaps
        countStrings = {}
        countStringt = {}

        for i in range(len(s)):
            # Parameter:	    Description
            # keyname:	        Required. The keyname of the item you want to return the value from
            # value:	        Optional. A value to return if the specified key does not exist.
            #                   Default value None

            countStrings[s[i]] = countStrings.get(s[i], 0) + 1
            countStringt[t[i]] = countStringt.get(t[i], 0) + 1

        # Returns true if the hashmaps equal each other. Returns false if they do not.
        return countStrings == countStringt