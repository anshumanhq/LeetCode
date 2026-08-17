class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        #hme sqrt nikalna hai
        #1 ka1,2 ka 4, 3 ka 9, 4 ka 16
        #agar x=12 diya hai then left 3 aur right 4 ke bich me hai so 
        pre,curr=0,1
        while curr*curr<=x:
            curr+=1
            pre+=1
        return pre 
