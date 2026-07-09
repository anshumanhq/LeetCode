class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_index = {} # char -> last seen index
        left = 0
        max_len = 0

        for right in range(len(s)):
            # If char already in window, move left past its last position
            if s[right] in char_index and char_index[s[right]] >= left:
                left = char_index[s[right]] + 1

            char_index[s[right]] = right # update last seen position
            max_len = max(max_len, right - left + 1)

        return max_len