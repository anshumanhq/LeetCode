class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=0:
            return "Input should be positive"
        if n%2==0:
            return n
        else:
            return n*2