# LeetCode: https://leetcode.com/problems/valid-parentheses/
# NeetCode: https://www.youtube.com/watch?v=WTzjTskDFMg

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hashMap =   {
                    '(': ')', 
                    '{': '}', 
                    '[': ']'
                    }
        
        # Iterate through all the chars in string one by one
        # O(n) - since we going through each char in the string
        for char in s:
            if char in hashMap.keys():
                stack.append(char)
            else:
                # This check is the stack is empty.
                # If the stack is empty that means we are using a closed parenthesis without an open parenthesis
                if stack:
                    prevChar = stack.pop()
                    if hashMap[prevChar] != char:
                        return False
                else:
                    return False
                
        # If there is something in the stack that means a parenthesis was not closed
        # If there is nothing in the stack that means every parentsis was closed
        # You can shorten this by saying "return not stack" but this way is easier to read
        if stack:
            return False
        else:
            return True
