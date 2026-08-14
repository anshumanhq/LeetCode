class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                # Last element se swap kar do (kyunki order matter nahi karta)
                nums[i] = nums[n - 1]
                n -= 1
            else:
                i += 1
        return n