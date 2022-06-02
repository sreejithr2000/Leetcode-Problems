
from typing import List

class Solution:
    def count_prime(self, num):
        
        '''isPrimeCount = 0
        if num < 2:
            return -1
        for i in range(2, num+1):
            for j in range(2, i):
                if i % j == 0:
                    isPrimeCount = isPrimeCount + 1
                    break
        if i % j == 0:
            return num - (isPrimeCount+1)
        else:
            return num - (isPrimeCount+2)'''

        '''num_store = []
        composite_store = []
        for i in range(2, num):
            num_store.append(i)
        print(num_store)

        for i in range(0, len(num_store)):
            while num_store[i] * num_store[i] < num :
                ans = 0
                for j in range(num_store[i], len(num_store)):
                    while ans < num_store[-1]:
                        composite_store.append(num_store[i] * j)
                        print(num_store[i] * j)
                        ans = num_store[i] * j
                        break
                break
        
        return len(num_store) - len(composite_store) + 1'''

        if num < 2:
            return 0
        result = [1] * num
        result[0] = result[1] = 0
        for i in range(2, num):
            if result[i] == 1:
                for j in range(i*i, num, i):
                    result[j] = 0
        return sum(result)


s = Solution()
ans = s.count_prime(11)
print(ans)

# https://leetcode.com/problems/count-primes/

