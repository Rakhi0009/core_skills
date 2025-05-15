data = [4,2,7,1,3]

def insertion_sort(data):
    for i in range(1,len(data)):
        while i != 0:
            if data[i] < data[i-1]:
                data[i] , data[i-1] = data[i-1], data[i]
                i -= 1
            else:
                break
    return data

print(insertion_sort(data))