n = 5

# i = 0
# a,b =0,1
# while i < n:
#     if i > 1:
#        c= a+b
#        print(c)
#        a,b = b ,c
#     else:
#         print(i)
#     i += 1

def fibonacci(n):
    if n == 0:        # Base case
        return 0
    elif n == 1:      # Base case
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# result = fibonacci(n)
# print(result)

for i in range(10):
    result = fibonacci(i)
    print(result)

    


