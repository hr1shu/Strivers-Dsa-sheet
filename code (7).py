#longest subarray sum efficient approach

def longest(arr,n,summ):
    s = {}
    prefix_sum = 0
    res = 0
    for i in range(n):
        prefix_sum += arr[i]
        if prefix_sum == summ:
            res = i+1
            
        if prefix_sum - summ in s:
            res = max(res, i-s[prefix_sum-summ])
        else:
            s[prefix_sum] = i
            
    return res
    
    
if __name__ == "__main__":
    arr = [8, 3, -7, -4, 1]
    n = len(arr)
    summ = -10
    
    print(longest(arr,n,summ))