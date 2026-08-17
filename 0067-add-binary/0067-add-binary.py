class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        num1=int(a,2)
        num2=int(b,2)
        total=num1+num2
        result=bin(total)[2:]
        return result