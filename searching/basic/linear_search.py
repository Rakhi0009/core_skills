input = [1,4,6,3,7,8,5]
target = 5

def linear_search(input: list, target: int):
    for indx, val in enumerate(input):
        if val == target:
            return indx
        
print(linear_search(input, target))
        
