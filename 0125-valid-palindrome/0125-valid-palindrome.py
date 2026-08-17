class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        filtered = ''.join(ch.lower() for ch in s if ch.isalnum())
        
        return filtered == filtered[::-1]