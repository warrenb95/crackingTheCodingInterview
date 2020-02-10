def fib(n):
    if (n == 0 or n == 1):
        return n
    return fib(n - 1) + fib(n - 2)

def fibMem(n):
    return fibMemUtil(n, [0] * (n + 1))

def fibMemUtil(n, memo):
    if (n == 1 or n == 0):
        return n

    if (memo[n] == 0):
        memo[n] = fibMemUtil(n - 1, memo) + fibMemUtil(n - 2, memo)
    
    return memo[n]


fibN = fibMem(4)
print(fibN)