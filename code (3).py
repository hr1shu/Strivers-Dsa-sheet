## two sum problem
arr1 = [1,3,4,6]
target = 9


def twoSum(arr, target):
    values = dict()
    for i, elem in enumerate(arr):
        comp = target - elem
    
        if comp in values:
            return [values[comp], i]
        
        values[elem] = i
        
    return []


a = twoSum(arr1, target)
print(a)