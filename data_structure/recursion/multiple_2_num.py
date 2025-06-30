

a = 3
b = 4

def custom_multiple(a,b):
    if b == 0:
        return 0
    return a + custom_multiple(a, b-1)

result = custom_multiple(a,b)
print(result)
    