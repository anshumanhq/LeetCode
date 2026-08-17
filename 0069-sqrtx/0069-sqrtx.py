class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        #hme sqrt nikalna hai
        #1 ka1,2 ka 4, 3 ka 9, 4 ka 16
        #agar x=12 diya hai then left 3 aur right 4 ke bich me hai so 
        if x < 2:
            return x

        left, right = 1, x // 2
        while left <= right:
            mid = (left + right) // 2
            sq = mid * mid
            if sq == x:
                return mid
            elif sq < x:
                left = mid + 1
            else:
                right = mid - 1
        return right