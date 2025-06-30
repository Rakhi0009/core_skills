# print 1 to n without loops

def custom_print(n,i=1):
    if i > n:
        return 
    print(i)
    custom_print(n,i+1)

custom_print(5)
