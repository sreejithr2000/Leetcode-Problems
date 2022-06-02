from typing import List

class Solution:
    def single_number(self, arr: List[int]):
        sum_original = 0
        sum_set = 0
        for i in range(0, len(arr)):
            sum_original = sum_original + arr[i]
        arr = list(set(arr))
        for i in range(0, len(arr)):
            sum_set = sum_set + arr[i]
        sum_set = 2 * sum_set

        return sum_set - sum_original

s = Solution()
ans = s.single_number([4,1,2,1,2])
print(ans)

# https://leetcode.com/problems/single-number/

