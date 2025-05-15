data = [4,2,7,1,3]


def quick_sort(data):
    if len(data) <= 1:
        return data
    
    pivot = data[0]

    left =  [l for l in data[1:] if l <= pivot]
    right = [r for r in data[1:] if r >= pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort(data))

def quick_sort_inplace(data, low, high):
    if low < high:
        pi = partition(data, low, high)
        quick_sort_inplace(data, low, pi-1)
        quick_sort_inplace(data, pi+1, high)


def partition(data, low, high):
    pivot = data[high]
    i = low

    for j in range(low, high):
        if data[j] < pivot:
            data[i], data[j] = data[j], data[i]
            i += 1
    data[i], data[high] = data[high], data[i]
    return i


quick_sort_inplace(data, 0, len(data)-1)
print(data)
