number = 12345

def sum_of_digit(number):
    if number == 0:
        return 0
    return number%10 + sum_of_digit(number//10)

result = sum_of_digit(number)
print(result)