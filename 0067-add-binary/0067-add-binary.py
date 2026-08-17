class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        num1,num2=int(a,2),int(b,2)
        return bin(num1+num2)[2:]