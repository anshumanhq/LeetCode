class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        # Always binary search on the smaller array for O(log(min(m,n)))
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        low, high = 0, m

        while low <= high:
            i = (low + high) // 2 # partition in nums1
            j = (m + n + 1) // 2 - i # partition in nums2

            # Handle edge cases with -inf and +inf
            left1 = nums1[i-1] if i > 0 else float('-inf')
            right1 = nums1[i] if i < m else float('inf')
            left2 = nums2[j-1] if j > 0 else float('-inf')
            right2 = nums2[j] if j < n else float('inf')

            # Correct partition found
            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2 == 0: # even total length
                    return (max(left1, left2) + min(right1, right2)) / 2.0
                else: # odd total length
                    return max(left1, left2)

            # If left1 > right2, we need to move partition i left
            elif left1 > right2:
                high = i - 1
            # Else move partition i right
            else:
                low = i + 1