class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n - 2):
            # If the smallest number is positive, no triplet can sum to 0
            if nums[i] > 0:
                break

            # Skip duplicate first elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicate left values
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicate right values
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    # Move pointers inward for next unique triplet
                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return result