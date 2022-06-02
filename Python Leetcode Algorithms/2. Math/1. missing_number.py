
from typing import List

class Solution:
    def missing_number(self, arr: List[int]):
        '''
        Implementation using Hashing - o(n) time and space complexity

        n = max(arr)
        num = 0
        hash_list = []
        for i in range(0, len(arr)):
            if len(arr) not in arr:
                return len(arr)
        for i in range(0, n+1):
            hash_list.append(num)
            num = num + 1
        for i in range(0, len(hash_list)):
            if hash_list[i] in arr:
                pass
            else:
                return(hash_list[i])
        '''

        #Implemetation using formula - 0(n) time and o(1) space

        sum = 0
        for i in range(0, len(arr)):
            sum = sum + arr[i]
        formula = len(arr) * (len(arr) + 1)/2
        return formula - sum


s = Solution()
ans = s.missing_number([3,0,1])
print(ans)

# https://leetcode.com/problems/move-zeroes/

