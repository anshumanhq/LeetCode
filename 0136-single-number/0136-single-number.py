class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        check=0
        for num in nums:
            #if nums.count(num)>=2:
            #    continue
            #else:
            #    check=num
            check^=num
        return check