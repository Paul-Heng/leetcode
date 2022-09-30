from typing import List

# Arrays & Hashing #1
# 217. Contains Duplicate (Easy)
# https://leetcode.com/problems/contains-duplicate/

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
            # Parameter:        Description
            # keyname:          Required. The keyname of the item you want to return the value from
            # value:            Optional. A value to return if the specified key does not exist.
            #                   Default value None

            countStrings[s[i]] = countStrings.get(s[i], 0) + 1
            countStringt[t[i]] = countStringt.get(t[i], 0) + 1

        # Returns true if the hashmaps equal each other. Returns false if they do not.
        return countStrings == countStringt

# Arrays & Hashing #3
# 1. Two Sum (Easy)
# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

# Arrays & Hashing #4
# 49. Group Anagrams (Medium)
# https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for string in strs:
            count = [0] * 26 

            for char in string:
                # Give an +1 at each char
                # A = 0, B = 1
                # ord('a') - ord('a') = 0
                # ord('b') - ord('a') = 1
                count[ord(char) - ord('a')] += 1

            # Lists cannot be keys for dictionaries
            # So we turn them into tuples
            # We also check if the key exists before trying to append a new item
            # If it doesn exist we make a new list
            if tuple(count) in res.keys():
                res[tuple(count)].append(string)
            else:
                res[tuple(count)] = [string]
        return res.values()