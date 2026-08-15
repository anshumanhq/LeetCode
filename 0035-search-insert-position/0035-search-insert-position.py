class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #agr prsent hai then uska index return kro
        #agar present nahi hai then ek for loop se find kro ki kisake bich me aayega us index se +1 return kro
        if target in nums:
            return nums.index(target)
        if nums[0]>target:
            return 0
        else:
            for i in range(len(nums)):
                if nums[i]<target:
                    try:
                        if nums[i+1]>target:
                            return i+1
                    except IndexError:
                        return i+1
                    continue