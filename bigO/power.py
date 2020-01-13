def power(a:int, b:int):
    if b < 0:
        return 0
    elif b == 0:
        return 1
    else:
        return(a * power(a, b -1))

'''
My answer:

    It runs b - 1 times:

        O(n) 
'''