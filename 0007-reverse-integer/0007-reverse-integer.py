class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_neg=False
        if x<0:
            is_neg=True
            x=x*(-1)
        num=str(x)
        res=''
        #for l in num[::-1]:
        #    res+=l
        res=num[::-1]
        res=int(res)
        if is_neg:
            res*=(-1)
        limit=[(-2)**31, (2)**31 - 1]
        if (res<limit[0] or res>limit[1]): # range limit of  signed 32-bit integer range
            return 0
        return res