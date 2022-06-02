from typing import List

class Solution:
    def two_sum(self, arr, target):
        hash_table = {}
        
        for i in range(0, len(arr)):
            goal = target - arr[i]
            if goal in  hash_table:
                return [hash_table[goal],i]
            else:
                hash_table[arr[i]] = i

s = Solution()
ans = s.two_sum([2,7,11,15],9)
print(ans)

# https://leetcode.com/problems/two-sum/

