#longest consecutive subsequence efficient approach

def longer(arr, n):
    s = set()
    ans = 0
    curr = 0
    
    for ele in arr:
        s.add(ele)
    
    for i in range(n):
        if arr[i]-1 not in s:
            j = arr[i]
            while j in s:
                j += 1
            
            ans = max(ans, j-arr[i])
    return ans
    
if __name__ == '__main__':
    n = 7
    arr = [1, 9, 3, 10, 4, 20, 2]
    print ("Length of the Longest contiguous subsequence is "),
    print (longer(arr, n))
            
        