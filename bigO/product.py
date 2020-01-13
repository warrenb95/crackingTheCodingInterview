def product(a:int, b:int):
    sum = 0
    for i in range(b):
        sum += a

    return sum

'''
My answer:

    The for loop is run b times,
    therefore the runtime of this is:
        
        O(n)

'''