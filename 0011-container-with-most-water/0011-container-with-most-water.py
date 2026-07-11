from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0
        
        while left < right:
            width = right - left
            min_height = min(height[left], height[right])
            water = width * min_height
            
            if water > max_water:
                max_water = water
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water