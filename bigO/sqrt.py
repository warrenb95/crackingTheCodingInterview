def sqrt(n:int):
    return sqrtHelper(n, 1, n)

def sqrtHelper(n:int, min:int, max:int):
    if max < min: return -1
    guess = int((min + max) / 2)
    if guess * guess == n:
        return guess
    elif guess * guess < n:
        return sqrtHelper(n, guess + 1, max)
    else:
        return sqrtHelper(n, min, guess + 1)

'''
My answer:

    It's divide and conquer:

        O(log n) i think :/
'''