class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length=len(nums)
        #nums will already sorted
        numsc=[]
        count=0
        for num in nums:
            if num not in numsc:
                numsc.append(num)
            else:
                count+=1
        for i in range(len(numsc)):
            nums[i] = numsc[i]
        
        return len(numsc)