class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digs=''
        for digit in digits:
            digs+=str(digit)
        d2i2d=int(digs)+1
        result=[]
        for digit in str(d2i2d):
            result.append(int(digit))
        return result