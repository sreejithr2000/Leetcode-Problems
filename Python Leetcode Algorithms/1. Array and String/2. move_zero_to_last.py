
from typing import List

class Solution:
    def move_zero(self, arr: List[int]):
        j = 0
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[j] = arr[i]
                j = j + 1
        for x in range(j, len(arr)):
            arr[x] = 0
        print(arr)

        # arr1 = []
        # for i in range(0, len(arr)):
        #     if arr[i] != 0:
        #         arr1.append(arr[i])
        # for i in range(len(arr1), len(arr)):
        #     arr1.append(0)
        # arr = arr1
        # print(arr)

s = Solution()
s.move_zero([0,2,0,1,4])

# https://leetcode.com/problems/move-zeroes/

