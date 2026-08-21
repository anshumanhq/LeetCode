class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        
        def backtrack(current, open_count, close_count):
            # Base case: full valid string
            if open_count == n and close_count == n:
                result.append(current)
                return
            
            # Add '(' if possible
            if open_count < n:
                backtrack(current + '(', open_count + 1, close_count)
            
            # Add ')' if possible (only if close < open)
            if close_count < open_count:
                backtrack(current + ')', open_count, close_count + 1)
        
        backtrack('', 0, 0)
        return result