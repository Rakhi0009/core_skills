nums = [-2,1,-3,4,-1,2,1,-5,4]

def max_sum_subarray(nums):
    start = end = s = 0
    max_sum = curr_sum = nums[0]
    i = 1

    while i < len(nums):
        if nums[i] > curr_sum+nums[i]:
            curr_sum = nums[i]
            s = i
        else:
            curr_sum += nums[i] 
        
        if curr_sum > max_sum:
            max_sum = curr_sum
            start = s
            end = i 
        i += 1
    return nums[start:end+1]

print(max_sum_subarray(nums))
    