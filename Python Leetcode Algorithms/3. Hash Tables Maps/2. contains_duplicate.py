from typing import List

class Solution:
    def contains_duplicate(self, arr):
        # hash_table = []
        # for i in range(0, len(arr)):
        #     if arr[i] in hash_table:
        #         return True
        #     else:
        #         hash_table.append(arr[i])
        # return False

        if len(arr) == len(set(arr)):
            return False
        else:
            return True

s = Solution()
ans = s.contains_duplicate([1,2,3,3])
print(ans)

# https://leetcode.com/problems/contains-duplicate/

