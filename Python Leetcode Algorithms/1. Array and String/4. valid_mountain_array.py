from typing import List

class Solution:
    def valid_mountain(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        i = 1
        while(i < len(arr) and arr[i] > arr[i-1] ):
            i = i + 1
        if i == 1 or i == len(arr):
            return False
        while( i < len(arr) and arr[i] < arr[i-1] ):
            i = i + 1
        if i == len(arr):
            return True
        else:
            return False
        
s = Solution()
ans = s.valid_mountain([0,2,3,4,5,2,1])
print(ans)

# https://leetcode.com/problems/valid-mountain-array/