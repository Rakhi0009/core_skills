data = [[2,5,3,6],[7,19,4,35,5],[3,1,0]]



def merge_2_list(left, right):
    i = j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort_list(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort_list(arr[:mid])
    right = merge_sort_list(arr[mid:])
    return merge_2_list(left, right)

def merge_sort_k_lists(lists, left, right):
    if left ==  right:
        return merge_sort_list(lists[left])
    
    mid = (left + right)//2
    l = merge_sort_k_lists(lists, left, mid)
    r = merge_sort_k_lists(lists, mid+1, right)
    return merge_2_list(l,r)


def merge_k_lists(lists):
    if len(lists) <=0:
        return []
    return merge_sort_k_lists(lists, 0, len(lists)-1)

print(merge_k_lists(data))
    