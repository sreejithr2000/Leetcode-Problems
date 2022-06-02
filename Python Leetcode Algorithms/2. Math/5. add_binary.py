from typing import List

class Solution:
    def add_binary(self, a, b):
        if len(a) > len(b):
            b = b[::-1]
            while len(a) != len(b):
                b += "0"
            b = b[::-1]
        elif len(a) < len(b):
            a = a[::-1]
            while len(a) != len(b):
                a += "0"
            a = a[::-1]

        state_map = [["00", "0", "0"], ["01", "1", "0"], ["10", "1", "0"], ["11", "0", "1"], ["000", "0", "0"], ["001", "1", "0"], ["010", "1", "0"], ["011", "0", "1"], ["100", "1", "0"], ["101", "0", "1"], ["110", "0", "1"], ["111", "1", "1"]]
        carry = "0"
        result = ""
        i = len(a) - 1
        j = len(b) - 1
        while i >= 0  and j >= 0:
            operation = carry + a[i] + b[i]
            for k in range(0, len(state_map)):
                if state_map[k][0] == operation:
                    result += state_map[k][1]
                    carry = state_map[k][2]
                    i -= 1
                    j -= 1
        if (result + carry)[::-1][0] == "0":
            return((result + carry)[::-1][1:])
        else:
            return((result + carry)[::-1])

s = Solution()
ans = s.add_binary("1", "100")
print(ans)

# https://leetcode.com/problems/add-binary/

