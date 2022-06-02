from typing import List

class Solution:
    def four_sum_count(self, num1, num2, num3, num4):
        ans = 0
        hash_map = {}
        for i in range(0, len(num1)):
            for j in range(0, len(num2)):
                if num1[i] + num2[j] in hash_map:
                    hash_map[num1[i] + num2[j]] += 1
                else:
                    hash_map[num1[i] + num2[j]] = 1
        
        for i in range(0, len(num3)):
            for j in range(0, len(num4)):
                if -(num3[i] + num4[j]) in hash_map:
                    ans = ans + hash_map[-(num3[i] + num4[j])]
        
        return ans

s = Solution()
ans = s.four_sum_count([1,2], [-2,-1], [-1,2], [0,2])
print(ans)

# https://leetcode.com/problems/4sum-ii/

