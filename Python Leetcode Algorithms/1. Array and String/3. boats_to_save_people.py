from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0
        i = 0
        j = len(people) - 1
        while i <= j:
            if i == j:
                boats = boats + 1
                break
            if people[i] + people[j] <= limit:
                boats = boats + 1
                i = i + 1
                j = j - 1
            if people[i] + people[j] > limit:
                boats = boats + 1
                j = j - 1
        return boats
                
s = Solution()
ans = s.numRescueBoats([3,2,2,1], 3)  

# sort = 1,2,2,3 and limit 3
# 3
# 1,2
# 2

print(ans)    
    
# https://leetcode.com/problems/boats-to-save-people/