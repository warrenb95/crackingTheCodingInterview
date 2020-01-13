def div(a:int, b:int):
    count = 0
    sum = b
    while sum <= a:
        sum += b
        count += 1
    
    return count

'''
My answer:

    The code will run a / b times:

        i think it is O(a/b)
'''