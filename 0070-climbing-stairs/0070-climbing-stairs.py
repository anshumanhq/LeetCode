class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #jab hm analisys krte hain then hme pata chalta hai ye ek fabonachi series hi return kr raha hai 
        #like for 2,3,4,5,6,7,8 ke liye 2,3,5,8,13,21,etc
        a,b=1,1
        for _ in range(n):
            a,b=b,a+b
        return a