input_list = [3,5,10,19,30,0,1]
result_sum = 0
def sum_of_list(input_list, i = 0):
    global result_sum
    if i >= len(input_list):
        return result_sum
    result_sum += input_list[i]
    i+=1
    return sum_of_list(input_list, i)

print(sum_of_list(input_list))

    
    