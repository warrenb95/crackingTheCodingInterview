'''
    A child is running up a staircase with n steps and can hop either 1 step, 2 steps or 3 at a time.
    Implement a method to count how many possible ways the child and run the stais.

    Assuming:
        n > 0


'''

# def triple_step(n):
#     if (n < 0 ): return 0
#     if (n == 0): return 1

#     return triple_step(n - 1) + triple_step(n - 2) + triple_step(n - 3)

# print(triple_step(10))

def triple_step(n, memo):
    if (n < 0 ): return 0
    if (n == 0): return 1

    if memo[n] == 0:
        memo[n] = triple_step(n - 1, memo) + triple_step(n - 2, memo) + triple_step(n - 3, memo)
    
    return memo[n]

print(triple_step(10, ([0] *11)))