class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Agar string empty ya chhoti hai toh wapas bhej do
        if not s or len(s) == 0:
            return ""
        
        start = 0
        end = 0
        
        for i in range(len(s)):
            # Case 1: Odd length palindrome (center ek character hai)
            # Jaise "aba" mein 'b' center hai
            len1 = self.expand_around_center(s, i, i)
            
            # Case 2: Even length palindrome (center do characters ke beech hai)
            # Jaise "abba" mein 'bb' center hai
            len2 = self.expand_around_center(s, i, i + 1)
            
            # Sab se lambi length wala choose karo
            max_len = max(len1, len2)
            
            # Agar naya palindrome pehle se bada mila, toh uski boundaries update karo
            if max_len > (end - start):
                # Formula: start = i - (len - 1) // 2
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        
        # Slice karke longest palindromic substring return karo
        return s[start:end + 1]
    
    def expand_around_center(self, s: str, left: int, right: int) -> int:
        # Jab tak boundaries ke andar ho aur left aur right match karein
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # palindrome ki length return karo
        return right - left - 1
        