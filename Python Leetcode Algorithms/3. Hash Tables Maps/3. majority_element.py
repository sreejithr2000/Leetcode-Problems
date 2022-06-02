from typing import List

class Solution:
    def majority_element(self, arr):
        hash_map = {}
        for i in range(0, len(arr)):
            if arr[i] in hash_map:
                hash_map[arr[i]]+=1
            else:
                hash_map[arr[i]] = 1
                # hash_map.update({arr[i] : 1 })
        for i in hash_map:
            if hash_map[i] > float(len(arr)/2):
                return i

s = Solution()
ans = s.majority_element([2,2,1,1,1,2,2])
print(ans)

# https://leetcode.com/problems/majority-element/

