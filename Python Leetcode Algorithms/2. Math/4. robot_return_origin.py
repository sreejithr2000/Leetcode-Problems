from typing import List

class Solution:
    def robot_return_origin(self, s):
        pos1 = 0
        pos2 = 0
        for i in range(0, len(s)):
            if s[i] == "U":
                pos2+=1
            elif s[i] == "D":
                pos2-=1
            elif s[i] == "L":
                pos1-=1
            elif s[i] == "R":
                pos1+=1
        if pos1 == 0 and pos2 == 0:
            return True
        else:
            return False

s = Solution()
ans = s.robot_return_origin("LL")
print(ans)

# https://leetcode.com/problems/robot-return-to-origin/

