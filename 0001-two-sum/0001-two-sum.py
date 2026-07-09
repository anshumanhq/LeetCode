class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we need to find two num that sum reaches target
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []