def sliding_Window(arr, k):
    max_sum = 0
    i = 0
    j = k - 1
    while j < len(arr):
        curr_sum = 0
        for m in range(i, j+1):
            curr_sum = curr_sum + arr[m]

        if curr_sum > max_sum:
            max_sum = curr_sum
        i = i + 1
        j = j + 1
     
    return(max_sum)

arr = [1,5,7,3,2,1,6]
k = 3
max_sum = sliding_Window(arr, k)
print(max_sum)

# LeetCode In Python 50 Algorithms Coding Interview Questions\4. TECHNIQUE  Sliding Window (OPTIONAL)
    