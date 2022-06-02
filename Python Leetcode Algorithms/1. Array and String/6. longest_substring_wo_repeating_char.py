from typing import List

class Solution:
    def longest_substring(self, s):
        if len(s) == 1:
            return 1
        if len(s) == len(set(s)):
            return len(s)
        long_substr = 0
        i = 0
        j = 0
        while j < len(s):
            if len(s[i:j+1]) == len(set(s[i:j+1])):
                j = j + 1
            else:
                if j - i  >= long_substr:
                    long_substr = j - i 
                i = i + 1
        if j - i >= long_substr:
            long_substr = j - i
        return long_substr

s = Solution()
ans = s.longest_substring('pwwkew')
print(ans)

# https://leetcode.com/problems/valid-mountain-array/
# 987/987 TC pass set() algorithm own