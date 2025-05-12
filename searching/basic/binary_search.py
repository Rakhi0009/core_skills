input = [1,2,3,4,5,6,7,9,10]
target = 8

def binary_search(input, target):
    l = 0
    r = len(input)-1
    while l<=r:
        mid = (r+l) //2
        if input[mid] == target:
            return mid
        elif target > input[mid]:
            l = mid + 1
        else:
            r = mid - 1
    return l # In case target not in input, return l for next greater num or return r for next smaller num.


print(binary_search(input, target))

# Time complexity : O(logn)


