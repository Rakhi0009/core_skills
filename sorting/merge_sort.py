data = [3,6,8,2,10,5,19,4]


def merge(left_half, right_half):
    i = j = 0
    result = []

    while i <len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            result.append(left_half[i])
            i +=1
        else:
            result.append(right_half[j])
            j +=1
    result.extend(left_half[i:])
    result.extend(right_half[j:])
    return result

def merge_sort(input):
    if len(input) <= 1:
        return input
    
    mid = len(input)//2
    left_half_intput = merge_sort(input[:mid])
    right_half_input = merge_sort(input[mid:])

    return merge(left_half_intput, right_half_input)


print(merge_sort(data))