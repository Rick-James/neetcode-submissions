class Solution:
    def isPalindrome(self, s: str) -> bool:
        #left index
        l = 0
        #right index
        r = len(s) - 1
        #while the left index is less than the right index (they don't cross)
        while l < r:
            #if the pointer is not alpha numeric, adjust the pointer to the next index
            while l < r and not s[l].isalnum():
                l += 1
            #if the pointer is not alpha numeric, adjust the pointer to the next index
            while l < r and not s[r].isalnum():
                r -= 1
            #if the two values are not equal, it's not a palindrome
            if s[l].lower() != s[r].lower():
                return False
            #adjust the l & r pointers after each pass
            l = l + 1
            r = r - 1
        #if we break out of the loop and haven't returned false, it must be true :) 
        return True     