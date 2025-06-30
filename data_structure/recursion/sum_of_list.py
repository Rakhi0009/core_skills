input_list = [3,5,10,19,30,0,1]

def compute_sum(input_list):
    if len(input_list) == 0:
        return 0
    return input_list[0] + compute_sum(input_list[1:])

result = compute_sum(input_list)
print(result)

    
