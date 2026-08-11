class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        n = len(s)
        
        while i < n and s[i] == ' ':
            i += 1
        
        if i == n:
            return 0
        
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
        
        result = 0
        INT_MAX = 2**31 - 1 
        INT_MIN = -2**31
        
        while i < n and s[i].isdigit():
            digit = int(s[i])
            if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > 7):
                return INT_MAX if sign == 1 else INT_MIN
            
            result = result * 10 + digit
            i += 1
        
        return sign * result