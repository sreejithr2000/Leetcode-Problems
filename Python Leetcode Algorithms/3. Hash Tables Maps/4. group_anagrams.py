from typing import List

class Solution:
    def group_anagrams(self, arr):
        hash_map = {}
        for i in range(0, len(arr)):
            hash_map[''.join(sorted(arr[i]))] = []
        for i in range(0, len(arr)):
            if ''.join(sorted(arr[i])) in hash_map:
                hash_map[''.join(sorted(arr[i]))].append(arr[i])
            
        # return hash_map
        output = []
        for i in hash_map:
            output.append(hash_map[i])
        return output

s = Solution()
ans = s.group_anagrams(["eat","tea","tan","ate","nat","bat"])
print(ans)

# https://leetcode.com/problems/group-anagrams/

