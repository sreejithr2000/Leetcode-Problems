from typing import List

class Solution:
    def contain_most_water(self, arr: List[int]):
        max_area = 0
        curr_area = 0
        i = 0
        j = len(arr) - 1
        while i < j:
            curr_area = min(arr[i], arr[j]) * (j - i)
            if curr_area > max_area:
                max_area = curr_area
            if arr[i] < arr[j]:
                i = i + 1
            else:
                j = j - 1
        print(max_area)

s = Solution()
s.contain_most_water([1,8,6,2,5,4,8,3,7])

# https://leetcode.com/problems/container-with-most-water/