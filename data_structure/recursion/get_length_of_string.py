string = "rakhi"

def get_length_of_string(string, i=0):
    if i == len(string):
        return 0
    return 1 + get_length_of_string(string, i + 1)

result = get_length_of_string(string)
print(result)